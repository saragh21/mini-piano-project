from PyQt6.QtWidgets import QWidget,QMainWindow,QMenuBar,QHBoxLayout,QGraphicsScene,QGraphicsView,QGridLayout,QLabel
from PianoWidget1 import PianoWidget1
from StavesClass import Staves

class piano_GUI(QMainWindow):
    def __init__(self, size):
        super().__init__()
        self.size=size
        self.setCentralWidget(QWidget()) # QMainWindown must have a centralWidget to be able to add layouts
        self.grid = QGridLayout() # Grid main layout
        self.centralWidget().setLayout(self.grid)
        self.init_window()
        self.init_staves()

    def save(self):
        pass

    def load(self):
        pass

    def init_window(self):
        """
        Sets up the window.
    
        """

        # Instantiate PianoWidget1
        self.pianoWidget = PianoWidget1()
        pianoWindow = QMainWindow()  # Create a new QMainWindow for PianoWidget1
        self.pianoWidget.retranslateUi(self.pianoWidget) # Set the keyboard shortcuts
        self.pianoWidget.setupUi(pianoWindow)  # Setup the UI of PianoWidget1 inside this QMainWindow
        self.setGeometry(700, 700, 700, 700)
        self.setWindowTitle('minipiano')
        # self.show()
         
        # stavesWindow = QMainWindow()  # Create a new QMainWindow for PianoWidget1
        # self.Stavesclass.setupUi(stavesWindow)  # Setup the UI of PianoWidget1 inside this QMainWindow
        # self.setGeometry(700, 700, 700, 700)
        # self.setWindowTitle('staves')
        # # Add a scene for drawing 2d objects
        # self.scene = QGraphicsScene()
        # self.scene.setSceneRect(0, 0, 700, 700)

        # # Add a view for showing the scene
        # self.view =QGraphicsView(self.scene, self)
        # self.view.adjustSize()
        # self.view.show()
        
        # Create the four layouts
        self.topLeftLayout = QHBoxLayout()
        self.topRightLayout = QHBoxLayout()
        self.bottomLeftLayout = QHBoxLayout()
        self.bottomRightLayout = QHBoxLayout()

        # Add the layouts to the grid
        self.grid.addLayout(self.topLeftLayout, 0, 0)
        self.grid.addLayout(self.topRightLayout, 0, 1)
        self.grid.addLayout(self.bottomLeftLayout, 1, 0)
        self.grid.addLayout(self.bottomRightLayout, 1, 1)

        # Add the view to the bottom right layout
        # self.bottomRightLayout.addWidget(self.view)

         # Add widgets to the other layouts and set their sizes
        self.topLeftWidget = QLabel("metronome", self)
        self.topLeftWidget.setFixedSize(100, 350)
        self.topLeftLayout.addWidget(self.topLeftWidget)

        self.topRightWidget = QLabel("staves", self)
        self.topRightWidget.setFixedSize(600, 350)
        self.topRightLayout.addWidget(self.topRightWidget)

        self.bottomLeftWidget = QLabel("soundEffects", self)
        self.bottomLeftWidget.setFixedSize(100, 350)
        self.bottomLeftLayout.addWidget(self.bottomLeftWidget)
 
        self.bottomRightWidget = QLabel("piano", self)
        self.bottomRightWidget.setFixedSize(700, 350)
        self.bottomRightLayout.addWidget(self.bottomRightWidget)


        # Add the piano widget and staves to the right layouts
        self.grid.addWidget(pianoWindow, 1, 1)  # Add it to the grid layout at position (1, 1)
         
         
        
        # Show the window
        self.show()
 
    def init_staves(self):
        # Instantiate Staves
        self.staves = Staves()
        self.grid.addWidget(self.staves, 0, 1)  # Add it to the top right layout
        self.show()