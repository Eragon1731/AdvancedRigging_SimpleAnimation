import maya.cmds as mc
import os
import AdvancedRigging

#Create the bulb by importing a bulb type from default lib
#path : "/Users/christyye/Documents/maya/projects/Advanced_Rigging/bulb_default.fbx "
def createBulb(path="abs_path"):

    mc.file(path, i=True)

    '''create a loc for bulb'''
    dir_path = os.path.basename(os.path.normpath(path)).split(".")[0]
    bulb = setLocforSelected(dir_path)

    print "bulb: ", bulb

    AdvancedRigging.createCenterLocatorController(bulb, orient=False)

    return bulb


#Create a single petal by importing a petal type from default lib
#testing default is : "/Users/christyye/Documents/maya/projects/Advanced_Rigging/petal_default.fbx "
def createPetal(path="abs_path"):

    mc.file(path, i=True)


def setLocforSelected(name="bulb_default"):

    object = mc.ls(name)
    print "object: ", object

    return object