**Date: Wed 15 Sep 2025**<br>

# Activities

<12am - Over the weekend I explored other ways of solving my navigational problem ([day 7 - Issues/Errors Section](day7_Fri12Sep2025.md)) including  periodically spawning in a giant `SphereCollider` to get a list of each unique `GameObject` that the NPC can "see". This would be WAY more efficient but I'm still not 100% happy with this solution.

1am - Started working on a new controller component "`UniversalMovementController`" that would handle movement for all in-game entities.

1:20am - Started by sketching up a workflow diagram and assigning specific responsibilities to different entities (Entities in red). Then sketched up another diagram for the new responsibility I wanted to introduce - Applying terrain modifier to movement speed. 

![newMovementControllerFlowChart1.jpg](../assets/newMovementControllerFlowChart1.jpg)

2am - Explored different ways of detection of that slope. Discussed it with Bogdan. 

![newMovementControllerFlowChart2.jpg](../assets/newMovementControllerFlowChart2.jpg)



5am - Went ahead with 2-point precision and implemented it.

![image.png](../assets/a3a9980d810f218041512e703bd5e8434d994fc4.png)<img title="" src="../assets/9e2fa03da3bd03cebaac78a67357dbecaaf092fa.png" alt="image1.png" data-align="left">



6am - Extrapolated the difference between center and forward with 4 test different test cases and devised a simple conversion formula to convert the difference in distance to angle.

![20250915_051440.jpg](../assets/a14fffa51f4a4e6c38d51f1ad421fa77aa3ab255.jpg)







9pm - Discussed different methods of giving NPCs eyesight in our Unity project with Bogdan.

<br>

# Issues/Errors

<br>

# Next Steps

<br>

## Resources
