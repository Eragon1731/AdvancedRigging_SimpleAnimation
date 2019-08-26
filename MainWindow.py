import ImportFlower
reload(ImportFlower)
import FlowerAnimation
reload(FlowerAnimation)
from Flower import Flower
import os

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
TAB02_TITLE = "Animation Attributes"
TAB03_TITLE = "Edit Animation"


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
        bulbTitle = QLabel(self)
        bulbTitle.setText('Bulb Name:')
        bulbNameBox = QLineEdit(self)
        bulbNameBox.setText('lotus_bulb')

        petalTitle = QLabel(self)
        petalTitle.setText('Petal Name:')
        petalNameBox = QLineEdit(self)
        petalNameBox.setText('lotus_petal')

        pybutton = QPushButton('Load', self)
        pybutton.clicked.connect(lambda: self.on_click_button(bulbNameBox.text()))
        pybutton.clicked.connect(lambda: self.on_click_button(petalNameBox.text()))

        layout.addWidget(bulbTitle)
        layout.addWidget(bulbNameBox)
        layout.addWidget(petalTitle)
        layout.addWidget(petalNameBox)
        layout.addWidget(pybutton)

        return layout

    '''create a default flower with default animation'''
    def layout02(self):
        layout = QVBoxLayout()

        petalTitle = QLabel()
        baseTitle = QLabel()
        petalTitle.setText("Assign Petal Rows")
        baseTitle.setText("Assign Base Petals")

        # Use second tab to edit Flower Attrs
        petalRows = QSpinBox()
        basePetals = QSpinBox()

        button = QPushButton()
        button.setText("Ok")

        button.clicked.connect(lambda: self.on_click_button(petalRows.value()))
        button.clicked.connect(lambda: self.on_click_button(basePetals.value()))

        #Create animation for the flower
        timeTitle = QLabel()
        timeTitle.setText("Animation Time Length")
        frequencyTitle = QLabel()
        frequencyTitle.setText("Keyframe frequency within Time Limit: ")
        axisTitle = QLabel()
        axisTitle.setText("Which axis to animate on: ")
        speedTitle = QLabel()
        speedTitle.setText("Speed of Animation: ")

        timeBox = QSpinBox()
        timeBox.setRange(0, 240)
        timeBox.setValue(120)
        frequencyBox = QLineEdit()
        frequencyBox.setValidator(QIntValidator())
        axisBox = QComboBox()
        axisBox.addItems(["X", "Y", "Z"])
        speedBox = QSpinBox()
        speedBox.setRange(1, 20)


        animateButton = QPushButton()
        animateButton.setText("Animate the Flower")

        layout.addWidget(petalTitle)
        layout.addWidget(petalRows)
        layout.addWidget(baseTitle)
        layout.addWidget(basePetals)
        layout.addWidget(button)

        layout.addWidget(timeTitle)
        layout.addWidget(timeBox)
        layout.addWidget(frequencyTitle)
        layout.addWidget(frequencyBox)
        layout.addWidget(axisTitle)
        layout.addWidget(axisBox)
        layout.addWidget(speedTitle)
        layout.addWidget(speedBox)
        layout.addWidget(animateButton)

        return layout

    def layout03(self):
        layout = QVBoxLayout()

        # All edits that can be made on a flower
        runButton = QPushButton()
        runButton.setText("Clear Keyframes")
        runButton.clicked.connect(lambda: self.edit_assets(runButton.text()))

        spinButton = QPushButton()
        spinButton.setText("Spin the Flower")

        # Moves flower according to locator attached to bulb
        relocateButton = QPushButton()
        relocateButton.setText("Update Flower Assets")

        layout.addWidget(runButton)
        layout.addWidget(spinButton)
        layout.addWidget(relocateButton)

        return layout

    # Test functions
    def edit_assets(self,val):
        print "FlowerAnimation.%s" %(val)

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
