 from PyQt6.QtWidgets import QFileDialog,QMenu, QComboBox, QWidget, QMainWindow, QMenuBar, QHBoxLayout, QGraphicsView, QGridLayout, QLabel
from PianoWidget1 import PianoWidget1
from StavesClass import Staves
from Metronome import Metronome
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
 

class piano_GUI(QMainWindow):
    def __init__(self, size):
        super().__init__()
        self.size = size
        self.setCentralWidget(QWidget())  # QMainWindow must have a centralWidget to be able to add layouts
        self.grid = QGridLayout()  # Grid main layout
        self.centralWidget().setLayout(self.grid)
        self.init_window()

    def init_window(self):
        """
        Sets up the window.
    
        """
        # Create a menu bar
        menu_bar = self.menuBar()
        # Instantiate the Metronome, PianoWidget1, and Staves
        self.metronome = Metronome()
        self.staves = Staves()
        self.pianoWidget = PianoWidget1(self.staves)
        pianoWindow = QMainWindow()
        self.pianoWidget.notePlayed.connect(self.staves.add_quarter_note)
         
        self.pianoWidget.setupUi(pianoWindow)  # Setup the UI of PianoWidget1 inside this QMainWindow
        self.setGeometry(100, 100, 800, 600) 
        self.setWindowTitle('minipiano')

        time_signature_menu = QMenu("Time Signature", self)
        menu_bar.addMenu(time_signature_menu)

        save_action = QAction("Save Notes", self)
        save_action.triggered.connect(self.save_notes)
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction(save_action)

        # Create actions for 4/4 and 3/4 time signatures
        time_signature_4_4_action = QAction("4/4", self)
        time_signature_3_4_action = QAction("3/4", self)

        # Add actions to the time signature menu
        time_signature_menu.addAction(time_signature_4_4_action)
        time_signature_menu.addAction(time_signature_3_4_action)

         # Connect actions to the method that changes the time signature
        time_signature_4_4_action.triggered.connect(lambda: self.change_time_signature('4/4'))
        time_signature_3_4_action.triggered.connect(lambda: self.change_time_signature('3/4'))
        
         # Create the four layouts
        self.topLeftLayout = QHBoxLayout()
        self.topRightLayout = QHBoxLayout()
        self.bottomLeftLayout = QHBoxLayout()
        self.bottomRightLayout = QHBoxLayout()


        # Set the fixed sizes for the widgets  
        metronome_size = (200, 300)  
        piano_and_staves_size = (600, 300)   

        self.metronome.setFixedSize(*metronome_size)
        self.pianoWidget.setFixedSize(*piano_and_staves_size)
        self.stavesView = QGraphicsView(self.staves, self)
        self.stavesView.setFixedSize(*piano_and_staves_size)
        
        #self.stavesView.fitInView(self.staves.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)  # Fit the view to the scene
        # Add the widgets to the corresponding layouts
        self.topLeftLayout.addWidget(self.metronome)
        self.topRightLayout.addWidget(self.stavesView)
        self.bottomRightLayout.addWidget(self.pianoWidget)
        self.stavesView.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        # Add the layouts to the grid
        self.grid.addLayout(self.topLeftLayout, 0, 0)
        self.grid.addLayout(self.topRightLayout, 0, 1)
        self.grid.addLayout(self.bottomLeftLayout, 1, 0)
        self.grid.addLayout(self.bottomRightLayout, 1, 1)
         
        self.bottomRightLayout.addWidget(self.pianoWidget)  # Add the piano widget directly

        # Add the piano widget to the right layout
        self.grid.addWidget(pianoWindow, 1, 1)  # Add it to the grid layout at position (1, 1)
        # Connect the notePlayed signal to the updateView slot
        #self.pianoWidget.notePlayed.connect(self.updateView)
        self.show()

    def change_time_signature(self, signature):
        self.staves.set_time_signature(signature)
        
    def save_notes(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Notes", "",
                                                "Text Files (*.txt);;All Files (*)")
        if fileName:
            with open(fileName, 'w') as file:
                for note in self.notes:
                    file.write(f"{note}\n")
                file.flush()
            print(f"Notes saved to {fileName}")
    def updateView(self, key):
        print(f"Note played: {key}, updating view.")

        # Print the scene rect and viewport rect
        scene_rect = self.staves.sceneRect()
        

