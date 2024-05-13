 from PyQt6.QtWidgets import QApplication, QWidget,QMainWindow
from PianoWidget1 import PianoWidget1
from Piano_graphic_user_interface import piano_GUI
 

if __name__ == '__main__':
    import sys
    global app # Use global to prevent crashing on exit
    app = QApplication(sys.argv)
    gui=piano_GUI(400)
    gui.show()
    sys.exit(app.exec())
 
     
    
 
