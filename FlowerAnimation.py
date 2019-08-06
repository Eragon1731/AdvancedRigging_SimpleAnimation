import maya.cmds as mc
import Utils

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


# This function orders all petal joints in a recognizable format. Used for custom petals
def orderPetalJoints(parent, children):

    petal_jnt = []

    for i in range(len(children)):
        petal_jnt.append(children[i])
    petal_jnt.append(parent)
    petal_jnt.reverse()

    return petal_jnt


# This function renames the petal geo and joints in recognizable format. Used for custom petals
def renamePetalChildren(jnts, separator, suffix):

    new_names = []
    for i in range(len(jnts)):
        temp = Utils.addSuffix(jnts[i], separator=separator, suffix=suffix)
        new_names.append(temp)

    return new_names


