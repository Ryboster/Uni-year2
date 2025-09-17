**Date: Wed 17 Sep 2025**<br>

# Activities

12am - Deployed the new `Agent` ([day 9](day9_Tue16Sep2025.md)). Immediately encountered an old error.



1am - Thought of a strong opening to a song. Went songwriting.

4am - Wrote a song. Composed a melody for it.

5am -

7:30pm - Moved all whiteboard images to my PC
7:50pm - Sketched up a quick tidy ERD of the new movement controller.
8pm - Fixed my crontab (finally)

8:10pm - Carried on catching up with daily logs. It was a busy week working on SL and so prioritizing SL, I neglected my daily logs.

9pm - Found a problem with the way MarkText interprets dragged-and-dropped images. Instead of the `markdown` syntax (`![alt text](src "name")`), it kept pasting it in `HTML` syntax (`<img src="path" ...>`).

9:25pm - Found a solution to the problem. It's only converted to HTML if you resize the picture because markdown doesn't have an equivalent to `height` and `width` attributes of an `img` tag.

<br>

# Issues/Errors

12am - Upon deployment, NPCs almost immediately fall through the `TerrainCollider`. They aren't even going at super fast speeds or anything, they simply phase through in some places like my terrain was a cheese grater.

Tried resolving this by:

* Setting NPCs' `Rigidbody.CollisionDetection` to `Continuous Dynamic` and `Continuous Speculative`. Failed.

*  Decreasing/Increasing their `Rigidbody.Mass`. Failed.

* Setting their `Rigidbody.Interpolate` to `Interpolate`. Failed.

* Removing the `Rigidbody.useGravity` toggles from my `UniversalMovementController`. Failed.

* Repositioning my NPCs' `CapsuleCollider` slightly. Failed.

<br>

# Next Steps

<br>

## Resources

[Objects Falling Through Terrain - #10 by Greenwater79 - Unity Engine - Unity Discussions](https://discussions.unity.com/t/objects-falling-through-terrain/738551/10)

[Objects Falling Through Terrain - #8 by arfish - Unity Engine - Unity Discussions](https://discussions.unity.com/t/objects-falling-through-terrain/738551/8)

[Objects Falling Through Terrain - #7 by JoeStrout - Unity Engine - Unity Discussions](https://discussions.unity.com/t/objects-falling-through-terrain/738551/7)

[How to stop falling through floors and colliders in Unity &#8211; John Stejskal : Software and Game Developer](https://johnstejskal.com/wp/how-to-stop-falling-through-floors-in-unity/)



<br>
