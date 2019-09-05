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
        layout = QGridLayout()

        #Load the flower parts: Allow users to add their flower parts to the list
        bulbTitle = QLabel("Bulb Name:")
        bulbNameBox = QLineEdit("lotus_bulb")
        petalTitle = QLabel("Petal Name:")
        petalNameBox = QLineEdit("lotus_petal")

        pybutton = QPushButton("Load")
        pybutton.clicked.connect(lambda: FlowerMain.StepOne(bulbNameBox.text(), petalNameBox.text()))

        layout.addWidget(bulbTitle,0,0)
        layout.addWidget(bulbNameBox,0,1)
        layout.addWidget(petalTitle,1,0)
        layout.addWidget(petalNameBox,1,1)
        layout.addWidget(pybutton, 2, 0, 1, 2)

        return layout

    '''create a default flower with default animation'''
    def layout02(self):
        layout = QVBoxLayout()

        rowsTitle = QLabel("Assign Petal Rows")
        baseTitle = QLabel("Assign Base Petals")
        nameTitle = QLabel("Name the flower")
        petalTitle = QLabel("Petal Anim Model Name")
        bulbTitle = QLabel("Bulb Center Locator Name")

        # Use second tab to edit Flower Attrs
        petalRows = QSpinBox()
        petalRows.setValue(3)
        basePetals = QSpinBox()
        basePetals.setValue(3)
        nameValue = QLineEdit()
        petalName = QLineEdit("lotus_petal")
        bulbName = QLineEdit("lotus_bulb_loc")

        button = QPushButton("Ok")

        button.clicked.connect(lambda: FlowerMain.StepTwo(nameValue.text(), petalName.text(),
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
        intValidator = QIntValidator()

        # Default animation for flower
        timeTitle = QLabel("Animation Time Length")
        frequencyTitle = QLabel("Keyframe frequency within Time Limit: ")
        axisTitle = QLabel("Which axis to animate on: ")
        speedTitle = QLabel("Speed of Animation: ")

        timeBox = QSpinBox()
        timeBox.setRange(0, 240)
        timeBox.setValue(120)
        frequencyBox = QLineEdit()

        frequencyBox.setValidator(intValidator)

        axisBox = QComboBox()
        axisBox.addItems(["X", "Y", "Z"])
        speedBox = QSpinBox()
        speedBox.setRange(1, 20)

        animateInstructions = QLabel("Select the ctrl group(s) you want to animate with")
        animateButton = QPushButton("Animate the Flower Blooming")
        animateButton.clicked.connect(lambda: FlowerMain.StepThree(int(frequencyBox.text()), timeBox.value(),
                                                                   axisBox.currentText(), 1, 0.5))

        # All edits that can be made on a flower
        clearButton = QPushButton("Clear Keyframes")
        clearTextTitle = QLabel("Name of flower to clear keyframes on")
        clearText = QLineEdit()
        clearButton.clicked.connect(lambda: FlowerMain.clearKeyFramesForFlower(clearText.text(), timeBox.value()))

        numRowsTitle = QLabel("Which row num do you want to spin: ")
        numRows = QLineEdit()
        numRows.setValidator(intValidator)
        spinButton = QPushButton("Spin the Flower")
        spinTextTitle = QLabel("Name of flower to spin")
        spinText = QLineEdit()
        spinButton.clicked.connect(lambda: FlowerMain.spinFlowerForFlower(spinText.text(), int(numRows.text())))

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

        layout.addWidget(clearTextTitle)
        layout.addWidget(clearText)
        layout.addWidget(clearButton)

        layout.addWidget(numRowsTitle)
        layout.addWidget(numRows)
        layout.addWidget(spinTextTitle)
        layout.addWidget(spinText)
        layout.addWidget(spinButton)

        return layout


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
