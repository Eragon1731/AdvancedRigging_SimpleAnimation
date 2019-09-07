import ImportFlower
reload(ImportFlower)
import FlowerAnimation
reload(FlowerAnimation)

import FlowerMain

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

"""
Creates all the layouts for the tool. There are 3 parts to the tool: Loading the assets, Building the Flower, and
Animating the Flower
"""


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

    # Creates the UI Tab for Loading the Flower Assets
    def layout01(self):
        layout = QGridLayout()

        # Allow Users to add their flower parts from local dir
        bulbTitle = QLabel("Bulb Name:")
        bulbNameBox = QLineEdit("lotus_bulb")
        petalTitle = QLabel("Petal Name:")
        petalNameBox = QLineEdit("lotus_petal")

        pybutton = QPushButton("Load")
        pybutton.clicked.connect(lambda: FlowerMain.StepOne(bulbNameBox.text(), petalNameBox.text()))

        # Organising layout of UI
        layout.addWidget(bulbTitle,0,0)
        layout.addWidget(bulbNameBox,0,1)
        layout.addWidget(petalTitle,1,0)
        layout.addWidget(petalNameBox,1,1)
        layout.addWidget(pybutton, 2, 0, 1, 2)

        return layout

    # Creates the UI Tab for Building the Flower
    def layout02(self):
        layout = QGridLayout()

        # String validator to make sure Users do not use numbers or special chars
        regex = QRegExp("[a-z-A-Z_]+")
        validator = QRegExpValidator(regex)

        rowsTitle = QLabel("Assign Petal Rows")
        baseTitle = QLabel("Assign Base Petals")
        nameTitle = QLabel("Name the flower")
        petalTitle = QLabel("Petal Name")
        bulbTitle = QLabel("Bulb Locator Name")

        petalRows = QSpinBox()
        petalRows.setValue(3)
        basePetals = QSpinBox()
        basePetals.setValue(3)
        nameValue = QLineEdit()
        nameValue.setValidator(validator)
        petalName = QLineEdit("lotus_petal")
        petalName.setValidator(validator)
        bulbName = QLineEdit("lotus_bulb_loc")
        bulbName.setValidator(validator)

        button = QPushButton("Create the Flower")

        button.clicked.connect(lambda: FlowerMain.StepTwo(nameValue.text(), petalName.text(),
                                                bulbName.text(), petalRows.value(), basePetals.value()))

        # Organising layout of UI
        layout.addWidget(nameTitle, 0, 0)
        layout.addWidget(nameValue, 0, 1)
        layout.addWidget(petalTitle, 1, 0)
        layout.addWidget(petalName, 1, 1)
        layout.addWidget(bulbTitle, 2, 0)
        layout.addWidget(bulbName, 2, 1)
        layout.addWidget(rowsTitle, 3, 0)
        layout.addWidget(petalRows, 3, 1)
        layout.addWidget(baseTitle, 4, 0)
        layout.addWidget(basePetals, 4, 1)

        layout.addWidget(button,5,0,1,2)

        return layout

    def layout03(self):
        layout = QGridLayout()

        # String validator to make sure Users do not use numbers or special chars
        regex = QRegExp("[a-z-A-Z_]+")
        validator = QRegExpValidator(regex)

        # Titles and Instructions for this tab
        timeTitle = QLabel("Animation Time Length")
        frequencyTitle = QLabel("Keyframe frequency within Time Limit: ")
        axisTitle = QLabel("Which axis to animate on: ")
        speedTitle = QLabel("Speed of Animation: ")
        bloomInstructions= QLabel("Bloom according to all inputs above. MUST enter Flower name")
        spinInstructions = QLabel("Spin according to all inputs above. MUST enter Flower name AND row number")
        clearInstructions = QLabel("Clear ALL keyframes. Clear may not affect keyframes created OUTSIDE of tool")
        spinTextTitle = QLabel("Name of flower to animate/edit")
        numRowsTitle = QLabel("Which row num do you want to spin: ")

        # Input Variables for Animations/Clear Keyframes
        nameText = QLineEdit()
        nameText.setValidator(validator)
        timeBox = QSpinBox()
        timeBox.setRange(0, 240)
        timeBox.setValue(120)
        frequencyBox = QSpinBox()
        frequencyBox.setValue(5)
        axisBox = QComboBox()
        axisBox.addItems(["X", "Y", "Z"])
        speedBox = QSpinBox()
        speedBox.setRange(1, 20)
        numRows = QSpinBox()
        spinButton = QPushButton("Animate Petals Spin")

        # Blooming Button
        animateButton = QPushButton("Animate Blooming")
        animateButton.clicked.connect(lambda: FlowerMain.StepThree(nameText.text(), frequencyBox.value(), timeBox.value(),
                                                                   axisBox.currentText(), 0, speedBox.value()))

        # Spin Button
        spinButton.clicked.connect(lambda: FlowerMain.spinFlowerForFlower(nameText.text(), numRows.value()))

        # Clear Button
        clearButton = QPushButton("Clear Keyframes")
        clearButton.clicked.connect(lambda: FlowerMain.clearKeyFramesForFlower(nameText.text(), timeBox.value()))

        # Organising layout of UI
        # Variables
        layout.addWidget(spinTextTitle,0 ,0)
        layout.addWidget(nameText, 0,1)
        layout.addWidget(timeTitle, 1,0)
        layout.addWidget(timeBox, 1,1)
        layout.addWidget(frequencyTitle, 2,0)
        layout.addWidget(frequencyBox, 2,1)
        layout.addWidget(axisTitle, 3,0)
        layout.addWidget(axisBox, 3,1)
        layout.addWidget(speedTitle,4,0)
        layout.addWidget(speedBox, 4,1)
        layout.addWidget(numRowsTitle ,5,0)
        layout.addWidget(numRows,5,1)

        # Buttons
        layout.addWidget(bloomInstructions,6,0,1,2)
        layout.addWidget(animateButton,7,0,1,2)

        layout.addWidget(spinInstructions,8,0,1,2)
        layout.addWidget(spinButton,9,0,1,2)

        layout.addWidget(clearInstructions, 10,0,1,2)
        layout.addWidget(clearButton, 11,0,1,2)

        return layout


""" This is the Main UI Window for the Tool. Will have 3 tabs with all the capabilities of tool """


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
        self.setLayout(QGridLayout())

        # Create a tab for each category of functionality
        tab01 = ExampleTab("layout01")
        tab02 = ExampleTab("layout02")
        tab03 = ExampleTab("layout03")

        # Add all the tabs
        self.addTab(tab01, TAB01_TITLE)
        self.addTab(tab02, TAB02_TITLE)
        self.addTab(tab03, TAB03_TITLE)

        self.show()


def main():
    MainWindow()
