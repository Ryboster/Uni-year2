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

8:25am - Let my team know about having to rewrite the IInstrument interface. Got a discussion started.

8:45am - Got greenlit. Full steam ahead!

8:55am - Fixed all the errors and got the project to compile. 



10am - With the classes now written, I need to better define the purchasing workflow. It's a little bit tricky because ideally I'd handle the purchasing in the shop and not the item, however, that's impossible as it's the Item that handles the OnClick event.

10:45am - Food break.



11:10am - Marta gave me some feedback on the progress thus far. Will have to: remake the shop a little bit as we don't need two categories, add a popup window so the player can 

11:30am - Have to redesign the shop UI.

11:40am - Rebuilt the ShopItem prefab. Made it a horizontal list item instead of the "cell" it used to be.

11:55am - Rebuilt the Shop. Added a side panel to display more information about the selected item before it is purchased. Inspired by the following UI design: https://www.gameuidatabase.com/uploads/Astral-Chain03132021-122126-84561.jpg



12pm - Attended the ASD meeting,

12:30pm - Learned about what telemetry is from Heckie. It's basically when applications gather user data and send it back over to the developers. This is then used to extract valuable insights about the customer and application usage trends. 

<br>

# Issues/Errors

8:05am - Unity doesn't serialize interfaces. Fudge! In order to serialize this I'm going to have to create a new MonoBehaviour class that subscribes to that interface. 

8:07am - Nevermind, Marta's done that already. We're good!

8:08am - Nevermind again, those classes aren't MonoBehaviour so I can't serialize them. I'm going to have to rewrite `interface IInstrument` into a `abstract class Instrument : Monobehaviour` for this to work.



9:24am - Shop and ShopItems are thus far disconnected. This is a problem as the Shop has something the ShopItems need - Player score. I need to somehow make the shop aware of the items it has. 

9:40am - Solved the problem. Instead of placing the items inside the Shop prefab manually, I created a Shop script that defines the field `GameObject[] instrumentsToSell;`. Then, I simply instantiate the items in that list and set their parents to the appropriate content list.



<br>

# Next Steps

<br>

## Resources

<br>
