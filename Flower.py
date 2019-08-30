import maya.cmds as mc
import AdvancedRigging
reload(AdvancedRigging)

class Flower:
    #instances = []
    # This constructor sets the type of petal and bulb, and the amount of petal layers a flower has
    def __init__(self, name, petal, bulb, rows, base_petals):

        self.name = name

        """Sets the petal and bulb type. Also tracks num of rows and each root joint in every petal"""
        self.petal = mc.ls(petal)
        self.bulb = mc.ls(bulb)
        self.rows = rows
        self.base_petals = base_petals

        '''dict to track each layer of petals'''
        self.petal_layers = {}

        '''lists to track all petals and joints'''
        self.all_petals = []
        self.all_joints = []
        self.all_grps = []
        self.all_ctrls = []

        '''get the position of the bulb'''
        self.pos = mc.getAttr(bulb + ".translate")

    # Determines how many petals are in each row and how many rows there are. Also sets the angle and position of
    # petals relative to the bulb
    def organiseFlowerPetals(self):

        """find all the joints in petal loaded into scene"""
        joints = [x for x in mc.listRelatives(self.petal, ad=True) if "petal_joint" in x]
        joints.reverse()

        '''track all parent joints'''
        petals = []
        all_joints = []

        '''create all the petals in for each row'''
        for j in range(self.rows):

            """from the base petal num at the first layer, all layers contain one more petal than the previous"""
            curr_num = self.base_petals + j

            '''keep track of all the petals in a single row with temporary array'''
            base_petals = []

            '''create all petals by duplicating loaded petal '''
            for i in range(curr_num):

                '''duplicate and arrange petals into groups to manipulate later'''
                temp_petal = mc.duplicate(self.petal, rc=True)

                '''find petal in the group duplicated'''
                curr_petal = [x for x in temp_petal if self.petal[0] in x]

                petals.append(curr_petal)

                '''track all the joints in each petal'''
                temp_jnts = [x for x in mc.listRelatives(temp_petal, ad=True) if "petal_joint" in x]
                temp_jnts.reverse()
                all_joints.append(temp_jnts)

                '''track every root joint in each petal'''
                base_petals.append(temp_jnts[0])

            '''organize all the petal joints by their petal layer/row so User can adjust by layer/row'''
            self.petal_layers[str(j)] = base_petals

        self.all_petals = petals
        self.all_joints = all_joints

        '''delete the original petal when the Flower is done'''
        mc.delete(mc.ls(self.petal[0]))


    # This function organises the petals around the bulb. The User chooses how petal layers they want,
    # how many petals in the first layer, how many more petals for each ascending layer.
    def movePetalsAroundBulb(self, offset=1):

        '''counter to mark the range of petals to be included at each layer'''
        curr_count = 0

        '''distance and rotate the petals around the bulb for each row of petals'''
        for j in range(self.rows):

            next_count = curr_count + self.rows + j

            for i in range(curr_count, next_count):

                '''make sure petal found is within max number of petals in flower. Else, end search'''
                if i < len(self.all_petals):

                    mc.rotate(0, (360 / (self.rows+j)) * i, 0, self.all_petals[i], r=True, fo=True, os=True)
                    mc.move(self.pos[0][0] - (j * offset), self.pos[0][1], self.pos[0][2], self.all_petals[i], r=True,
                            wd=True, os=True)

                    mc.bindSkin(self.all_petals[i], self.all_joints[i])

                    '''create the spine rigs for each petal'''
                    grp, names = (AdvancedRigging.createLinearSpineControllers(self.all_joints[i], ctrl_scale=1, createXtra_grp=False))

                    self.all_grps.append(grp)
                    self.all_ctrls.append(names)

                else:
                    break

            curr_count = next_count

    # This function adjusts the position and angle of a row of petals.
    # def adjustPetalRowTransform(self, row_index=0, pos_offset=(0, 0, 0), angle=45, axis="Y"):
    #
    #     """for a selected row of petals, adjust the initial state"""
    #     curr_row = self.petal_layers["Row at "+str(row_index)]
    #
    #     print "change"
    #
    #     '''move petals in the row to new position and angle'''
    #     for petal in curr_row:
    #
    #         mc.setAttr(petal + "_grp.rotate", 0, angle, 0, type="double3")
    #         mc.rotate(0, angle, 0, petal, os=True)
    #         mc.move(pos_offset[0], pos_offset[1], pos_offset[2], petal, os=True, r=True)
    #
    # # This function adjusts the position and rotation of a single petal. Petal must be selected in the scene.
    # def adjustSinglePetalTransform(petal=None, bend=1, axis="Y"):
    #
    #     """get the selected petal"""
    #     if petal is None:
    #         petal = mc.ls(sl=True)
    #
    #     if petal is None:
    #         mc.warning("Select the petal grp to mainipulate")
    #
    #     mc.setAttr(petal + ".rotate" + axis, bend)


    def groupAllComponents(self):

        grp = mc.group(em=True, name=self.name + "_ctrlGrp")
        for group in self.all_grps:
            mc.parent(group[0], grp)



