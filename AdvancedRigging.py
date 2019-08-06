import maya.cmds as mc
import Utils

CTRL_SCALE = 1

def createCenterLocatorController(selected=None, orient=True):

    locs = []

    center_pos = mc.xform(selected, q=True, t=True)
    center_name = selected[0] + "_loc"

    center_loc = mc.spaceLocator(p=center_pos, n=center_name)
    locs.append(center_loc)
    mc.makeIdentity(selected, apply=True, translate=True)

    if(orient):
        mc.orientConstraint(center_loc, selected, mo=1)

    mc.rename(selected[0], selected[0]+"_geo")

    if mc.ls(selected[0]) > 0:
        mc.group(selected[0] + "_geo", center_loc, name=Utils.changeSuffix(selected[0], "geo", "", "_"))

    return locs


# This function creates a rig that will bend the petal in a Linear manner. The root jnt is
# at the bottom of the petal and there is a single chain going up the petal
def createLinearSpineControllers(fk_joints=None, ctrl_scale=CTRL_SCALE, createXtra_grp=False):

    grps, names = createControllers(selected=fk_joints, ctrl_scale=ctrl_scale,
                                    createXtra_grp=createXtra_grp)
    for i in range(1, len(grps)):
        mc.parent(grps[i], names[i - 1])

    return names


def createControllers (selected, shape= "circle", ctrl_scale=CTRL_SCALE, createXtra_grp=False):

    print "selected: ", selected[0]

    '''check if is a bnd joint'''
    currlist = [x for x in selected if "joint" in x]

    ctrlnames = []
    grpnames = []

    '''creating controllers'''
    for i in range(len(currlist)):

        ''' get new names'''
        ctrlname = Utils.addSuffix(currlist[i], "ctrl", "_")
        grpname = Utils.addSuffix(currlist[i], "grp", "_")
        parentname = Utils.addSuffix(currlist[i], "par", "_")

        '''joint position'''
        jnt_pos = mc.xform(currlist[i], q=True, translation=True, ws=True)

        '''create and place controller'''
        ctrl = mc.circle(n=ctrlname, r=ctrl_scale, normal=(0, 1, 0))[0]
        grp = mc.group(ctrl, n=grpname)

        if createXtra_grp:
            grp = mc.group(grp, name=grpname + "_outerGrp")

        mc.move(jnt_pos[0], jnt_pos[1], jnt_pos[2], grp, a=True)
        ctrl_cvs = mc.ls(ctrlname + ".cv[*]")
        mc.scale(ctrl_scale, ctrl_scale, ctrl_scale, ctrl_cvs)

        '''orient constraint'''
        tempconstraint = mc.orientConstraint(currlist[i], grp, mo=0)
        mc.delete(tempconstraint)

        '''parent constraints'''
        mc.parentConstraint(ctrl, selected[i], mo=1, name=parentname)


        '''get all names'''
        ctrlnames.append(ctrlname)
        grpnames.append(grpname)


    return grpnames, ctrlnames