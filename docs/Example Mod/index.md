# About This Example

??? info "Under Development"

    Both Patchwork and its documentation are currently under active development.
    
    As new updates are introduced to Patchwork, these pages will be updated to match. Please expect occasional issues, incomplete sections, or temporary inconsistencies as the software and reference materials evolve alongside each other.

!!! note "Compatibility"
    This mod has been tested to work on Patchwork[|octicons-history-24||v1.1.0|] and later.

**Patchwork** is a mod loader; and as such it needs some examples!  
This section walks you through building **Unbreakable Blocks** — a small but complete mod that ships with Breakmine in `example_mods/unbreakable_block/`. It covers everything a real mod needs:

- a `ModData` manifest and a `ModLoad.js` entry point,
- a custom **block** with its own texture and tooltip,
- a custom **item** (an Unbreakable Ingot),
- a **crafting recipe** that turns four ingots into an unbreakable block,
- a custom **creative tab** to hold them,
- a chat **command** with arguments (`/unbreakable give <count>`),
- a **keybind**, an **HUD overlay** and **JSON storage** registered from `ModLoad.js`,
- and a **render hook** demo.

## Pages

1. [Setting Up Your First Mod](setup.md) — mod structure, ModData and installing.
2. [Packaging & Distribution](packaging.md) — ZIP layout and `.jph` patch packages.
3. [ModAPI Reference](../API/mod_api.md) — every method your mod can call.
4. [Patching](../API/patching_api.md) — replacing game files at runtime.

The finished source lives in the Breakmine repository at `example_mods/unbreakable_block/`; clone it, drop the folder into your `mods/` directory, and play with it while you read.