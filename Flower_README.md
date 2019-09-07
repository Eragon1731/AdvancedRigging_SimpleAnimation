# Flower Animations

advanced_rigging is a module that contains a tool to build a simple flower and animate it with python scripts. The module will also contain different ways to edit the flower's form and animation.

## Installation

To import module, run in the Maya Script Editor:

import advanced_rigging
import advanced_rigging.MainWindow

advanced_rigging.MainWindow.main()

## Usage
```

Load Assets:

1. "Bulb Name" and "Petal Name": Enter the names of your bulb and petal files in the text areas below
2. Click "Load" to load your files

Build Flower:

1. "Name the flower": Give your flower a name. Make sure the name is at least one letter long. This will be used as a reference to a specific flower. 
2. "Petal Name" and "Bulb Locator Name": The petal name should be a group containing the skinned model and the joints for the petal you want to use. This will allow the tool to rig your petal for the animations. The bulb name should be the name of the locator attached to your bulb asset. This will ensure that the petals form around the local center of you bulb. If you change the names of the petal and bulb assets, enter appropriate the names as such:

Petal Model Name:  <petal>
Bulb Locator Name:  <bulb>_loc 
  
3. "Assign Petal Rows": Select the number petal rows you want in the flower. The default number is 3. This means that there will be 3 layers of petals forming from the center of the flower. 
4. "Assign Base Petals": This the amount of petals in the inner most layer of the flower. Each layer of petals after will be 1 more than the previous one. For example, if the number of base petals in the inner most layer is 3, than the next layer will have 4 petals, and the next 5, and so on. Indicate the number of petals you want in this layer. 
5. Click "Create the Flower" to create the flower 

Animate the Flower: 

Variables:
1. "Name of the flower to animate/edit": Use the name you gave earlier when you created it to animate or clear all keyframes on. 
2. "Animation Time Length": The total amount of frames the animation should run for. Use this to determine the maximum amount of frames the animation will run for. The default amount is 120 frames.  
3. "Keyframe frequency within Time Limit": For every xx amount of frames, when you want to keyframe. For example, if 5 is entered, then every 5 frames will have a keyframe. Use this to control the flow of your flower blooming animation.
4. "Which axis to animate on": On which axis should the petals rotate on. If "X" is chosen, then the joints will rotate on the X axis. Choose "Z" for a default blooming animation with the default petal and bulb provided. 
5. "Speed of Animation": How quickly the you want the petals to bend during the animation. For example, if 1 is selected, than the petal will bend an extra 1 degrees at the next keyframe (i.e. 0 to 1 to 2 etc.). If 5 is selected, than the petal will bend an extra 5 degrees at the next keyframe (i.e. 0 to 5 to 10 etc.). Use this variable to determine how quickly you want the petals to bend and spin. 
6. "Which row num you want to spin": the petal rows are ordered from 0 to n-1, from inner-most to outer-most, with n being the number of petal rows you previously indicated. For example, if you entered 3 rows for the flower, the petal layers will be ordered as 0,1,2 from inner-most to outer-most. Use this category to indicate which layer you want to spin around the flower. For example, if you want the inner-most layer, enter 0. This variable is only for the Spinning Animation. 

Buttons:
** For this animation, you MUST enter an EXISTING flower name ** 
1. Click "Animate Blooming" to create the flower blooming animation. This animation will make all petals gradually rotate in uniform. This animation can stack up. For example, if on the first click you animation the petals on the X axis, you can change the axis variable to "Y" to add the animation on the Y axis as well. 

** For this animation, you MUST enter an EXISTING flower name AND an EXISTING row number in the named flower ** 
2. Click "Animate Petals Spin" to create the spinning animations. This will only make ONE row of the flowers spin around the bulb according to the variables above.  

** For this action, you MUST enter an EXISTING flower name. It may not affect keyframes created outside tool ** 
2. Click "Clear Keyframes" to clear keyframes. This action will clear ALL keyframes created with the tool

```
## Important Notes:
1.  If you are using your own models, make sure the joints in the petal contains: "petal_joint". Otherwise, the tool will not create controllers for petals. 
    The following are all valid naming styles. For Example:

    petal_joint_<something>
    <something>_petal_joint_<something>
    <something>_petal_joint

2. If you creating your own bulb locator, make sure to zero out transforms in locator. Otherwise tool will
    organise petals randomly.
3. Tool will not work properly if assets are deleted from scene. 
4. Tool will not remember the assigned flower names if Scene or tool is restarted. Make sure not to close tool while using it.
5. Use Tool in order of tabs from Loading, Building, and Animating. Using Tool out of order will not work.

## In Progress
Have to test the flower animation tool on other types of assets and see if the tool still works if the User renames assets. Also have not cleaned or commented code for this tool yet.
