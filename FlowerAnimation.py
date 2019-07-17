import maya.cmds as mc

#organise the petals around the bulb. Define how many rows/layer of petals for the flower,
# the distance from the bulb, how many petals on the first row layer.
def movePetalsAroundBulb(bulb=None, rows=1, distance=5, num_petals=3, shape="circle"):

    if bulb is None:
        bulb = mc.ls(sl=True)

    '''set up the inital variables'''
    amount = num_petals

    '''for each row, move and orient all the petals into position'''
    for i in rows:
        petals = duplicatePetals(shape=shape, amount= (amount + i))
        for j in range(len(petals)):
            mc.rotate(0,360/amount,0, petals[j], pivot=(0,0,0))
            mc.move(0, 0, -distance * j, petals[j], a=True)



#duplicates all the petals per row/layer of the flower
def duplicatePetals(shape="circle", amount=3):

    petal = mc.polySphere(n="petal")

    if shape == "circle":

    elif shape == "triangle":
        #create sharp petal
    else:
        #create wavy petal

    petals = []

    '''create all the petals'''
    for i in range(amount):
        mc.duplicate

    return petals



