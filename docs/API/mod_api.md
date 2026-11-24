# ModAPI

Minimum Patchwork: [|octicons-history-24||v1.1.0|]

??? info "Under Development"

    Both Patchwork and its documentation are currently under active development.
    
    As new updates are introduced to Patchwork, these pages will be updated to match. Please expect occasional issues, incomplete sections, or temporary inconsistencies as the software and reference materials evolve alongside each other.

Every mod receives a **ModAPI** object, scoped to the mod's ID. It is passed to `ModLoad.onLoad` as the third argument (`modLoader`) and is also available as `ModAPI` inside block, item, GUI, command and tab class files.

Anything registered through ModAPI is **tracked per mod**: when the mod is disabled, reloaded or uninstalled, all of its registrations (including file patches) are removed automatically.

---

## Properties

### `Minecraft .minecraft`
The running Minecraft client instance.

### `World .world`
Shortcut for `ModAPI.minecraft.world`.

### `string .modId`
The ID of the mod this API instance belongs to.

### `bool .isServer`
Always `false` on the client.

---

## Commands

### `Entry registerCommand(name, usage, description, execute, options = {})`
Registers a chat command. `execute(minecraft, args)` should return `true` when the command was handled. `options` may include `{ modId, opOnly }`. Commands appear in `/help` and chat autocomplete and work on client and server alike.

### `bool unregisterCommand(name)`
Removes a command previously registered by this mod.

### `Entry|null getCommand(name)`
Looks up any registered command by name.

---

## Render hooks

### `Handle registerRenderHook(hook, fn, options = {})`
Calls `fn(context)` at a specific point in the render loop. `context` contains `minecraft`, the relevant `worldRenderer`, and hook-specific payload (e.g. `partialTicks`). `options.priority` sorts hooks (lower runs first).

Available hooks:

- `beforeRender`
- `renderChunks`
- `renderSky`
- `renderBlockHitBox`
- `afterRender`
- `onTick`

### `bool unregisterRenderHook(hook, handle)`
Removes a hook. Accepts the handle returned by `registerRenderHook`, or the original function.

---

## Keybinds

### `Entry registerKeybind(id, name, defaultKey, onPress, options = {})`
Registers a keybind shown in the controls settings. `id` is 1-64 letters, numbers, `_` or `-`; `defaultKey` is a key string or `null`; `onPress({ key, keybind, minecraft })` fires when the key is pressed. `options` may include `onRelease`, `allowRepeat` and `category`.

The descriptor-object form is also supported: `registerKeybind({ id, name, defaultKey, onPress, onRelease })`.

### `bool unregisterKeybind(id)`
Removes a keybind registered by this mod.

### `Entry|null getKeybind(id)` / `string|null getKeybindKey(id)`
Look up a keybind, or the key the user currently has bound to it.

---

## Overlay text

### `Handle registerOverlayText(fn, options = {})`
Registers a HUD overlay provider. `fn(context)` is called every frame the overlay is drawn with a context containing:

- `context.text(value, x, y, options)` — draw one or more `\n`-separated lines; `options` supports `scale`, `color` (hex number or CSS string), `shadow`, `align` (`'left' | 'center' | 'right'`), `background` and `padding`.
- `context.tooltip(value, x, y, options)` — draw a Minecraft-style tooltip box.
- `context.rect(left, top, right, bottom, color, alpha)` — draw a filled rectangle.
- `context.measure(value, options)` — measure text without drawing.
- `context.width` / `context.height` — overlay dimensions; `context.minecraft`.

The alias `onOverlayText(fn)` does the same.

### `bool unregisterOverlayText(handle)`
Removes an overlay provider.

---

## Block actions

A lightweight event bus for block interactions.

### `Handle registerBlockAction(action, fn, options = {})`
Registers a handler for a named action. Alias: `onBlockAction`.

### `bool unregisterBlockAction(action, handle)` / `bool hasBlockAction(action)`
Remove or query a handler.

### `bool emitBlockAction(action, data)`
Fires all handlers registered for `action`.

---

## JSON storage

Persistent JSON files scoped to your mod, stored under `mod_data/<modId>/`:

### `Promise<Value> saveJson(key, value)`
Saves a JSON-serializable value. `key` must match `[A-Za-z0-9._-]{1,64}`.

### `Promise<Value|null> loadJson(key, fallback = null)`
Loads a value, returning `fallback` when missing or invalid.

### `Promise<bool> deleteJson(key)`
Deletes a stored file; resolves `true` when it existed.

### `Promise<string[]> listJson()`
Lists the keys currently stored by this mod.

---

## Services

Share objects between mods.

### `Service registerService(serviceId, service)`
Registers a shared object under an ID.

### `Service|null getService(serviceId)`
Retrieves a service registered by any mod.

---

## Custom creative tabs

### `Tab registerCustomTab(name, iconBlockId)`
Registers a creative inventory tab shown in the creative screen. Blocks and items can opt in by setting `inventoryTab` to the tab's name (string form).

---

## Networking

### `bool sendModMessage(payload)`
Sends `{ type: 'modMessage', modId, payload }` to the server through the active network connection. Returns `false` when not connected. Services registered with a `handleNetworkMessage(payload, networkManager)` method receive mod messages on both ends.

---

## Texture resolution

### `{ modId, textureName }|null resolveTexture(key)`
Resolves a `modid:name` texture key against installed mods.

---

## File patching

### `Handle patchFile(file, fn)`
Patches any game file under `src/js/` at runtime. See [Patching](patching_api.md).

### `Promise<Module> loadFileModule(file)`
Loads a game file's live module namespace without patching it.

### `string[] listPatchableFiles()`
Lists every game file available for patching in the current build.

---

## Utilities

### `log(...args)` / `warn(...args)`
Console logging prefixed with `[Patchwork] [<modId>]`.