**Date: Sun 31 Aug 2025**<br>

# Activities

* 1am - Added seeds and assigned the prefab of the first stage of growth to them. Now when they're "planted" (instantiated), the seed is no longer needed. The seed is only a startup.

* 1:30am - Added watering functionality. Soil can be watered now.

* 2am - Ran into a relationship issue. Soil is unaware of plant and vice versa. Soil cannot be aware of plant because plant only exists for `duration` before dying and being replaced by another stage, so plant must know of soil. This is needed for watering logic.

* 2:30am - Added a flag preventing multiple uses of seeds on one farm spot.

* 3am - Trying to solve the previous problem i ran into another one. I mistakingly kept using the wrong version of the same file and kept going in circles wondering why I wasn't able to assign plants as children of soil. Done now.

* 3:10am - Ran into an issue of scale. Having made plants the children of soil, their scale setting is now meaningless.

* 4am - Spent another hour in blender trying to figure out how to export it properly.

* 4:20am - Unified scale on all stages. Now plants know when they're watered which reduces each watered stage's duration. Once all plants have been harvested, the soil returns back to its dry state, and the `isOccupied` flag is set back to `false` allowing further cultivation. 

* 5:05am - Posted the PR. Went back over my changes and listed them all in the PR for the reviewer.

* 6am - Caught up with the last 2 days of daily logs.

* 6:10am - Looked at our kanban. Picked the next 2 tickets to complete.

* 6:30am - sleep.

* 5pm - Took another ticket; T-358 - Improve animations.

* 5:05pm - Looked for free scythe animations

<br>

# Issues/Errors

<br>

# Next Steps

* T-358: Improve animations - To allow player to gather wheat properly.

* Beg Bogdan to review PR's.

* T-347: Update tutorial for item creation.

* Research how to actually start with the AI.

* Review high-level docs.

<br>

## Resources

<br>
