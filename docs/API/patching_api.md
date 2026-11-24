# Patching

Minimum Patchwork: [|octicons-history-24||v1.1.0|]

??? info "Under Development"

    Both Patchwork and its documentation are currently under active development.
    
    As new updates are introduced to Patchwork, these pages will be updated to match. Please expect occasional issues, incomplete sections, or temporary inconsistencies as the software and reference materials evolve alongside each other.

Beyond registering new content, Patchwork can **patch existing game files** — every file under `src/js/` is registered in a module registry, so a mod can replace or extend any class, function or constant the game ships with.

## How it works

The `ModulePatcher` is a static registry of game files (built at compile time with Vite's `import.meta.glob`). Patching a file imports it once and hands its **live module namespace** to your patch function; because modules are cached, patching a class the game already loaded works on the exact object the game is using.

!!! warning "Raw builds"
    In a raw (non-bundled) deployment the registry is empty; `ModulePatcher.isAvailable()` returns `false` and patching reports itself as unavailable. Always check availability before shipping patches that must run.

## Patch scripts

A patch script is plain JavaScript (no `import`/`export`) that receives two arguments:

- `exports` — the target file's live module namespace object.
- `api` — `{ modId, file, log(...), warn(...) }` for prefixed logging.

The script mutates the exports (replacing methods, wrapping functions, adding properties) and may **return a cleanup function** that restores the original behaviour. The cleanup is called automatically when the patch is reverted.

```js
// patches/net/minecraft/client/Minecraft.js
const originalStart = exports.default.prototype.startGame;
exports.default.prototype.startGame = function (...args) {
    api.log('startGame patched!');
    return originalStart.apply(this, args);
};

// cleanup
return function cleanup() {
    exports.default.prototype.startGame = originalStart;
};
```

## Shipping patches

There are two ways to ship patches; both use the same script contract:

1. **Inside a mod folder** — place one script per target under `patches/`, mirroring the path inside `src/js/`:

```text
my_mod/
└── patches/
    └── net/minecraft/client/ModLoader.js
```

2. **As a `.jph` package** — a standalone JSON document with one patch per target. See [Packaging](../Example%20Mod/packaging.md#jph-patch-packages).

Patches are applied after the mod's content files and `ModLoad.js` have run, and are reverted and reapplied in original order whenever mods are toggled — so two mods patching the same file never leave it half-patched.

## API reference

The `ModulePatcher` class (also reachable via `ModAPI.patchFile`, `ModAPI.loadFileModule` and `ModAPI.listPatchableFiles`) provides:

### `bool isAvailable()`
Returns whether the current build has a module registry at all.

### `string[] listFiles()`
Lists every patchable file, relative to `src/js/`.

### `Promise<Module> loadModule(file)`
Imports a game file and caches its namespace. Paths may be given with or without the `src/js/` prefix.

### `Promise<Handle> patch(modId, file, fn)`
Applies a patch function to a file. `fn(exports, api)` may be synchronous or async, and may return a cleanup function. Each patch gets a global `order` number used for deterministic unwinding.

### `Promise<Handle> applySource(modId, file, source)`
Evaluates a patch **script** (as shipped in `patches/` or `.jph`) against a file.

### `Handle[] patchesOf(modId)` / `string[] patchedFiles()`
Introspection: the patches a mod applied, and every file currently patched.

### `number revert(modId)`
Removes every patch the mod applied. For each affected file, all patches are unwound via their cleanup functions (newest first) and the surviving patches from other mods are reapplied in their original order. Returns the number of reverted patches.

### `number revertAll()`
Reverts every patch from every mod.

!!! tip
    You rarely call `ModulePatcher` directly: prefer `ModAPI.patchFile(file, fn)` inside `ModLoad.js`, or ship `patches/` files and let the loader apply them.
