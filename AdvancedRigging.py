import maya.cmds as mc
import Utils

CTRL_SCALE = 1

def createCenterLocatorController(selected=None, orient=True):

    locs = []
    if selected is None:
        selected = mc.ls(sl=True)

    for i in range(len(selected)):

        center_pos = mc.xform(selected[i], q=True, t=True)

        print "child is: ", selected[i], "at: ", center_pos

        center_name = selected[i] + "_loc"
        center_loc = mc.spaceLocator(p=center_pos, n=center_name)
        locs.append(center_loc)
        mc.makeIdentity(selected[i], apply=True, translate=True)

        if(orient):
            mc.orientConstraint(center_loc, selected[i], mo=1)

    return locs


def createSpineControllers(fk_joints=None, ctrl_scale=CTRL_SCALE, createXtra_grp=False):

    if fk_joints is None:
        fk_joints = mc.ls(sl=True)

    grps, names = createControllers(selected=fk_joints, ctrl_scale=ctrl_scale,
                                    createXtra_grp=createXtra_grp)

    print "names: ", names
    for i in range(1, len(grps)):
        mc.parent(grps[i], names[i - 1])

    return names


def createControllers (selected=None, ctrl_scale=CTRL_SCALE, createXtra_grp=False):

    if selected is None:
        selected = mc.ls(sl=True)[0]

    print "selected: ", selected[0]

    '''check if is a bnd joint'''
    currlist = [x for x in selected if "joint" in x]

    ctrlnames = []
    grpnames = []

    print "currlist: "

    '''creating controllers'''
    for i in range(len(currlist)):

        ''' get new names'''
        ctrlname = Utils.addSuffix(currlist[i], "ctrl", "_")
        grpname = Utils.addSuffix(currlist[i], "grp", "_")
        orientname = Utils.addSuffix(currlist[i], "oct", "_")
        parentname = Utils.addSuffix(currlist[i], "par", "_")

        '''joint position'''
        jnt_pos = mc.xform(currlist[i], q=True, translation=True, ws=True)

        '''create and place controller'''
        ctrl = mc.circle(n=ctrlname, r=ctrl_scale, normal=(1, 0, 0))[0]
        grp = mc.group(ctrl, n=grpname)

        if createXtra_grp:
            grp = mc.group(grp, name=grpname + "_outerGrp")

        mc.move(jnt_pos[0], jnt_pos[1], jnt_pos[2], grp, a=True)
        ctrl_cvs = mc.ls(ctrlname + ".cv[*]")
        mc.scale(ctrl_scale, ctrl_scale, ctrl_scale, ctrl_cvs)

        '''orient constraint'''
        tempconstraint = mc.orientConstraint(currlist[i], grp, mo=0)
        mc.delete(tempconstraint)
        mc.orientConstraint(ctrl, selected[i], mo=1, name=orientname)

        '''parent constraints'''
        mc.parentConstraint(ctrl, selected[i], mo=1, name=parentname)


        '''get all names'''
        ctrlnames.append(ctrlname)
        print "ctrlnames: ", ctrlnames
        grpnames.append(grpname)


    return grpnames, ctrlnames