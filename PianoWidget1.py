from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QThread
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QWidget


class PianoWidget1(QWidget):
	def setupUi(self, MainWindow):

		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(659, 251)
         

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
			setattr(self, key, self.create_key((x, y), (w, h), color))


         
	   
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		self.key_sounds = {
            'c4': QSoundEffect(),
            'd4': QSoundEffect(),
    		'e4': QSoundEffect(),
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
            # Add the rest of your keys here
        }
		 
		self.key_sounds['c4'].setSource(QUrl.fromLocalFile('Sounds/c4.wav'))
		self.key_sounds['d4'].setSource(QUrl.fromLocalFile('Sounds/d4.wav'))
		self.key_sounds['e4'].setSource(QUrl.fromLocalFile('Sounds/e4.wav'))
		self.key_sounds['f4'].setSource(QUrl.fromLocalFile('Sounds/f4.wav'))
		self.key_sounds['g4'].setSource(QUrl.fromLocalFile('Sounds/g4.wav'))
		self.key_sounds['a4'].setSource(QUrl.fromLocalFile('Sounds/a4.wav'))
		self.key_sounds['b4'].setSource(QUrl.fromLocalFile('Sounds/b4.wav'))
		self.key_sounds['c5'].setSource(QUrl.fromLocalFile('Sounds/c5.wav'))
		self.key_sounds['d5'].setSource(QUrl.fromLocalFile('Sounds/d5.wav'))
		self.key_sounds['e5'].setSource(QUrl.fromLocalFile('Sounds/e5.wav'))
		self.key_sounds['f5'].setSource(QUrl.fromLocalFile('Sounds/f5.wav'))
		self.key_sounds['g5'].setSource(QUrl.fromLocalFile('Sounds/g5.wav'))
		self.key_sounds['a5'].setSource(QUrl.fromLocalFile('Sounds/a5.wav'))
		self.key_sounds['b5'].setSource(QUrl.fromLocalFile('Sounds/b5.wav'))
		self.key_sounds['c6'].setSource(QUrl.fromLocalFile('Sounds/c6.wav'))

		self.c4.raise_()
		self.d4.raise_()
		self.c40.raise_()
		self.e4.raise_()
		self.f4.raise_()
		self.d40.raise_()
		self.g4.raise_()
		self.a4.raise_()
		self.b4.raise_()
		self.c5.raise_()
		self.d5.raise_()
		self.a5.raise_()
		self.e5.raise_()
		self.g5.raise_()
		self.f5.raise_()
		self.b5.raise_()
		self.c6.raise_()
		self.f40.raise_()
		self.g40.raise_()
		self.a40.raise_()
		self.c50.raise_()
		self.d50.raise_()
		self.f50.raise_()
		self.g50.raise_()
		self.a50.raise_()

			# # Connect the button press event to the play_sound function
		self.c4.clicked.connect(lambda: self.play_sound('c4'))
		self.d4.clicked.connect(lambda: self.play_sound('d4')) 
		self.e4.clicked.connect(lambda: self.play_sound('e4'))
		self.f4.clicked.connect(lambda: self.play_sound('f4'))
		self.g4.clicked.connect(lambda: self.play_sound('g4'))
		self.a4.clicked.connect(lambda: self.play_sound('a4'))
		self.b4.clicked.connect(lambda: self.play_sound('b4'))
		self.c5.clicked.connect(lambda: self.play_sound('c5'))
		self.d5.clicked.connect(lambda: self.play_sound('d5'))
		self.e5.clicked.connect(lambda: self.play_sound('e5'))
		self.f5.clicked.connect(lambda: self.play_sound('f5'))
		self.g5.clicked.connect(lambda: self.play_sound('g5'))
		self.a5.clicked.connect(lambda: self.play_sound('a5'))
		self.b5.clicked.connect(lambda: self.play_sound('b5'))
		self.c6.clicked.connect(lambda: self.play_sound('c6'))
		#will do that for ather keys
		
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
	 
		# Define a single function to play the sounds for each key
	def play_sound(self, key_name):
		if key_name in self.key_sounds:
			self.key_sounds[key_name].play()
			
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "minipiano"))
		self.c4.setShortcut(_translate("MainWindow", "A"))
		self.d4.setShortcut(_translate("MainWindow", "S"))
		self.c40.setShortcut(_translate("MainWindow", "Q"))
		self.d40.setShortcut(_translate("MainWindow", "W"))
		self.e4.setShortcut(_translate("MainWindow", "D"))
		self.f4.setShortcut(_translate("MainWindow", "F"))
		self.g4.setShortcut(_translate("MainWindow", "G"))
		self.a4.setShortcut(_translate("MainWindow", "H"))
		self.b4.setShortcut(_translate("MainWindow", "J"))
		self.c5.setShortcut(_translate("MainWindow", "K"))
		self.d5.setShortcut(_translate("MainWindow", "L"))
		self.a5.setShortcut(_translate("MainWindow", "V"))
		self.e5.setShortcut(_translate("MainWindow", "Z"))
		self.g5.setShortcut(_translate("MainWindow", "C"))
		self.f5.setShortcut(_translate("MainWindow", "X"))
		self.b5.setShortcut(_translate("MainWindow", "B"))
		self.c6.setShortcut(_translate("MainWindow", "N"))
		self.f40.setShortcut(_translate("MainWindow", "E"))
		self.g40.setShortcut(_translate("MainWindow", "R"))
		self.a40.setShortcut(_translate("MainWindow", "T"))
		self.c50.setShortcut(_translate("MainWindow", "Y"))
		self.d50.setShortcut(_translate("MainWindow", "U"))
		self.f50.setShortcut(_translate("MainWindow", "I"))
		self.g50.setShortcut(_translate("MainWindow", "O"))
		self.a50.setShortcut(_translate("MainWindow", "P"))

		self.retranslateUi(MainWindow)
	# def change_color(self, key_name, color):
	# 	button = self.buttons[key_name]
	# 	button.setStyleSheet(f"background-color: {color};")

	# 	self.buttons = {
    #         'a50': self.a50,
    #         'c4': self.c4,
    #         'd4': self.d4,
    #         'c40': self.c40,
    #         'e4': self.e4,
    #         'f4': self.f4,
    #         'd40': self.d40,
    #         'g4': self.g4,
    #         'a4': self.a4,
    #         'b4': self.b4,
    #         'c5': self.c5,
    #         'd5': self.d5,
    #         'a5': self.a5,
    #         'e5': self.e5,
    #         'g5': self.g5,
    #         'f5': self.f5,
    #         'b5': self.b5,
	# 	}
	# 	for key, button in self.buttons.items():
	# 		button.clicked.connect(lambda key_name=key: self.play_sound(key_name))
	# 		button.pressed.connect(lambda key_name=key: self.change_color(key_name, 'red'))  # Change color to red when pressed
	# 		button.released.connect(lambda key_name=key: self.change_color(key_name, 'white'))  # Change color back to white when released
 
	# def retranslateUi(self, MainWindow):
	# 		_translate = QtCore.QCoreApplication.translate
	# 		MainWindow.setWindowTitle(_translate("MainWindow", "minipiano"))
	# 		for key in self.keys:
	# 			getattr(self, key).setShortcut(_translate("MainWindow", self.shortcuts[key]))

	def change_color(self, key_name, color):
		button = getattr(self, key_name)
		button.setStyleSheet(f"background-color: {color};")

    # def show_names (self,names):
    #     pass

    # def change_octaves(self,octaves):
    #     pass

    # def stop_sounds(self):
    #     pass

    # def set_volume(self):
    #     pass

    # def set_pitch(self):
    #     pass

    # def get_soundEffects(self):
    #     pass

    # def set_soundEffects(self):
    #     pass
 

