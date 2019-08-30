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

        """load the models found"""
        ImportFlower.createBulb(bulb_path)
        ImportFlower.createPetal(petal_path)
    else:
        mc.warning("Bulb and Petal names are not defined")

# Step 2: Move Petals in place. Specify name of the parent petal joint, petal geo name, and bulb locator name in this order
def StepTwo(name, petal_name, bulb_name, petal_rows=1, base_petals=3):

    """create an Flower instance so each flower as a unique set attributes"""
    lotus_flower = Flower(name=name, petal=petal_name, bulb=bulb_name, rows=petal_rows, base_petals=base_petals)

    """build the flower using the traits assigned to instance"""
    lotus_flower.organiseFlowerPetals()
    lotus_flower.movePetalsAroundBulb(offset=1)

    lotus_flower.groupAllComponents()

    FLOWER_INSTANCES.update({name: lotus_flower})


# Step 3: Rig and Animation petal joints in Flower. Select the petal groups to animate
def StepThree():
    FlowerAnimation.animatePetals()


def clearKeyFramesForFlower(name, time=120):

    flower = FLOWER_INSTANCES.get(name)
    FlowerAnimation.clearAllKeyFrames(flower, max_time=time)


def spinFlowerForFlower(name, numRows=1):

    flower = FLOWER_INSTANCES.get(name)
    FlowerAnimation.spinRowAnimation(flower, row_num=numRows)