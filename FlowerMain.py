import ImportFlower
reload(ImportFlower)
import FlowerAnimation
reload(FlowerAnimation)
from Flower import Flower
import os
import maya.cmds as mc

FLOWER_INSTANCES = {}

# Step 1: Load the models
def StepOne(bulb, petal):

    if (bulb is not None) and (petal is not None):
        """find the relative paths to the models and load them"""
        current_dir = os.path.dirname(__file__)
        bulb_path = os.path.join(current_dir, "Assets", bulb + ".fbx")
        petal_path = os.path.join(current_dir, "Assets", petal + ".fbx")

        if os.path.exists(bulb_path) is False:
            mc.warning("cannot find bulb file: ", bulb, "Using default:\n lotus_bulb")
            bulb_path = os.path.join(current_dir, "Assets", "lotus_bulb.fbx")
            bulb = "lotus_bulb"
        if os.path.exists(petal_path) is False:
            mc.warning("cannot find petal file: ", petal, "Using default:\n lotus_petal")
            petal_path = os.path.join(current_dir, "Assets", "lotus_petal.fbx")
            petal = "lotus_petal"

        """load the models found"""
        ImportFlower.createBulb(bulb_path)
        ImportFlower.createPetal(petal_path)
    else:
        mc.warning("Bulb and Petal names are not defined")

    print "Finished loading Bulb:", bulb, " and Petal: ", petal


# Step 2: Move Petals in place. Specify name of the parent petal joint, petal geo name, and bulb locator name in this order
def StepTwo(name, petal_name, bulb_name, petal_rows=1, base_petals=3):

    if not name:
        mc.warning("Name for Flower is empty! Enter a name")
    else:
        """create an Flower instance so each flower as a unique set attributes"""
        lotus_flower = Flower(name=name, petal=petal_name, bulb=bulb_name, rows=petal_rows, base_petals=base_petals)

        """build the flower using the traits assigned to instance"""
        lotus_flower.organiseFlowerPetals()
        lotus_flower.movePetalsAroundBulb(offset=1)

        lotus_flower.groupAllComponents()

        FLOWER_INSTANCES.update({name: lotus_flower})

        print "Finished creating flower: ", name


# Step 3: Rig and Animation petal joints in Flower. Select the petal groups to animate
def StepThree(name, frequency, time, axis, init_bend, speed):

    if not name:
        mc.warning("Enter Name of Flower you want to animate!")
    else:
        flower = FLOWER_INSTANCES.get(name)
        FlowerAnimation.animatePetals(flower=flower, frequency=frequency, time=time,
                                      axis=axis, curr_bend=init_bend, bend_speed=speed)

        print "Finished Animating Flower Blooming for: ", name


def clearKeyFramesForFlower(name, time=120):
    if not name:
        mc.warning("Enter Name of Flower you want to clear keyframes for!")
    else:
        flower = FLOWER_INSTANCES.get(name)
        FlowerAnimation.clearAllKeyFrames(flower, max_time=time)

        print "Finished clearing all keyframes for flower: ", name

def spinFlowerForFlower(name, numRows):

    if not name:
        mc.warning("Enter Name of Flower you want to animate")
    elif not numRows:
        mc.warning("Row number not entered! Which row of petals do you want to spin?")
    else:
        flower = FLOWER_INSTANCES.get(name)
        FlowerAnimation.spinRowAnimation(flower, row_num=numRows)

        print "Finished animating Spin for flower: ", name, " at row: no. ", numRows