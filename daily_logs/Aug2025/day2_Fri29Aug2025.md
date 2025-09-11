### **Date: Fri 29 Aug 2025**<br>

# Activities

* 1am - Gave up on making `OpenYear.desktop` run in an independent window. Got somewhat close to the desired effect but that meant that all subsequent nautilus windows also shared that class. It is impossible to "split away" this single window under a different class name.

* 1:20am - Caught a bug in my `CopyToken.desktop`. When launched, token wasn't being copied to my clipboard. When executed directly, it worked fine.

* 1:40am - Apparently since `Terminal` flag was set to `true`, and the `Exec` line was executed directly, the terminal in which the line ran was being closed before `xsel` had the chance to finish execution. Fixed the issue by setting the flag to false and running the command inside a separate independent terminal window.

* 2:10am - Changed the logic of retrieving the most recent daily log in `open_daylog.sh`. Instead of defining the same retrieval method again in another script, I saved the output of `prepare_for_day.sh` into a special file which is then read in one line with `cat`. 

* 5:25am - Sleep.

* 5:40am - Did some brainstorming on why the issue could be occurring. Thought that maybe intersections and phasing through of models would introduce some hidden extra cost in performance - that's only the case if the models aren't fully opaque.

* 1:40pm - Tested and fixed webcam in time for the meeting.

* 2pm - Attended meeting with Charles.

* 6pm - Bogdan informed me he's leaving the projecct for a month. Started downgrading unity

* 8pm - Finished downgrading unity

* 8:05pm - Updated the use of the old input system. Fixed outstanding errors.

* 8:15pm - Back to work on the ticket and looking for the cause of the issue.

* 9pm - Resigned, I imported the wheat models into blender to have a look at them. Found the cause of the performance problems:
  
  ![Screenshot from 2025-08-29 21-00-27.png](/home/snek/Desktop/portfolio/year-2-1/assets/Screenshot%20from%202025-08-29%2021-00-27.png)
  
  each of the "low poly" models had around 8k polygons. That's more than many hyper realistic models used in triple A games. Lacking in skill, I applied decimation and brought that number down to about 200 polygons per model (still very high, but any lower than that the object would become unrecognizable.). This ended the performance issues.

* 11pm - Spent 2 hours trying to export the models into a unity-friendly format.

# Issues/Errors

#### Lag in many concurrent wheat models

The problem is a noticable lag on spawning multiple wheat plants simultaneously.

excerpt from `PlantGrowth.cs`:

```cs
private IEnumerator GrowPlant()
    {
        foreach (GrowthStage stage in stages)
        {
            ReplaceStage(stage.stagePrefab);
            yield return new WaitForSeconds(stage.duration);
        }
    }

    private void ReplaceStage(GameObject newPrefab)
    {
        foreach (GameObject stage in currentStages) { Destroy(stage); }

        for (int i = 0; i < randomNumberOfCrops; i ++)
        {
            Vector3 plantPosition = GetRandomOffsetPosition();
            currentStages.Add(Instantiate(newPrefab, plantPosition, newPrefab.transform.rotation, transform));
        }
    }
```

While the script itself isn't very efficient, and it's definitely responsible for a part of the lag, when the script finishes executing, the lag persists. If this was the cause, it would also only lag once every `stage.duration`, the lag wouldn't be consistent.

##### Tried:

* Removing colliders and interactions -> O.1

* Removing rigidbodies -> O.2

* Using tomato models instead -> O.3

##### O.1, O.2:

    No change whatsoever

##### O.3

    The drop in performance still occurred but was noticably less than with wheat.

<br>

# Next Steps

<br>

## Resources

#### `CopyToken.desktop` v1:

```bash
[Desktop Entry]
Name=CopyToken
Type=Application
Exec=cat /home/snek/Desktop/portfolio/SLToken | xsel --clipboard
Terminal=true
Icon=/home/snek/Pictures/icons/SLToken.png
```

#### `CopyToken.desktop` v2:

```bash
[Desktop Entry]
Name=CopyToken
Type=Application
Exec=/bin/sh -c "cat /home/snek/Desktop/portfolio/SLToken | xsel --clipboard"
Terminal=false
Icon=/home/snek/Pictures/icons/SLToken.png
```
