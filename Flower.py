import maya.cmds as mc
import AdvancedRigging

#Create the bulb by importing a bulb type from default lib
def createBulb():

    bulb = mc.polySphere()

    AdvancedRigging.createCenterLocatorController(bulb)

    return bulb


#Create a single petal by importing a petal type from default lib
def createPetal():

