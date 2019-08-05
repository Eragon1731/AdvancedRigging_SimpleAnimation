import Flower
import FlowerAnimation
import os

#Step 1: Load the models
def StepOne(bulb="bulb_default", petal="petal_default"):

    current_dir = os.path.dirname(__file__)
    bulb_path = os.path.join(current_dir, "Assets", bulb + ".fbx")

    petal_path = os.path.join(current_dir, "Assets", petal + ".fbx")

    print petal_path
    Flower.createBulb(bulb_path)
    Flower.createPetal(petal_path)

#Step 2: Move Petals in place. Specify name of the parent petal joint, petal geo name, and bulb locator name in this order
def StepTwo(petal_name):
    FlowerAnimation.movePetalsAroundBulb(petal=petal_name)

#Step 3: Rig and Animation joints. Select the controller group for each petal
def StepThree():
    FlowerAnimation.animatePetals(axis="Y")