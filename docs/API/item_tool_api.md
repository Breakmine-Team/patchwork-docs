# ItemTool
Minimum Patchwork: [|octicons-history-24||v1.1.0|]

??? info "Under Development"

    Both Patchwork and its documentation are currently under active development.
    
    As new updates are introduced to Patchwork, these pages will be updated to match. Please expect occasional issues, incomplete sections, or temporary inconsistencies as the software and reference materials evolve alongside each other.

> **Extends:** `Item`  
> Base class for tools, weapons, and harvest utilities.

## Constructor

### `constructor(id, textureName, name, material, toolType)`
Creates a new tool instance with specified material properties, tool type, and auto-calculated durability.

---

## Properties

### `string material`
Property defining the tier material (e.g., `'wood'`, `'stone'`, `'iron'`, `'diamond'`, `'gold'`).

### `string toolType`
Property defining the Tool Category (e.g., `'pickaxe'`, `'axe'`, `'shovel'`).

---

## Methods

### `number efficiency()`
Returns the mining speed multiplier based on the tool's material tier.