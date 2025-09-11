**Date: Sat 30 Aug 2025**<br>

# Activities

* 1am - Continued adjusting the prefabs, their scales, colliders, and behaviour scripts. 

* 5am - Sleep

* 4pm - Took T-306: Allow Player to gather wheat.

* 5pm - Added instantiation of the equivalent item in plants' `OnDestroy`.

* 5:20pm - Got screamed at by the editor. It's a bad practice. Thought about the next logical place to put that behaviour.

* 6:20pm - Started rewriting WheatLive. Now, instead of having one GameObject directly managing a group of plants, each plant will be their own boss. It will only have knowledge of itself and the next plant in chain and whether they're the final stage/evolution. 

* 7pm - Finished rewriting the core of the script.

* 8pm - Still kept getting silly small errors. Revised the hoe script.

* 9pm - Simplified the whole script vastly. Corrected inconsistencies in applications of positions and rotations. Readjusted height offset. Updated collision matrix and corrected layer filtering. No more rotating or moving random objects in preview. No more logic blocking placement on collision with ground. Now the preview has gravity and can receive the perfect rotation directly with gravity and collision. When placed, the placed object is kinematic so no more problems with colliders phasing through each other either.

* 10pm - Simplified the logic and construction of the preview as well. Instead of keeping a recipe for the creation of a translucent material directly in code, i created the material to clear up the space - code is for people.  Linked up the new material. Vastly simplified the logic to basically just: Check if can place -> Change color to red/green. Also added an extra collider for preventing other fields being placed too close to each other.

<br>

# Issues/Errors

* Because of the fact that we have one GameObject; `WheatLive` that directly manages a group of plants while plants have not the faintest knowledge of being managed or of the fact that they're currently growing, defining the "conversion to item" behaviour necessitates creating a new script. This is a bad practice however as this step would need to be repeated for every subsequent plant.
  
  SOLUTION: Rewrite of `WheatLive`

* The unity's `Camera.main.ScreenToWorldPoint(Mouse.current.position.ReadValue()` method of translating cursor's 2d position to world coordinates has a fatal flaw. Since the camera is most often under an angle to the ground, the accuracy of which point you're aiming for and which point your ray actually intersects with, decreases over distance, and fast. I went over an idea involving "satelites" - cameras high above the ground perfectly perpendicular to it, but quickly rejected it due to impracticality and the fact that it wouldn't solve the problem anyway. Opted for simply limiting the placement range to 7f.

<br>

# Next Steps

<br>

## Resources

#### new refreshed version of PlantGrowth

```csharp
private void Start()
    {   
        isWatered = transform.parent.GetComponent<SoilBehaviour>().isWatered;
        transform.localScale = new Vector3(10f, 10f, 10f);
        duration = isWatered? duration - Mathf.Max(duration / 5, 1) : duration; // if isWatered, decrease duration by 20%
        StartCoroutine(Grow());
    }

    public IEnumerator Grow()
    {
        yield return new WaitForSeconds(duration);
        Evolve();
    }

    public void Evolve()
    {
        if (isFinalStage) { isRipe = true; return;}
        var newStage = Instantiate(nextStage, transform.position, Quaternion.identity, transform.parent);

        Destroy(transform.gameObject);
    }
```

[Unity - Manual: Make a material transparent](https://docs.unity3d.com/Manual/StandardShaderTransparency.html)

<br>
