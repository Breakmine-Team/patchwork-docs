# ItemEdible
Minimum Patchwork: [|octicons-history-24||v1.1.0|]

??? info "Under Development"

    Both Patchwork and its documentation are currently under active development.
    
    As new updates are introduced to Patchwork, these pages will be updated to match. Please expect occasional issues, incomplete sections, or temporary inconsistencies as the software and reference materials evolve alongside each other.

> **Extends:** `Item`  
> Base class for consumable food items.

## Constructor

### `constructor(id, textureSlotId = id)`
Creates a new edible item instance.

---

## Properties

### `number healAmount`
Property storing the number of health or hunger points restored when consumed.

---

## Methods

### `void onUse(world, x, y, z, itemstack, hitFace)`
Called when a Player uses or consumes the item.