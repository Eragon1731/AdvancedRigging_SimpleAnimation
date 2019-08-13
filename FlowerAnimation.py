import maya.cmds as mc
import Utils
from Flower import Flower

# This function create keyframes that will bend a petal on an single axis. The User can adjust the frequency
# of keyframes, the time of animation, the axis the petal bends on and the angle the petal bends at.
def animatePetals(ctrls=None, frequency=5, time=120, axis="Z", curr_bend=1, bend_speed=0.5):

    if ctrls is None:
        temp = mc.ls(sl=True)
        ctrls = [x for x in mc.listRelatives(temp, ad=True, type="transform") if "_ctrl" in x]

    all_ctrls = []

    for i in range(len(ctrls)):
        all_ctrls.append(ctrls[i])

    counter = frequency
    while counter < time:
        for i in range(len(all_ctrls)):
            new_rot = mc.getAttr(str(all_ctrls[i]) + ".rotate" + axis)
            mc.setKeyframe(all_ctrls[i], v=new_rot + curr_bend, attribute="rotate" + axis, t=counter)

        counter += frequency
        curr_bend += bend_speed


# This function re-animates the selected Petals
def changeRowAnimation(flower, row=1, frequency=5, time=120, axis="Z", curr_bend=1, bend_speed=0.5):


    """get the petals in a row to re-animate for a specific flower"""
    petals = flower.petal_layers["Row at "+str(row)]

    group = []

    """for each parent joint in the petals list, find it's group"""
    for i in petals:
        temp = [x for x in i if "_grp" in x]
        print "temp: ", temp
        group.append([x for x in i if "_grp" in x])





