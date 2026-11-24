# Packaging & Distribution

??? info "Under Development"

    Both Patchwork and its documentation are currently under active development.
    
    As new updates are introduced to Patchwork, these pages will be updated to match. Please expect occasional issues, incomplete sections, or temporary inconsistencies as the software and reference materials evolve alongside each other.

Patchwork accepts three kinds of packages, told apart by their **content** — not their file extension.

## ZIP mods

A ZIP with the mod folder contents at its root:

```text
my_mod.zip
├── ModData.js              # or ModData.json
├── ModLoad.js
├── icon.png
├── blocks/
│   └── BlockExample.js
├── items/
│   └── ItemExample.js
├── crafting/
│   └── BlockExampleCrafting.js
├── smelting/
│   └── BlockExampleSmelting.js
├── commands/
│   └── CommandExample.js
├── tabs/
│   └── TabExample.js
├── gui/
│   └── GuiExample.js
├── gui_textures/
│   └── panel.png
├── patches/
│   └── js/net/minecraft/client/ModLoader.js
├── textures/
│   └── example.png
└── sounds/
    └── example.ogg
```

A `ModData.js` metadata class looks like this:

```js
export default class ModData {
    static NAME = "My Custom Mod";
    static ID = "my_mod";
    static AUTHOR = "You";
    static VERSION = "1.0.0";
    static DESCRIPTION = "What the mod does";
    static LICENSE = "MIT";
}
```

!!! note
    Only the layout paths listed in the [setup guide](setup.md#directory-structure) are imported. Arbitrary nested folders are ignored in ZIPs; use folder installs or a dev URL if you need arbitrary files.

## `.jph` patch packages

!!! warning
    JPH mods are under development and must be turned on manually in the Experiments screen.

A `.jph` — a **J**avascript **P**atc**H** package — is a single JSON document for distributing pure code patches, with no assets. It is installed through the same Mods screen as a normal mod; Patchwork converts it into a regular mod folder with `ModData.json` and one `patches/<path>.js` file per target.

```json
{
    "format": "jph",
    "version": 1,
    "id": "my_patch",
    "name": "My Patch",
    "author": "You",
    "description": "What this patch changes",
    "modVersion": "1.0.0",
    "createdAt": "2026-11-25T00:00:00.000Z",
    "patches": [
        {
            "file": "net/minecraft/client/ModLoader.js",
            "source": "console.log('[my_patch] ModLoader loaded', Object.keys(exports));"
        }
    ]
}
```

Rules enforced by the loader:

- `format` must be `"jph"` and `version` must be `1`.
- `id` must be lowercase letters, digits, `-` or `_`, at most 64 characters.
- Every `patches[].file` must be a `.js` path inside `src/js/` (a leading `src/js/` is stripped), and each target may only appear once.
- At least one patch is required.

Patch scripts follow the same contract as `patches/` files in a mod folder — see [Patching](../API/patching_api.md).

## Distribution checklist

1. Pick a stable, unique mod `ID` — it is the namespace for everything you register and cannot change later without breaking saves.
2. Bump `VERSION` on every release; it appears in the Mods screen and the multiplayer handshake.
3. Include an `icon.png` so your mod stands out in the Mods screen.
4. For code-only changes, prefer a `.jph` — it is a single small file users can install directly.
