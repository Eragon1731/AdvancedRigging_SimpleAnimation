import maya.cmds as mc
import AdvancedRigging

PETAL_ROWS = []


class Flower:

    # This constructor sets the type of petal and bulb and the num of rows a flower has
    def __init__(self, petal, bulb, rows, base_petals):
        self.petal = mc.ls(petal)
        self.bulb = mc.ls(bulb)
        self.rows = rows
        self.base_petals = base_petals

        '''dict for moving petals in position'''
        self.petal_layers = {}

        '''dict for rigging all petals'''
        self.all_petals = []
        self.all_joints = []

        '''get the position of the bulb'''
        self.pos = mc.getAttr(bulb + ".translate")


    # Determines how many petals are in each row and how many rows there are. Also sets the angle and position of
    # petals relative to the bulb
    def organiseFlowerPetals(self):

        joints = [x for x in mc.listRelatives(self.petal, ad=True) if "petal_joint" in x]
        joints.reverse()

        '''track all parent joints'''
        petals = []
        all_joints = []

        '''create all the petals in for each row'''
        for j in range(self.rows):

            curr_num = self.base_petals + j

            for i in range(curr_num):
                '''keep track of all the petals in a single row with temporary array'''
                base_petals = []

                '''duplicate and arrange petals into groups to manipulate later'''
                temp_petal = mc.duplicate(self.petal, rc=True)

                '''track each petal'''
                curr_petal = [x for x in temp_petal if self.petal[0] in x]

                petals.append(curr_petal)
                base_petals.append(curr_petal)

                '''track all the joints in each petal'''
                temp_jnts = [x for x in mc.listRelatives(temp_petal, ad=True) if "petal_joint" in x]
                temp_jnts.reverse()
                all_joints.append(temp_jnts)


            '''track all the petal joints in each row so User can adjust by row'''
            self.petal_layers["Row at "+str(j)] = base_petals

        self.all_petals = petals
        self.all_joints = all_joints


    # This function organises the petals around the bulb. The User chooses how petal layers they want,
    # how many petals in the first layer, how many more petals for each ascending layer.
    def movePetalsAroundBulb(self, offset=1):

        curr_count = 0

        '''distance and rotate the petals around the bulb for each row of petals'''
        for j in range(self.rows):

            next_count = curr_count + self.rows + j

            print "from: ", curr_count, "to: ", next_count

            for i in range(curr_count, next_count):

                if i < len(self.all_petals):

                    '''print checks'''
                    #print "angle of petal is: ", (360 / (self.rows+j)) * i, " at index: ",i

                    mc.rotate(0, (360 / (self.rows+j)) * i, 0, self.all_petals[i], r=True, fo=True, os=True)
                    mc.move(self.pos[0][0] - (j * offset), self.pos[0][1], self.pos[0][2], self.all_petals[i], r=True,
                            wd=True, os=True)

                    mc.bindSkin(self.all_petals[i], self.all_joints[i])

                    '''create the spine rigs for each petal'''
                    AdvancedRigging.createLinearSpineControllers(self.all_joints[i], ctrl_scale=1, createXtra_grp=False)

                else:
                    break

            curr_count = next_count




    # This function adjusts the position and angle of a row of petals.
    def adjustPetalRowTransform(row_index=0, pos_offset=(0, 0, 0), angle=45, axis="Y"):

        """for a selected row of petals, adjust the initial state"""
        curr_row = PETAL_ROWS[row_index]

        '''move petals in the row to new position and angle'''
        for petal in curr_row:
            mc.setAttr(petal + ".rotate" + axis, 0, angle, 0, type="double3")
            mc.rotate(0, angle, 0, petal, os=True)
            mc.move(pos_offset[0], pos_offset[1], pos_offset[2], petal, os=True, r=True)


    # This function adjusts the position and rotation of a single petal. Petal must be selected in the scene.
    def adjustSinglePetalTransform(petal=None, bend=1, axis="Y"):

        """get the selected petal"""
        if petal is None:
            petal = mc.ls(sl=True)

        petal.setAttr(petal + ".rotate" + axis, bend)