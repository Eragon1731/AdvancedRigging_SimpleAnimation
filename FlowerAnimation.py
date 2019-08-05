import maya.cmds as mc
import Utils
import AdvancedRigging

PETAL_ROWS = []

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


# This function organises the petals around the bulb. The User chooses how petal layers they want,
# how many petals in the first layer, how many more petals for each ascending layer.
def movePetalsAroundBulb(petal, bulb, rows, num_petals=3, offset=5):

    petal_grp = mc.ls(petal)

    joints = [x for x in mc.listRelatives(petal_grp, ad=True) if "petal_joint" in x]
    joints.reverse()

    '''get the position of the bulb'''
    pos = mc.getAttr(bulb + ".translate")

    '''track all parent joints'''
    petals = [petal_grp]
    all_joints = [joints]

    '''create all the petals in for each row'''
    for j in range(rows):

        for i in range(num_petals-1):

            '''keep track of all the petals in a single row with temporary array'''
            base_petals = []

            '''duplicate and arrange petals into groups to manipulate later'''
            temp_petal = mc.duplicate(petal, rc=True)

            '''track each petal'''
            curr_petal = [x for x in temp_petal if petal in x]
            petals.append(curr_petal)
            base_petals.append(curr_petal)

            '''track all the joints in each petal'''
            temp_jnts = [x for x in mc.listRelatives(temp_petal, ad=True) if "petal_joint" in x]
            temp_jnts.reverse()
            all_joints.append(temp_jnts)

        '''track all the petal joints in each row so User can adjust by row'''
        PETAL_ROWS.append(base_petals)


    print "petals: ", petals

    '''distance and rotate the petals around the bulb for each row of petals'''
    for j in range(rows):
        for i in range(0, len(petals)):

            mc.rotate(0, (360/num_petals) * i, 0, petals[i], r=True, fo=True, os=True)
            mc.move(pos[0][0], pos[0][1], pos[0][2] + (j * offset), petals[i], os=True, wd=True, r=True)

            mc.bindSkin(petals[i], all_joints[i])

            '''create the spine rigs for each petal'''
            AdvancedRigging.createLinearSpineControllers(all_joints[i], ctrl_scale=1, createXtra_grp=False)


# This function adjusts the position and angle of a row of petals.
def adjustPetalRowAnimation(row_index=0, pos_offset=(0, 0, 0), angle=45, axis="Y"):

    """for a selected row of petals, adjust the initial state"""
    curr_row = PETAL_ROWS[row_index]

    '''move petals in the row to new position and angle'''
    for petal in curr_row:
        mc.setAttr(petal + ".rotate" + axis, 0, angle, 0, type="double3")
        mc.rotate(0, angle, 0, petal, os=True)
        mc.move(pos_offset[0], pos_offset[1], pos_offset[2], petal, os=True, r=True)


# This function adjusts the position and rotation of a single petal. Petal must be selected in the scene.
def adjustSinglePetalAnimation(petal=None, bend=1, axis="Y"):

    """get the selected petal"""
    if petal is None:
        petal = mc.ls(sl=True)

    petal.setAttr(petal + ".rotate"+axis, bend)


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


