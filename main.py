from PyQt6.QtWidgets import QApplication, QWidget,QMainWindow
from PianoWidget1 import PianoWidget1
from Piano_graphic_user_interface import piano_GUI


if __name__ == '__main__':
    import sys
    global app # Use global to prevent crashing on exit
    app = QApplication(sys.argv)
    # piano = PianoWidget1()# an instance from pianowidet
    # MainWindow =QMainWindow()
    # piano.setupUi(MainWindow)
    # #Gui.draw_keys(MainWindow)
    gui=piano_GUI(500)
    #gui.init_window()
    gui.show()
    #Gui.play_sound('h4')
    #Gui.play_sound('d4')
    sys.exit(app.exec())
 
     
    
 