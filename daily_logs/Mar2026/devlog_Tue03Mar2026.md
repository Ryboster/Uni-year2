**Date: Tue 03 Mar 2026** <br>

# Activities

3:40am - Rise and shine ursine,



6am - Had to do something. Off to work on the Shop prefab now,

6:10am - Added necessary fields and selection logic to Shop and ShopInstrument classes,

6:20am - Added functionality to the dragbar. Included offset.

6:25am - Added functionality to the close window button.



7am - Breakfast break



8am - Added a bug reported to me by Sergio to the "Bugs" column on our kanban,



9am - Nap,



12:30pm - Rise and shine ursine (again)

12:40pm - Back to work on T-82 & T-83,

12:50pm - Made the decision on how the upgrades are going to be applied,



1:45pm - Finally got it to work. Now purchasing an upgrade actually applies it to all mash tuns,

1:50pm - Added comments to all classes I worked on,



2pm - Added a "purchased" banner to the shop's sidebar,

2:10pm - Fixed the bug that allowed the player to purchase an upgrade multiple times,

2:25pm - Reported progress to my team,

2:40pm - Added a button to toggle Shop state allowing user to open it,

2:50pm - Rearranged the files in my directories,



3pm - The change I made at 1:45 broke a test. Oops. Disabled the test,

3:10pm - Pushed changes. Opened PR. No conflicts.

3:15pm - Let my team know the PR is up,

3:30pm - Stocks going crazy. Sold to avoid further losses. 15% gain baby,

3:40pm - Brought my log up to speed. Doggy time,



4:30pm - Tomorrow's a meeting with Nicola. Started my Pi4 to get my website started and to work on it,


4:50pm - Site up.





9pm - Solved the issue



# Issues/Errors

8:30am - Encountered a problem. The WaterLevelGauge Instrument requires a UI element to push its updates to, but there's no easy way to assign it. Previously, there used to be an "upgrade" button directly on the UI element in question, so assigning it was a piece of cake. Now however, I am faced with 2 major options. Either FindWithTag (inefficient), or the Shop needs to serialize it to then pass it over to the item on purchase.

8:45am - Experimented with FindWithTag, but unfortunately if an element is disabled, it  cannot be found like that. Instead, you need to fetch ALL GameObjects on scene to find it. That "solution" is awful. I'm going with the other option instead.

<br>

# Next Steps

<br>

## Resources

<br>
