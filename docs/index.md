# Patchwork

??? info "Under Development"

    Both Patchwork and its documentation are currently under active development.
    
    As new updates are introduced to Patchwork, these pages will be updated to match. Please expect occasional issues, incomplete sections, or temporary inconsistencies as the software and reference materials evolve alongside each other.

**Patchwork** is an advanced mod loading framework initially created by [SpinningCubes](https://github.com/spinning-cubes).  
It is specifically designed to expand and extend the capabilities of Breakmine; providing modders with the systems needed to create complex, feature-rich additions and custom functionality that go beyond the standard gameplay.

Current Patchwork version: **v1.1.0**

---

## What Patchwork does

Patchwork ships inside Breakmine as the `ModLoader` plus a small set of registries. It discovers, loads, toggles and unloads mods from several sources, and gives every mod a scoped **ModAPI** object so anything a mod registers is automatically removed again when the mod is disabled, reloaded or uninstalled.

### Mod formats

| Format | Description |
| ------ | ----------- |
| **Folder** | A folder inside the Breakmine `mods/` directory (or selected through the Mods screen) containing `ModData.json` and your mod's code. |
| **ZIP package** | A `.zip` with a `ModData.js` (or `ModData.json`) metadata class at its root, plus `ModLoad.js`, `blocks/`, `items/`, textures, sounds, recipes, commands, tabs, GUIs and patches. |
| **`.jph` patch package** | A JSON document (JavaScript PatcH package) holding metadata and one patch script per game file. Ideal for distributing pure code patches without assets. |
| **Disk mods** | Mods placed in the game's on-disk `mods/` folder are picked up automatically and cannot be deleted from inside the game. |
| **Server mods** | An integrated/server host can push mods to connecting clients during the handshake; the server version replaces a locally installed mod of the same ID and is unloaded again on disconnect. |
| **Dev mods** | `loadDevModFromUrl(url)` loads a ZIP from a URL entirely in memory for development. |

### Registries

- **Blocks & items** — declare classes in `blocks/` and `items/`; class names convert to namespaced IDs automatically (`BlockUnbreakableBlock` in mod `unbreakable_block` becomes `unbreakable_block:unbreakable_block`).
- **Crafting & smelting** — recipe classes in `crafting/` and `smelting/`.
- **Textures, GUI textures & sounds** — `textures/*.png`, `gui_textures/*.png` and `sounds/*.ogg` are stored and addressed with `modid:name` keys.
- **GUI screens** — custom screens in `gui/`.
- **Commands** — `commands/*.js` classes or `ModAPI.registerCommand()`; they appear in `/help` and chat autocomplete, and work on client and server alike.
- **Custom creative tabs** — `tabs/*.js` or `ModAPI.registerCustomTab()`.

### ModAPI hooks

Every mod receives a `ModAPI` object with:

- Commands, **render hooks** (`beforeRender`, `renderChunks`, `renderSky`, `renderBlockHitBox`, `afterRender`, `onTick`),
- **Keybinds** with settings integration,
- **Overlay text** drawing on the HUD (text, tooltips, rects),
- **Block actions** — a generic event bus for block interactions,
- **JSON storage** scoped to your mod (`saveJson` / `loadJson` / `deleteJson` / `listJson`),
- **Services** — shared objects other mods can look up,
- **Networking** — `sendModMessage()` to send payloads to the server.

### File patching

The **ModulePatcher** lets a mod replace or extend any game file under `src/js/`. Patches receive the target file's live module exports and may return a cleanup function; patches are fully unwound and reapplied in order when mods are toggled, so two mods touching the same file never leave it half-patched. Patches can ship as `patches/<path>.js` inside a mod folder or as standalone `.jph` packages.

See [Patching](API/patching_api.md) and [ModAPI](API/mod_api.md) for the full reference, or start with the [Example Mod](Example%20Mod/index.md).