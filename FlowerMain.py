import ImportFlower
reload(ImportFlower)
import FlowerAnimation
reload(FlowerAnimation)
from Flower import Flower
import os
import maya.cmds as mc

FLOWER_INSTANCES = {}

""" 
Step 1: Load the models. Function also provides error checking for loading 
"""


def StepOne(bulb, petal):

    # Given that the bulb and petal names are not null. Else ask User to enter names.
    if (bulb is not None) and (petal is not None):

        # find the relative paths to the models and load them
        current_dir = os.path.dirname(__file__)
        bulb_path = os.path.join(current_dir, "Assets", bulb + ".fbx")
        petal_path = os.path.join(current_dir, "Assets", petal + ".fbx")

        # Check if BOTH paths to bulb and petal exist. Else use a default path for either one missing
        if os.path.exists(bulb_path) is False:
            mc.warning("cannot find bulb file: ", bulb, "Using default:\n lotus_bulb")
            bulb = "lotus_bulb"
            bulb_path = os.path.join(current_dir, "Assets", bulb + ".fbx")

        if os.path.exists(petal_path) is False:
            mc.warning("cannot find petal file: ", petal, "Using default:\n lotus_petal")
            petal = "lotus_petal"
            petal_path = os.path.join(current_dir, "Assets", petal + ".fbx")

        # if both paths to bulb and petal exist, load them
        ImportFlower.createBulb(bulb_path)
        ImportFlower.createPetal(petal_path)
    else:
        mc.warning("Bulb and Petal names are not defined")

    # Tell User action is done
    print "Finished loading Bulb:", bulb, " and Petal: ", petal


""" 
Step 2: Move Petals in place. Specify name of the parent petal joint, petal geo name, and bulb locator name in this order. 
Function also provides error checking for loading 
"""


def StepTwo(name, petal_name, bulb_name, petal_rows=1, base_petals=3):

    # Check if the parameters are valid. Check that: Name is not empty, petal AND bulb exist in scene.
    if not name:
        mc.warning("Name for Flower is empty! Enter a name")
    elif len(mc.ls(petal_name)) == 0:
        mc.warning("Cannot find Petal! Make sure name is entered correctly")
    elif len(mc.ls(bulb_name)) == 0:
        mc.warning("Cannot find Bulb Locator! Make sure name is entered correctly")
    else:

        # create an Flower instance so each flower as a unique set attributes
        lotus_flower = Flower(name=name, petal=petal_name, bulb=bulb_name, rows=petal_rows, base_petals=base_petals)

        # build the flower using the traits assigned to instance
        lotus_flower.organiseFlowerPetals()
        lotus_flower.movePetalsAroundBulb(offset=1)

        # Group all controllers together
        lotus_flower.groupAllComponents()

        # Track all Flower instances created
        FLOWER_INSTANCES.update({name: lotus_flower})

        # Tell User action is done
        print "Finished creating flower: ", name


""" 
Step 3: Rig and Animation petal joints in Flower. Select the petal groups to animate
Function also provides error checking for loading 
"""


def StepThree(name, frequency, time, axis, init_bend, speed):

    # Check that: Name is not empty. If it is, throw a warning for User
    if not name:
        mc.warning("Enter Name of Flower you want to animate!")
    else:

        # Get flower with its name
        flower = FLOWER_INSTANCES.get(name)

        # Check that the flower exists in dictionary. If it doesn't, use the first flower in dictionary.
        if flower is None:
            mc.warning("Enter Name of existing Flower! Using a default flower")
            flower = FLOWER_INSTANCES.get(FLOWER_INSTANCES.keys()[0])

        # Animate Flower
        FlowerAnimation.animatePetals(flower=flower, frequency=frequency, time=time,
                                      axis=axis, curr_bend=init_bend, bend_speed=speed)
        # Tell User action is done
        print "Finished Animating Flower Blooming for: ", name


""" 
Clear Keyframes for Flower: Clears all keyframes in Flower controllers. 
Function also provides error checking for loading 
"""


def clearKeyFramesForFlower(name, time=120):

    # Check that the name entered is valid. Otherwise, tell User
    if not name:
        mc.warning("Enter Name of Flower you want to clear keyframes for!")
    else:

        flower = FLOWER_INSTANCES.get(name)

        # Check if the flower exists in dictionary. Else use the first flower in dictionary
        if flower is None:
            mc.warning("Enter Name of existing Flower! Using a default flower")
            flower = FLOWER_INSTANCES.get(FLOWER_INSTANCES.keys()[0])

        # Clear all keyframes
        FlowerAnimation.clearAllKeyFrames(flower, max_time=time)

        # Tell User action is done
        print "Finished clearing all keyframes for flower: ", name


"""
Spin ONE specific row of petals around the bulb 
"""


def spinFlowerForFlower(name, numRows):

    # Check if the name is valid AND if the Row Number indicated exists. If not, tell the User
    if not name:
        mc.warning("Enter Name of Flower you want to animate")
    elif not numRows:
        mc.warning("Row number not entered! Which row of petals do you want to spin?")
    else:
        flower = FLOWER_INSTANCES.get(name)

        # Check if the flower exists in dictionary. Otherwise use the first flower in dictionary
        if flower is None:
            mc.warning("Enter Name of existing Flower! Using a default flower")
            flower = FLOWER_INSTANCES.get(FLOWER_INSTANCES.keys()[0])

        # if cannot find the row number for an existing flower, tell the User to enter a Correct row number.
        status = FlowerAnimation.spinRowAnimation(flower, row_num=numRows)

        if status:
            print "Finished animating Spin for flower: ", name, " at row: no. ", numRows
        else:
            print "Wrong Row Number! Enter a correct one"
