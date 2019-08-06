import ImportFlower
import FlowerAnimation
from Flower import Flower
import os

#Step 1: Load the models
def StepOne(bulb="bulb_default", petal="petal_default"):

    current_dir = os.path.dirname(__file__)
    bulb_path = os.path.join(current_dir, "Assets", bulb + ".fbx")

    petal_path = os.path.join(current_dir, "Assets", petal + ".fbx")

    print petal_path
    ImportFlower.createBulb(bulb_path)
    ImportFlower.createPetal(petal_path)

#Step 2: Move Petals in place. Specify name of the parent petal joint, petal geo name, and bulb locator name in this order
def StepTwo(petal_name, bulb_name, petal_rows=1, base_petals=3):

    lotus_flower = Flower(petal=petal_name, bulb=bulb_name, rows=petal_rows, base_petals=base_petals)
    lotus_flower.organiseFlowerPetals()
    lotus_flower.movePetalsAroundBulb(offset=1)

#Step 3: Rig and Animation joints. Select the controller group for each petal
def StepThree():
    FlowerAnimation.animatePetals(axis="Z")