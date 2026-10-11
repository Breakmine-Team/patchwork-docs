# Block
Minimum Patchwork: [|octicons-history-24||v1.0.0|]

??? info "Under Development"

    Both Patchwork and its documentation are currently under active development.
    
    As new updates are introduced to Patchwork, these pages will be updated to match. Please expect occasional issues, incomplete sections, or temporary inconsistencies as the software and reference materials evolve alongside each other.

## Constructor

### `constructor(id, textureSlotId = id)`
Creates a new block instance and registers it in the Block Registry.

---

## Properties

### `bool .multipart`
Property flag that, when set to `true` in the constructor, identifies the block as using dynamic multipart geometry instead of a standard single cube.

### `bool .description`
Sets the block's Tooltip.

### `int .hardness`
Sets the block's break speed.

### `bool .path`
Whether to render as a Grass Path or not.

### `bool .inventoryTab`
The inventory tab to add this block to. Defaults to `EnumCreativeInventoryTab.BUILDING_BLOCKS`.

### `string .mod`
The mod name that appears in the Tooltip. Patchwork automatically sets this to the mod's name.

### `int .id`
> **Warning**: Mods shouldn't mess with this.

This property returns the block's ID. Never hardcode IDs as they are bound to change.

### `Block.sounds .sound`
Sets the block's sound. Currently loaded sounds:
* `Block.sounds.stone`
* `Block.sounds.wood`
* `Block.sounds.gravel`
* `Block.sounds.grass`
* `Block.sounds.cloth`
* `Block.sounds.sand`
* `Block.sounds.glass`
* `Block.sounds.leaves`

---

## Methods

### `bool canCastAmbientOcclusion()`
Returns whether this block can cast Ambient Occlusion on neighboring Blocks.

### `bool onRender(world, x, y, z, blockRenderer)`
Called upon render of this Block by Block Renderer; returning `true` allows for overriding the block's rendering logic.

### `bool canInteract()`
Returns whether Players can interact with this Block.

### `MovingObjectPosition collisionRayTrace(world, x, y, z, start, end)`
Performs a raytrace against the block's bounding box (or multipart bounding boxes) to calculate collision hits.

### `bool getAmbientOcclusion()`
Returns a `bool` telling the Block Renderer if the block should receive Ambient Occlusion.

### `BoundingBox getBoundingBox(world, x, y, z)`
Returns the selection and outline Bounding Box for the block at the specified position.

### `BoundingBox getCollisionBoundingBox(world, x, y, z)`
Returns the solid collision Bounding Box for entity collision, or `null` if non-solid.

### `number getColor(world, x, y, z, face)`
Returns the hex color multiplier applied to the specified face during rendering.

### `string|null getDescription()`
Returns the Tooltip text for the block.

### `Array getDrop(world, x, y, z)`
Returns an array containing the dropped item ID and quantity when broken (defaults to `[id, 1]`).

### `number getHardness()`
Returns the base breaking Hardness of the Block in ticks.

### `number getId()`
Returns the numerical ID of the Block.

### `number getLightValue()`
Returns the Light level emitted by this Block (`0`–`15`).

### `Array|null getModel(world, x, y, z)`
Returns the default array of static block components and Bounding Box definitions for rendering.

### `Array|null getMultipart(world, x, y, z)`
Returns dynamic Multipart definitions and Bounding Box arrays based on surrounding world state (e.g. adjacent connecting blocks). If world is `null`, typically falls back to `getModel()`.

### `number getOpacity()`
Returns the Light opacity value of the Block (`1.0` for opaque, `0.0` for fully transparent).

### `number getParticleColor(world, x, y, z)`
Returns the color tint applied to breaking Particles.

### `EnumBlockFace getParticleTextureFace()`
Returns which face Texture is used for Block Particles.

### `string|null getPreferredToolType()`
Returns the preferred Tool Category required to efficiently mine this Block.

### `BlockRenderType getRenderType()`
Returns the rendering model type used by the Block Renderer.

### `BlockSound getSound()`
Returns the sound set used for stepping, placing, and breaking the Block.

### `string getTextureForFace(face, data, x, y, z, world)`
Returns the Texture key or path for a specific Block face.

### `number getTransparency()`
Returns the transparency level of the Block.

### `number handHardnessMultiplier()`
Returns the break speed multiplier applied when breaking without Tools.

### `bool isItem()`
Returns whether the block is treated as a pure Item representation.

### `bool isLava()`
Returns whether the Block behaves as Lava.

### `bool isLiquid()`
Returns whether the Block is a Liquid.

### `bool isReplaceable(world, x, y, z)`
Returns whether this Block can be overwritten when placing another Block at its position.

### `bool isSolid()`
Returns whether the Block is Solid for collision and pathfinding.

### `bool isTranslucent()`
Returns whether Light can pass through this Block.

### `bool isVecInsideXYBounds(point, bbox = null)`
Checks if a vector position falls within the X and Y bounds of the Bounding Box.

### `bool isVecInsideXZBounds(point, bbox = null)`
Checks if a vector position falls within the X and Z bounds of the Bounding Box.

### `bool isVecInsideYZBounds(point, bbox = null)`
Checks if a vector position falls within the Y and Z bounds of the Bounding Box.

### `number|null minimumToolLevel()`
Returns the minimum Tool Tier Level required to drop Items when broken.

### `void onBlockAdded(world, x, y, z)`
Called when the Block is placed or added into the world.

### `void onBlockPlaced(world, x, y, z, face)`
Called when the Player places the block against a specific Block face.

### `bool onMouseButton(world, x, y, z, button)`
Called when a mouse click occurs on the Block.

### `void onUse(world, x, y, z, itemstack)`
Called when a Player right-clicks an Item.

### `MovingObjectPosition raytraceBoundingBox(bbox, x, y, z, start, end)`
Helper method to perform raytracing against a specific Bounding Box relative to world coordinates.

### `Block setHardness(hardness)`
Sets the Block hardness and returns this for chaining.

### `bool shouldRenderFace(world, x, y, z, face)`
Returns whether the specified face should be rendered.

### `static Block|null getById(typeId)`
Retrieves a registered Block instance by its ID.

## Deprecated Methods

!!! warning
    These methods and properties are deprecated; usage isn't recommended.

### `bool isHalf(world, x, y, z)`

Returns whether the block occupies half height (like slabs).

### `bool .noFaceCull`
> **Deprecated**: Use `isTranslucent()` instead.

Tells other blocks to not cull their faces when touching this block.