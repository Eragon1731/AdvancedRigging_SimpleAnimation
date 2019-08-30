import ImportFlower
reload(ImportFlower)
import FlowerAnimation
reload(FlowerAnimation)

from FlowerMain import StepOne
from FlowerMain import StepTwo
from FlowerMain import StepThree
from FlowerMain import clearKeyFramesForFlower

from maya import OpenMayaUI as omui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *
from shiboken2 import wrapInstance

mayaMainWindowPtr = omui.MQtUtil.mainWindow()
MAYA_MAIN_WINDOW = wrapInstance(long(mayaMainWindowPtr), QWidget)

WIN_TITLE = "Flower Animation"
TAB01_TITLE = "Load Assets"
TAB02_TITLE = "Build Flower Attributes"
TAB03_TITLE = "Animate Flower"

PETAL_NAME = ""
BULB_NAME = ""

class ExampleTab(QWidget):
    def __init__(self, layout_type, *args, **kwargs):
        super(ExampleTab,self).__init__(*args, **kwargs)
        self.layout_type = layout_type
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout(self)
        sublayout = getattr(self, self.layout_type)()
        self.layout.addLayout(sublayout)
        self.setLayout(self.layout)


    def layout01(self):
        layout = QVBoxLayout()

        #Load the flower parts: Allow users to add their flower parts to the list
        bulbTitle = QLabel("Bulb Name:")
        bulbNameBox = QLineEdit("lotus_bulb")
        petalTitle = QLabel("Petal Name:")
        petalNameBox = QLineEdit("lotus_petal")

        pybutton = QPushButton("Load")
        pybutton.clicked.connect(lambda: StepOne(bulbNameBox.text(), petalNameBox.text()))

        layout.addWidget(bulbTitle)
        layout.addWidget(bulbNameBox)
        layout.addWidget(petalTitle)
        layout.addWidget(petalNameBox)
        layout.addWidget(pybutton)

        return layout

    '''create a default flower with default animation'''
    def layout02(self):
        layout = QVBoxLayout()

        rowsTitle = QLabel("Assign Petal Rows")
        baseTitle = QLabel("Assign Base Petals")
        nameTitle = QLabel("Name the flower")
        petalTitle = QLabel("Petal Anim Model Name")
        bulbTitle = QLabel("Bulb Anim Model Name")

        # Use second tab to edit Flower Attrs
        petalRows = QSpinBox()
        petalRows.setValue(3)
        basePetals = QSpinBox()
        basePetals.setValue(3)
        nameValue = QLineEdit()
        petalName = QLineEdit("lotus_petal")
        bulbName = QLineEdit("lotus_bulb_geo")

        button = QPushButton("Ok")

        button.clicked.connect(lambda: StepTwo(nameValue.text(), petalName.text(),
                                               bulbName.text(), petalRows.value(), basePetals.value()))

        # Add widgets to layout
        layout.addWidget(nameTitle)
        layout.addWidget(nameValue)
        layout.addWidget(petalTitle)
        layout.addWidget(petalName)
        layout.addWidget(bulbTitle)
        layout.addWidget(bulbName)
        layout.addWidget(rowsTitle)
        layout.addWidget(petalRows)
        layout.addWidget(baseTitle)
        layout.addWidget(basePetals)

        layout.addWidget(button)

        return layout

    def layout03(self):
        layout = QVBoxLayout()

        # Default animation for flower
        timeTitle = QLabel("Animation Time Length")
        frequencyTitle = QLabel("Keyframe frequency within Time Limit: ")
        axisTitle = QLabel("Which axis to animate on: ")
        speedTitle = QLabel("Speed of Animation: ")

        timeBox = QSpinBox()
        timeBox.setRange(0, 240)
        timeBox.setValue(120)
        frequencyBox = QLineEdit()
        frequencyBox.setValidator(QIntValidator())
        axisBox = QComboBox()
        axisBox.addItems(["X", "Y", "Z"])
        speedBox = QSpinBox()
        speedBox.setRange(1, 20)

        animateInstructions = QLabel("Select the ctrl group(s) you want to animate with")
        animateButton = QPushButton("Animate the Flower Blooming")
        animateButton.clicked.connect(lambda: StepThree())

        # All edits that can be made on a flower
        clearButton = QPushButton("Clear Keyframes")
        clearText = QLineEdit()
        clearButton.clicked.connect(lambda: clearKeyFramesForFlower(clearText.text()))

        numRows = QLineEdit().setValidator(QIntValidator())
        spinButton = QPushButton("Spin the Flower")
        spinText = QLineEdit()
        spinButton.clicked.connect(lambda: main.spinFlowerForFlower(spinText.text(), numRows.value()))

        layout.addWidget(timeTitle)
        layout.addWidget(timeBox)
        layout.addWidget(frequencyTitle)
        layout.addWidget(frequencyBox)
        layout.addWidget(axisTitle)
        layout.addWidget(axisBox)
        layout.addWidget(speedTitle)
        layout.addWidget(speedBox)
        layout.addWidget(animateInstructions)
        layout.addWidget(animateButton)

        layout.addWidget(clearText)
        layout.addWidget(clearButton)

        layout.addWidget(numRows)
        layout.addWidget(spinText)
        layout.addWidget(spinButton)

        return layout

    # Test functions
    # def build_flower(self, name, petalName, bulbName, petalRows, basePetals):
    #     StepTwo(name, petalName, bulbName, petalRows, basePetals)
    #     PETAL_NAME = name
    #     BULB_NAME = name

    def on_click_button(self, val):
        print "build a spine with %s joints" %(val)


class MainWindow(QTabWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setParent(MAYA_MAIN_WINDOW)
        self.setWindowFlags(Qt.Window)
        self.init_ui()
        self.inserted_text = ""
        self.is_checked = False

    def init_ui(self):
        self.setWindowTitle(WIN_TITLE)
        main_layout = QGridLayout()
        self.setLayout(QGridLayout())

        #create a tab for each category of functionality
        tab01 = ExampleTab("layout01")
        tab02 = ExampleTab("layout02")
        tab03 = ExampleTab("layout03")

        #Add all the tabs
        self.addTab(tab01, TAB01_TITLE)
        self.addTab(tab02, TAB02_TITLE)
        self.addTab(tab03, TAB03_TITLE)

        self.show()


def main():
    MainWindow()
