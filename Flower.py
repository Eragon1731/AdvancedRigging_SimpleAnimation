import maya.cmds as mc
import os
import AdvancedRigging

#Create the bulb by importing a bulb type from default lib
#path : "/Users/christyye/Documents/maya/projects/Advanced_Rigging/bulb_default.fbx "
def createBulb(path):

    mc.file(path, i=True)

    '''create a loc for bulb'''
    dir_path = os.path.basename(os.path.normpath(path)).split(".")[0]

    object = mc.ls(dir_path)
    AdvancedRigging.createCenterLocatorController(object, orient=False)


#Create a single petal by importing a petal type from default lib
#testing default is : "/Users/christyye/Documents/maya/projects/Advanced_Rigging/petal_default.fbx "
def createPetal(path):

    mc.file(path, i=True)

    '''find the petal'''
    dir_path = os.path.basename(os.path.normpath(path)).split(".")[0]

    object = mc.ls(dir_path)

    children = mc.listRelatives(object, ad=True)[:-1]

    joints = []
    meshes = []
    for i in range(len(children)):
        print mc.objectType(children[i])
        if mc.objectType(children[i]) == "joint":
            mc.rename(children[i], "petal_joint" + str(i))
            joints.append(children[i])
        elif mc.objectType(children[i]) == "mesh":
            mc.rename(children[i], "petal_geo"+str(i))
            meshes.append(children[i])

    return joints, meshes
