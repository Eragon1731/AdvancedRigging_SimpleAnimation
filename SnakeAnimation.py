import maya.cmds as mc

def createSnakeAnimation(selected=None, curve=None, time=120, frequency=10):

    if selected is None:
        selected = mc.ls(sl=True)[0]

    if curve is None:
        curve = mc.ls(sl=True)[1]

    '''check the selected items'''
    if len(mc.ls(sl=True)) < 2:
        mc.warning("Please select the object and then the curve")

