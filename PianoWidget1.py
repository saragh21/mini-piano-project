 from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QThread
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl, pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget
from StavesClass import Staves


class PianoWidget1(QWidget):
	notePlayed = pyqtSignal(str)  # Signal to be emitted when a note is played
	def __init__(self,staves, parent=None):
			super().__init__(parent)
			self.staves = Staves()
            
	def setupUi(self, MainWindow):

		MainWindow.setObjectName("MainWindow")
		#MainWindow.resize(659, 181)
         

		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		MainWindow.setCentralWidget(self.centralwidget)
		 

		self.keys = {
            'c4': (20, 30, 41, 181, 'white'),
            'd4': (60, 30, 41, 181, 'white'),
            'c40': (40, 30, 31, 111, 'black'),
            'e4': (100, 30, 41, 181, 'white'),
			'd40': (80, 30, 31, 111, 'black'),
            "f4": (140, 30,41, 181, 'white'),
            "g4": (180, 30,41, 181, 'white'),
            "a4": (220, 30,41, 181, 'white'),
            "b4": (260, 30,41, 181, 'white'), 
            "c5": (300, 30,41, 181, 'white'), 
            "d5": (340, 30,41, 181, 'white'), 
            "a5": (500, 30,41, 181, 'white'), 
            "e5": (380, 30,41, 181, 'white'), 
            "g5": (460, 30,41, 181, 'white'), 
            "f5": (420, 30,41, 181, 'white'), 
            "b5": (540, 30,41, 181, 'white'), 
            "c6": (580, 30,41, 181, 'white'), 
            "f40": (160, 30, 31, 111, 'black'), 
			"g40":(200, 30, 31, 111, 'black'),   
            "a40": (240, 30, 31, 111, 'black'), 
            "c50": (320, 30, 31, 111, 'black'), 
            "d50": (360, 30, 31, 111, 'black'), 
            "f50":(440, 30, 31, 111, 'black'),  
            "g50":(480, 30, 31, 111, 'black'),  
            "a50":  (520, 30, 31, 111, 'black'),
		
        }
		self.shortcuts = {
            'c4': 'A', 'd4': 'S', 'c40': 'Q', 'd40': 'W', 'e4': 'D', 'f4': 'F', 'g4': 'G', 'a4': 'H', 'b4': 'J',
            'c5': 'K', 'd5': 'L', 'a5': 'V', 'e5': 'Z', 'g5': 'C', 'f5': 'X', 'b5': 'B', 'c6': 'N', 'f40': 'E',
            'g40': 'R', 'a40': 'T', 'c50': 'Y', 'd50': 'U', 'f50': 'I', 'g50': 'O', 'a50': 'P'
        }

		for key, params in self.keys.items():
			x, y, w, h, color = params
			button = self.create_key((x, y), (w, h), color)
			setattr(self, key, button)	
			
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)


		self.key_sounds = {
            'c4': QSoundEffect(),
            'd4': QSoundEffect(),
			'c40': QSoundEffect(),
    		'e4': QSoundEffect(),
			'd40': QSoundEffect(),
			'f4': QSoundEffect(),
			'g4': QSoundEffect(),
			'a4': QSoundEffect(),
			'b4': QSoundEffect(),
			'c5': QSoundEffect(),
			'd5': QSoundEffect(),
			'e5': QSoundEffect(),
			'f5': QSoundEffect(),
			'g5': QSoundEffect(),
			'a5': QSoundEffect(),
			'b5': QSoundEffect(),
			'c6': QSoundEffect(),
			'f40': QSoundEffect(),
			'g40': QSoundEffect(),
			'a40': QSoundEffect(),
			'c50': QSoundEffect(),
			'd50': QSoundEffect(),
			'f50': QSoundEffect(),
			'g50': QSoundEffect(),
			'a50': QSoundEffect(),
		}
		print(self.key_sounds['c4'].status())
		for key_name in self.key_sounds:
			self.key_sounds[key_name].setSource(QUrl.fromLocalFile(f'Sounds/{key_name}.wav'))
        
	
		for key in self.keys:
			getattr(self, key).raise_()
			getattr(self, key).pressed.connect(lambda key=key: self.key_pressed(key))
			getattr(self, key).released.connect(lambda key=key: self.key_released(key))
			#self.play_sound('c4')
			getattr(self, key).clicked.connect(lambda checked=False,key=key: self.key_clicked(key)) 
         
	def create_key(self, pos, size, color):
			key = QtWidgets.QPushButton(self.centralwidget)
			key.setGeometry(QtCore.QRect(*pos, *size))
			key.setStyleSheet(self.get_stylesheet(color))
			key.setText("")
			return key
	 
	def get_stylesheet(self, color):
		if color == 'white':
			return """QPushButton {
				background-color: rgb(242, 242, 242);
				background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
			}
			QPushButton:pressed {
				background-color: rgb(250, 250, 250);
			}"""
		else:
			return """QPushButton {
				background-color: rgb(0, 0, 0);
				background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));
			}
			QPushButton:pressed {
				background-color: rgb(0, 0, 0);
				background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));
			}"""
 
	def play_sound(self, key):
		 
		print(f"play_sound called with key: {key}")
		if key in self.key_sounds:
			self.key_sounds[key].play()
		if key not in self.key_sounds:
			raise KeyError(f"Invalid key: {key}")	 
			
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "minipiano"))
		for key_name, shortcut in self.shortcuts.items():
			getattr(self, key_name).setShortcut(_translate("MainWindow", shortcut))
		 
	def change_color(self, key_name, color):
		button = getattr(self, key_name)
		if color == 'blue':
			button.setStyleSheet("""QPushButton {
            background-color: rgb(173, 216, 230);  # This is a light blue color
            ...
        }""")
		elif color == 'white':
			button.setStyleSheet("""QPushButton {
				background-color: rgb(242, 242, 242);
				background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
			}
			QPushButton:pressed {
				background-color: rgb(250, 250, 250);
			}""")
		elif color == 'black':
			button.setStyleSheet("""QPushButton {
				background-color: rgb(0, 0, 0);
				background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));
			}
			QPushButton:pressed {
				background-color: rgb(0, 0, 0);
				background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));
			}""")
       
	def key_pressed(self, key_name):
		self.change_color(key_name, 'blue')  # Change the color to blue when the key is pressed

	def key_released(self, key_name):
		color = 'white' if '0' not in key_name else 'black'  # Determine the original color based on the key name
		self.change_color(key_name, color)  # Change the color back to the original color when the key is released

	def key_clicked(self, key):
        # Play the sound
		self.play_sound(key)   
        # Call the method to add the quarter note to the staves
		self.notePlayed.emit(key)
	
	def on_key_pressed(self, key):
		self.staves.add_quarter_note(key)

	
	 


     
 

