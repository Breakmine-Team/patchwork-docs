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
    ├── mod.json
    └── main.js
```