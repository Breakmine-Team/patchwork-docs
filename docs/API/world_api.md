# World
Minimum Patchwork: [|octicons-history-24||v1.1.0|]

??? info "Under Development"

    Both Patchwork and its documentation are currently under active development.
    
    As new updates are introduced to Patchwork, these pages will be updated to match. Please expect occasional issues, incomplete sections, or temporary inconsistencies as the software and reference materials evolve alongside each other.

## Constructor

### `constructor(minecraft)`
Creates a new World instance. Note that you are recommended to use the global `minecraft.world` if a method isn't given a `world` property.

---

## Methods

### `void addEntity(entity)`
Adds an Entity to the World, assigns an ID if needed, and initializes its renderer.

### `bool blockExists(x, y, z)`
Checks whether a block coordinate is within valid World height bounds and in a loaded Chunk.

### `number calculateSkylightSubtracted(partialTicks)`
Calculates the reduction in skylight brightness based on time of day.

### `bool chunkExists(chunkX, chunkZ)`
Returns whether a Chunk exists at the given chunk coordinates.

### `void clearChunks()`
Clears all Chunks via the ChunkProvider.

### `void clearEntities()`
Removes all Entity instances currently active in the World.

### `void cleanup()`
Cleans up World timers and resources like light update intervals.

### `number getBlockAt(x, y, z)`
Returns the numerical ID of the Block at the specified position.

### `number getBlockAtFace(x, y, z, face)`
Returns the ID of the Block adjacent to the given position on the specified face offset.

### `Array<BoundingBox> getBlockCollisionBoxesAt(x, y, z)`
Gets a list of BoundingBox instances contributing to solid physics collision at a specific block coordinate.

### `number getBlockDataAt(x, y, z)`
Returns the metadata value associated with the Block at the given coordinate.

### `number getCelestialAngle(partialTicks)`
Calculates the current celestial rotation (sun/moon position) for rendering and light levels.

### `Chunk|null getChunkAt(x, z)`
Gets the Chunk instance at the specified chunk grid coordinates.

### `ChunkSection|null getChunkAtBlock(x, y, z)`
Gets the specific 16x16x16 ChunkSection at world block coordinates.

### `ChunkProvider getChunkProvider()`
Returns the current ChunkProvider attached to the World.

### `ChunkSection|null getChunkSectionAt(chunkX, layerY, chunkZ)`
Returns the ChunkSection at specific chunk coordinates and Y-layer index.

### `Array<BoundingBox> getCollisionBoxes(region)`
Gets all colliding BoundingBox instances from solid blocks overlapping with the specified bounding box region.

### `Entity|null getEntityById(id)`
Retrieves an active Entity by its unique ID.

### `Vector3 getFogColor(partialTicks)`
Calculates the current fog color based on the time of day and celestial angle.

### `number getHeightAt(x, z)`
Gets the world height position of the first non-solid Block at the specified X/Z column.

### `number getHighestBlockAt(x, z)`
Gets the Y position of the highest solid Block at the given X/Z coordinate.

### `number getHumidity(x, y, z)`
Returns the climate humidity value for the specified world location.

### `number getLightBrightness(x, y, z)`
Gets normalized brightness level (`0.1` to `1.0`) at the specified block coordinate.

### `number getLightBrightnessForEntity(entity)`
Gets normalized brightness level (`0.1` to `1.0`) at an Entity's current position.

### `number getSavedLightValue(sourceType, x, y, z)`
Gets raw saved light level (`0`–`15`) for a specific light source type (`EnumSkyBlock.SKY` or `EnumSkyBlock.BLOCK`).

### `number getSeed()`
Returns the seed value for world generation.

### `Vector3 getSkyColor(x, z, partialTicks)`
Calculates the overall RGB sky color based on time of day and temperature.

### `Vector3 getSkyColorByTemp(temperature)`
Translates a temperature value into an RGB sky color tint.

### `Vector3 getSpawn()`
Returns the world spawn position as a Vector3.

### `number getStarBrightness(partialTicks)`
Gets the current star visibility brightness for night rendering.

### `Vector4|null getSunriseSunsetColor(partialTicks)`
Calculates RGBA color factors for the horizon during sunrise or sunset.

### `number getTemperature(x, y, z)`
Returns the climate temperature at the specified world location.

### `number getTotalLightAt(x, y, z)`
Gets the combined total light level reaching a specific block position.

### `bool isAboveGround(x, y, z)`
Checks whether the specified position is strictly above the highest solid Block in the column.

### `bool isHalfBlockAt(x, y, z)`
Checks whether the Block at the specified coordinate is a half-height block.

### `bool isHighestBlock(x, y, z)`
Checks whether a block position is at or above the highest solid Block in its column.

### `bool isSolidBlockAt(x, y, z)`
Checks whether the Block at the specified position is solid and non-multipart.

### `bool isTranslucentBlockAt(x, y, z)`
Checks whether light can pass through the Block at the specified coordinate.

### `void loadSpawnChunks()`
Pre-loads Chunks surrounding the world spawn point based on view distance settings.

### `void neighborLightPropagationChanged(sourceType, x, y, z, level)`
Notifies light engine when neighbor light sources or opacity state updates.

### `void onBlockChanged(x, y, z)`
Triggers modified chunk flags to re-render nearby blocks when a change occurs.

### `void onTick()`
Runs the main world update tick including entity updates, scheduled block ticks, tile entities, daylight recalculations, and time passage.

### `void processBlockTicks()`
Processes and executes queued block tick events up to the current world time (singleplayer only).

### `MovingObjectPosition|number|null rayTraceBlocks(from, to, slab = false)`
Traces a ray between two positions against block collision bounding boxes in the world.

### `void removeEntityById(id)`
Removes an Entity from the World and disposes of associated render elements (meshes, nametags, shadows).

### `void scheduleBlockTick(x, y, z, delay)`
Schedules a block tick callback at a position after a specified number of world tick delays.

### `void scheduleNeighborTicks(x, y, z)`
Schedules block ticks for six adjacent neighbor coordinates.

### `void setBlockAt(x, y, z, type, data = 0)`
Sets the block ID and metadata at a location, triggering placement, removal, tick updates, and chunk re-renders.

### `void setBlockDataAt(x, y, z, data)`
Sets only the metadata state of a Block at a position without changing its ID.

### `void setChunkProvider(chunkProvider)`
Assigns the world's ChunkProvider.

### `void setLightAt(sourceType, x, y, z, lightLevel)`
Sets light values directly for sky or block light channels and marks the chunk to rebuild.

### `void setModified(minX, minY, minZ, maxX, maxY, maxZ)`
Marks affected chunk sections as modified so they can be re-rendered.

### `void setSpawn(x, z)`
Updates the world's spawn position to the top ground layer at `(x, z)`.

### `void tickBlock(x, y, z)`
Triggers the `onBlockTick` handler for a block at the given position.

### `bool updateLights()`
Processes pending light updates queued in `lightUpdateQueue`.

### `void updateLight(sourceType, x1, y1, z1, x2, y2, z2, notifyNeighbor = true)`
Queues a light recalculation task across a 3D bounding region.