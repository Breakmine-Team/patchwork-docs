# Item
Minimum Patchwork: [|octicons-history-24||v1.1.0|]

??? info "Under Development"

    Both Patchwork and its documentation are currently under active development.
    
    As new updates are introduced to Patchwork, these pages will be updated to match. Please expect occasional issues, incomplete sections, or temporary inconsistencies as the software and reference materials evolve alongside each other.

## Constructor

### `constructor(id, textureSlotId = id)`
Creates a new base item instance and registers it in the Item Registry.

---

## Properties

### `string|null description`
Property storing the display name or Tooltip text for the item.

### `bool isTool`
Property flag identifying if the item behaves as a tool or weapon. Defaults to `false`.

### `number durability`
Property storing the maximum durability or durability uses of the item.

---

## Methods

### `string getTextureForFace(face)`
Returns the texture key or path used when rendering the item in hand, on the GUI, or dropped in the world.

### `string|null getDescription()`
Returns the Tooltip description text for the item.

### `bool isItem()`
Returns `true` to identify this object as an Item.

### `static Item|null getById(itemId)`
Retrieves a registered Item instance by its numerical ID.