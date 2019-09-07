import maya.cmds as mc
from Flower import Flower


"""
This function create keyframes that will bend a petal on an single axis. The User can define the frequency
 of keyframes, the time of animation, the axis the petal bends on and the angle the petal bends at.
"""


def animatePetals(flower, bend_speed, frequency=5, time=120, axis="Z", curr_bend=0):

    # get the list of all joints for each petal
    ctrls = flower.all_ctrls

    # temp container to store all ctrls
    all_ctrls = []

    # get every joint in all the petals
    for i in range(len(ctrls)):
        for j in range(len(ctrls[i])):
            all_ctrls.append(ctrls[i][j])

    # Set up for the first keyframe
    counter = frequency

    # rotate and keyframe all joints within a set amount of time. For each keyframe, rotate controller back "curr_bend"
    while counter < time:
        for i in range(len(all_ctrls)):
            new_rot = mc.getAttr(str(all_ctrls[i]) + ".rotate" + axis)
            mc.setKeyframe(all_ctrls[i], v=new_rot + curr_bend, attribute="rotate" + axis, t=counter)

        counter += frequency
        curr_bend += bend_speed


"""
Spin the petals around the bulb's center. Spins all rows by default or specify a row to spin at.
"""


def spinRowAnimation(flower, row_num=1, frequency=5, time=120, spin_speed=10):

    # get the petals in a row to re-animate for a specific flower
    petals = flower.petal_layers.get(str(row_num))

    # If the row number doesn't exist, return false to tell User to re enter a correct row number for flower
    if petals is None:
        mc.warning("Row Number does not Exist (Out of Bounds)! Enter an existing row number")
        return False

    # for each parent joint in the petals list, find its group
    grps = [x + "_grp" for x in petals]

    # Set up for first keyframe and initial rotation angle
    counter = frequency
    curr_angle = 0

    # Set a parent constraint on the bulb loc. Makes sure the petals spin in relation to the bulb location
    bulb_loc = flower.bulb

    for grp in grps:
        mc.parentConstraint(bulb_loc, grp, mo=1)

    # Rotate the petals around the bulb locator
    while counter < time:
        rot = mc.getAttr(str(bulb_loc[0]) + ".rotateY")
        mc.setKeyframe(bulb_loc[0], v=rot + curr_angle, attribute="rotateY", t=counter)
        counter += frequency
        curr_angle += spin_speed

    return True


"""
Clears all keyframes in all flower assets so User can reanimate petals
"""


def clearAllKeyFrames (flower, max_time=120):

    # check to see if User deleted or renamed ctrls
    for i in range(len(flower.all_ctrls)):
        if not mc.objExists(flower.all_ctrls[i][0]):
            del flower.all_ctrls[i]

    # get all children in the root group of all flower assets
    children = flower.all_ctrls

    # clear all keyframes
    for i in range(len(children)):
        mc.cutKey(children[i], time=(0, max_time))
        mc.makeIdentity(children[i], rotate=True)
