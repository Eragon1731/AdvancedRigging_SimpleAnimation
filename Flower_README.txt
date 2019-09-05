# Flower Animations

advanced_rigging is a module that contains pipelines to build a simple flower and animate it with python scripts. The module will also contain different ways to edit the flower's form and animation.

## Installation

To import module, run in the Maya Script Editor:

import advanced_rigging
import advanced_rigging.MainWindow

advanced_rigging.MainWindow.main()

## Usage
```python

Load Assets:

1. "Bulb Name" and "Petal Name": Enter the names of your bulb and petal files in the text areas below
2. Click Load to load your files

Build Flower Attributes:
1. "Name the flower": Give your flower a name. Make sure the name is at least one letter or number long. This will be used as a reference to a specific flower. 
2. "Petal Anim Model Name" and "Bulb Center locator Name": The petal name should be the root parent of the petal you want to use. The bulb name should be the name of the locator attached to your bulb asset. This will ensure that the petals form around the local center of you bulb. If you change the names of the petal and bulb assets, enter appropriate the names as such:

Petal Anim Model Name:  <petal>
Bulb Center locator Name:  <bulb>_loc 
  
3. "Assign Petal Rows": Select the number petal rows you want in the flower. 
4. "Assign Base Petals": Base petals stand for the petals in the inner most layer of the flower. Indicate the number of flowers you want in this layer. 
5. Click "Ok" to create the flower 

Animate the Flower:
** Be sure to select the controller group(s) you want to animate in this section. **
1. "Animation Time Length": The total amount of time the animation should run for. Use this to control how the flower blooms and how the petals should spin around the bulb. 
2. "Keyframe frequency within Time Limit": For every xx amount of seconds, when you want to keyframe. For example, if 5 is entered, then every 5 seconds will have a keyframe. Use this to control the flow of your flower blooming animation. Change or use this to affect how you want to keyframe the petals spinning around the bulb. 
3. "Which axis to animate on": On which axis should the petals rotate on. Choose "Z" for a default blooming animation
4. "Speed of Animation": How quickly the you want the petals to bend during the animation. Change or use this variable to determine how quickly you want the petals to spin around the bulb. 
5. Click "Animate the Flower Blooming" to create the flower blooming animation

1. "Name of the flower to clear keyframes on": Use the name you gave earlier when you created it to clear all keyframes on all assets on one specific flower.
2. Click "Clear Keyframes" to clear keyframes

1. "Which row num you want to spin": the petal rows are ordered from 0 to n-1, from inner-most to outer-most, with n being the number of petal rows you previously indicated. For example, if you entered 3 rows for the flower, the petal layers will be ordered as 0,1,2 from inner-most to outer-most. Use this category to indicate which layer you want to spin around the flower. 
For example, if you want the inner-most layer, enter 0. 
2. "Name of flower to spin": Enter the name of the flower you want to animate the spinning animation on. The name will be the one you previously entered to create the flower. 
3. Click "Spin the Flower" to create the spinning animations. 

```

## In Progress
Have to test the flower animation tool on other types of assets and see if the tool still works if the User renames assets. Also have not cleaned or commented code for this tool yet. A lot of the UI names and layout designs are still work in progress. If everything listed above is finished, I might consider adding a relocation function so the User can move the flower via one locator. 
```


