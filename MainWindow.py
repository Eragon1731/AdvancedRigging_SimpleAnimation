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
        layout = QGridLayout()
        regex = QRegExp("[a-z-A-Z_]+")
        validator = QRegExpValidator(regex)

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
        nameValue.setValidator(validator)
        petalName = QLineEdit("lotus_petal")
        petalName.setValidator(validator)
        bulbName = QLineEdit("lotus_bulb_loc")
        bulbName.setValidator(validator)

        button = QPushButton("Ok")

        button.clicked.connect(lambda: FlowerMain.StepTwo(nameValue.text(), petalName.text(),
                                                bulbName.text(), petalRows.value(), basePetals.value()))

        # Add widgets to layout
        layout.addWidget(nameTitle, 0,0)
        layout.addWidget(nameValue, 0,1)
        layout.addWidget(petalTitle, 1,0)
        layout.addWidget(petalName, 1,1)
        layout.addWidget(bulbTitle, 2,0)
        layout.addWidget(bulbName, 2,1)
        layout.addWidget(rowsTitle, 3,0)
        layout.addWidget(petalRows,3,1 )
        layout.addWidget(baseTitle , 4,0)
        layout.addWidget(basePetals, 4,1)

        layout.addWidget(button,5,0,1,2)

        return layout

    def layout03(self):
        layout = QGridLayout()
        intValidator = QIntValidator()
        regex = QRegExp("[a-z-A-Z_]+")
        validator = QRegExpValidator(regex)

        # Default animation for flower
        timeTitle = QLabel("Animation Time Length")
        frequencyTitle = QLabel("Keyframe frequency within Time Limit: ")
        axisTitle = QLabel("Which axis to animate on: ")
        speedTitle = QLabel("Speed of Animation: ")
        animateInstructions = QLabel("Select the ctrl group(s) you want to animate with")

        spinTextTitle = QLabel("Name of flower to animate/edit")
        nameText = QLineEdit()
        nameText.setValidator(validator)

        timeBox = QSpinBox()
        timeBox.setRange(0, 240)
        timeBox.setValue(120)
        frequencyBox = QLineEdit()

        frequencyBox.setValidator(intValidator)

        axisBox = QComboBox()
        axisBox.addItems(["X", "Y", "Z"])
        speedBox = QSpinBox()
        speedBox.setRange(1, 20)

        animateButton = QPushButton("Animate Blooming")
        animateButton.clicked.connect(lambda: FlowerMain.StepThree(nameText.text(), int(frequencyBox.text()), timeBox.value(),
                                                                   axisBox.currentText(), 1, 0.5))

        numRowsTitle = QLabel("Which row num do you want to spin: ")
        numRows = QLineEdit()
        numRows.setValidator(intValidator)
        spinButton = QPushButton("Animate Petals Spin")
        spinButton.clicked.connect(lambda: FlowerMain.spinFlowerForFlower(nameText.text(), int(numRows.text())))

        # All edits that can be made on a flower
        clearButton = QPushButton("Clear Keyframes")
        clearButton.clicked.connect(lambda: FlowerMain.clearKeyFramesForFlower(nameText.text(), timeBox.value()))

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
        layout.addWidget(animateInstructions,5,0,1,2)
        layout.addWidget(animateButton,6,0,1,2)

        layout.addWidget(numRowsTitle)
        layout.addWidget(numRows)

        layout.addWidget(spinButton)

        layout.addWidget(clearButton)

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
