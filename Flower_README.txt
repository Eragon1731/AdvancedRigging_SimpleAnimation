# Flower Animations

advanced_rigging is a module that contains pipelines to build a simple flower and animate it with python scripts. The module will also contain different ways to edit the flower's form and animation.

## Installation

To import module, run:

```bash
import advanced_rigging
```

## Usage
```python

import maya.cmds as mc
import advanced_rigging
import advanced_rigging.main

#Step One: Load flower parts
advanced_rigging.main.StepOne(bulb="lotus_bulb", petal="lotus_petal")
#Step Two: Make rig
lotus = advanced_rigging.main.StepTwo(petal_name="lotus_petal", bulb_name="lotus_bulb", petal_rows=3, base_petals=3)
#Step Three: Make animation
advanced_rigging.main.StepThree()


```

## In Progress
Still building functions to edit flower structure or adjust flower animations after all three steps have been run. 
```
#Testing edits to flower
advanced_rigging.main.adjustPetals(flower=lotus, func="adjustPetalRowTransform")```

