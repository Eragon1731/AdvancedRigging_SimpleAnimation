import maya.cmds as mc
import random as rand
import AdvancedRigging

#set up lantern distribution and spin animation
def createLanternAnimation(selected=None):

    if selected is None:
        selected = mc.ls(sl=True)

    lantern_group = lanternDistribution(selected=selected, max=10, uniform_range=5)

    spinAnimation(selected=lantern_group, axis=None, time=120, frequency=5)

#function clones and randomly distributes an object in world space.
def lanternDistribution(selected=None, max=10, uniform_range=5):

    obj_list = []

    '''if no object is found, assign object as one selected in scene'''
    if selected is None:
        selected = mc.ls(sl=True)

    if len(selected) != 1:
        print selected
        mc.warning("Please select an object with ONE locator")
        return

    obj_list.append(selected)

    '''randomly distribute objects in world space'''
    for i in range(0, max):
        dup = mc.duplicate(obj_list[-1], rc=True)
        moveX = rand.randint(-uniform_range, uniform_range)
        moveY = rand.randint(-uniform_range, uniform_range)
        moveZ = rand.randint(-uniform_range, uniform_range)
        mc.move(moveX, moveY, moveZ, ws=True)

        obj_list.append(dup)

    '''group all objects in list'''

    main_group = mc.group(n="main_group")

    for i in range(len(obj_list) - 1):
        mc.parent(obj_list[i], main_group)

    return main_group


def spinAnimation (selected=None, axis=None, time=120, frequency=5):

    locators = []

    children_selected = mc.listRelatives(selected, children=True)

    print children_selected

    if axis is None:
        axis = "Y"

    '''animate center locators not the model itself'''

    locators.append(AdvancedRigging.createCenterLocatorController(children_selected))

    '''determine the initial rotation angle in degrees'''
    angle = 0

    '''determine at what intervals to set keyframes'''
    counter = frequency


    print "children name: ", children_selected[0]

    while counter < time:
        for i in range(len(locators[0])):
            mc.xform(children_selected[i], rotation=(0, 90, 0), os=True, relative=True)

            new_rot = mc.getAttr(str(children_selected[i]) + ".rotate" + axis)
            mc.setKeyframe(locators[0][i], v=new_rot, attribute="rotate"+axis, t=counter)

        counter += frequency
