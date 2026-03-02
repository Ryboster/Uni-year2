**Date: Mon 02 Mar 2026** <br>

# Activities

1am - Fixed my DEVLOG_CREATOR.sh script for automatically creating daily logs,

1:30am - Started working on my UNI_REPO_UPDATER.sh script for automatic repo updates,

2:20am - Finished my UNI_REPO_UPDATER.sh script,

2:25am - Break,

3am - Created a special environment for cron to store its variables,

3:30am - Tidied my scripts,

5am - Wrote a desktop application for opening the most recent log,

5:10am - With my applications done, I got to work on T-83.

5:30am - Gas station break and breakfast,

6:30am - Got to work on T-83.

6:40am - Resolved conflicts with scene,

6:45am - Investigated how upgrades are applied to mash tuns.

6:50am - There is an `AddInstrument(IInstrument instrument)` method. Excellent. Now I need to create a `ShopItem` prefab with this interface, and call the method from UI,

7:10am - Built the prefabs for the two available instruments. Designing the behaviour right now,



7:40am - Doggy time,

7:50am - Ok, this interaction is more complex than anticipated. I can't just design in in my head; insufficient mental RAM. I'm going to have to make a UML just to chart the way forward. The problem is that in order for the UI to be able to apply bought items to the Mash Tuns, my Shop is going to have to be aware of all of the Mash Tuns on scene. So far, I only know of one way to do this, which is `GameObject.FindGameObjectsWithTag("tag")`.  This is a problem because it's very inefficient, and there are already 2 other scripts doing just that - luckily only at startup.  If I don't find a better solution, I'm going to have to settle for this, and then we can improve the performance in the future by creating some sort of a central singleton class that is going to keep an updated array of all Mash Tuns on scene, accessible by other classes who need it.



8am - Ok, there really doesn't seem to be a cleaner way to do it. I settled for `FindWithTag()`. The impact on the performance is still minimal so it's not that bad of an idea. It will become problematic later, but that's a problem for future me. I created a new prefab; ShopInstrument. It is going to be used to definte purchasable instruments.



<br>

# Issues/Errors

8:05am - Unity doesn't serialize interfaces. Fudge! In order to serialize this I'm going to have to create a new MonoBehaviour class that subscribes to that interface. 

8:07am - Nevermind, Marta's done that already. We're good!

<br>

# Next Steps

<br>

## Resources

<br>
