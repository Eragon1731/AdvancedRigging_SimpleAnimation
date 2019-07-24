import maya.cmds as mc
import Utils
import AdvancedRigging


def animatePetals(jnts=None, frequency=5, time=120, axis="Z", curr_bend=1, bend_speed=2):

    if jnts is None:
        jnts = mc.ls(sl=True)

    alljnts = []

    for i in range(len(jnts)):
        alljnts.append(jnts[i])

    children = mc.listRelatives(jnts, ad=True)

    for i in range(len(children)):
        alljnts.append(children[i])


    currlist = [x for x in alljnts if "grp" in x]

    print "jnts count", (jnts)
    print "all jnts count", range(len(alljnts))
    print "all grps: ", len(currlist)

    counter = frequency
    while counter < time:
        for i in range(len(currlist)):
            new_rot = mc.getAttr(str(currlist[i]) + ".rotate" + axis)
            print "new_rot: ", new_rot
            mc.setKeyframe(currlist[i], v=new_rot + curr_bend, attribute="rotate" + axis, t=counter)

        counter += frequency
        curr_bend += bend_speed



#organise the petals around the bulb. Define how many rows/layer of petals for the flower,
#how many petals on the first row layer.
#User must select petal joints in order to move petal
def movePetalsAroundBulb(joint=None, petal=None, bulb=None, rows=1, num_petals=3):

    if joint is None:
        temp = mc.ls(sl=True)[0]
        joints = mc.listRelatives(temp, ad=True)
        petal_jnt = orderPetalJoints(parent=temp, children=joints)

    if petal is None:
        petal = mc.ls(sl=True)[1]
        print "this is petal_geo: ", petal

    if bulb is None:
        bulb = mc.ls(sl=True)[2]
        pos = mc.getAttr(bulb + ".translate")

    '''track all parent joints'''
    base_jnts = [petal_jnt[0]]
    all_joints = [petal_jnt]

    print "this is petal : ", petal_jnt
    for i in range(num_petals-1):
        temp_jnts = mc.duplicate(petal_jnt, rc=True)
        temp_petal = mc.duplicate(petal, rc=True)
        mc.bindSkin(temp_jnts, temp_petal)
        base_jnts.append(temp_jnts[0])
        all_joints.append(temp_jnts)

    '''arrange petals for one row'''
    for i in range(len(base_jnts)):
        mc.rotate((360/num_petals) * i, 0, 0, base_jnts[i], os=True)
        mc.move(pos[0][0], pos[0][1], pos[0][2], base_jnts[i], a=True)

        AdvancedRigging.createSpineControllers(all_joints[i], ctrl_scale=1,createXtra_grp=False)


#rename all children
def orderPetalJoints(parent, children):

    petal_jnt = []

    for i in range(len(children)):
        petal_jnt.append(children[i])
    petal_jnt.append(parent)
    petal_jnt.reverse()

    return petal_jnt


def renamePetalChildren(jnts, separator, suffix):

    new_names = []
    for i in range(len(jnts)):
        temp = Utils.addSuffix(jnts[i], separator=separator, suffix=suffix)
        new_names.append(temp)

    return new_names


