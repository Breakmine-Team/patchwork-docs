# Setting Up Your First Mod

??? info "Under Development"

    Both Patchwork and its documentation are currently under active development.
    
    As new updates are introduced to Patchwork, these pages will be updated to match. Please expect occasional issues, incomplete sections, or temporary inconsistencies as the software and reference materials evolve alongside each other.

Before adding new thingamajigs to Breakmine, you need to structure your mod correctly so that Patchwork can discover and load them.

## Directory Structure

Create a new folder inside your Breakmine mods directory with your mod's internal identifier:

```text
mods/
└── my_custom_mod/
    ├── ModData.json          # required — mod metadata
    ├── ModLoad.js            # optional — entry point, called on load
    ├── icon.png              # optional — shown in the Mods screen
    ├── blocks/               # custom blocks (one class per .js file)
    │   └── BlockExample.js
    ├── items/                # custom items
    │   └── ItemExample.js
    ├── crafting/             # crafting recipes for your blocks
    │   └── BlockExampleCrafting.js
    ├── smelting/             # smelting recipes for your blocks
    │   └── BlockExampleSmelting.js
    ├── gui/                  # custom GUI screens
    │   └── GuiExample.js
    ├── gui_textures/         # .png textures for GUI screens
    ├── commands/             # chat commands
    │   └── CommandExample.js
    ├── tabs/                 # custom creative inventory tabs
    │   └── TabExample.js
    ├── patches/              # file patches (paths mirror src/js/)
    │   └── net/minecraft/client/ModLoader.js
    ├── textures/             # .png block/item textures
    │   └── example.png
    └── sounds/               # .ogg sounds
        └── example.ogg
```

Only `ModData.json` is required; everything else is optional and discovered by folder.

!!! tip
    When packaging a **ZIP** you may instead ship a `ModData.js` class with static metadata fields — Patchwork parses it and stores a `ModData.json` for you. See [Packaging](packaging.md).

## ModData

`ModData.json` is plain JSON:

```json
{
    "NAME": "My Custom Mod",
    "ID": "my_custom_mod",
    "AUTHOR": "You",
    "VERSION": "1.0.0",
    "DESCRIPTION": "What the mod does",
    "LICENSE": "MIT"
}
```

- `ID` must be 1-64 characters of letters, numbers, `_` or `-`. It is used as the namespace for everything the mod registers (`my_custom_mod:example_block`).
- `NAME` is shown in tooltips and the Mods screen.
- `VERSION` is shown in the Mods screen and included in the multiplayer handshake.

## ModLoad.js

If a `ModLoad.js` exists, its default-exported class is instantiated and `onLoad(world, minecraft, modLoader)` is called after all of the mod's files have been registered:

```js
export default class ModLoad {
    static onLoad(world, minecraft, modLoader) {
        console.log('[ModLoad] My mod loaded!');

        // The third argument is the ModLoader. Anything registered here
        // (commands, hooks, keybinds, ...) is remembered and removed again
        // automatically when the mod is disabled or uninstalled.
        modLoader.registerCommand(
            "example",
            "",
            "An example command",
            (mc, args) => {
                mc.addMessageToChat("§7Hello from my mod!");
                return true;
            }
        );
    }
}
```

`ModLoad.js` may use ES `import` statements; Patchwork resolves them against other files inside your mod.

## ID conversion rules

Class names in `blocks/`, `items/`, `crafting/` and `smelting/` convert to IDs automatically:

| Class name | Registered as (in mod `my_mod`) |
| ---------- | ------------------------------- |
| `BlockExampleBlock` | `my_mod:example_block` |
| `ItemExampleIngot` | `my_mod:example_ingot` |
| `BlockExampleBlockCrafting` | crafting recipe for `my_mod:example_block` |
| `BlockExampleBlockSmelting` | smelting recipe for `my_mod:example_block` |

CamelCase is split into words, a leading `Block`/`Item` prefix and a trailing `Crafting`/`Smelting` suffix are stripped, and the rest is lowercased with underscores.

## Installing a mod

From the in-game **Mods** screen you can:

- **Install a `.zip`** package,
- **Install a folder** (select the mod folder; it must contain `ModData.json` or `ModData.js` at its root),
- **Install a `.jph`** patch package — Patchwork detects the format by content, so either file type works through the same installer.

Alternatively:

- Drop the folder into the game's on-disk `mods/` directory and restart. Disk mods always take a stable place in the list and cannot be deleted from inside the game.
- Load a development ZIP straight from a URL (`loadDevModFromUrl`) — it is kept fully in memory.
- Connect to a server that ships mods; the server version of a mod replaces your local one while you are connected.

Mods remember their enabled/disabled state across sessions.

---

Continue with the [Example Mod](index.md) walkthrough, or jump to the [ModAPI reference](../API/mod_api.md).