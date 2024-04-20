
import unittest
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QMainWindow,QApplication
from PianoWidget1 import PianoWidget1  
import sys

class TestUi_MainWindow(unittest.TestCase):
    def setUp(self):
        
        self.ui = PianoWidget1()
        app=QApplication(sys.argv)
        mainwindow= QMainWindow()
        self.ui.setupUi(mainwindow)
        #print('hello')   

    def test_invalid_sound_path(self):
        # Test that an invalid sound path raises an exception
        #  with self.assertRaises(QSoundEffect.Error):
        #     self.ui.key_sounds['c4'].setSource(QUrl.fromLocalFile('invalid_path.wav'))
        #     self.ui.key_sounds['c4'].pla 
 
        self.ui.key_sounds['c4'].setSource(QUrl.fromLocalFile('invalid_path.wav'))

        # Check if an error occurred
        self.assertEqual(self.ui.key_sounds['c4'].error(), QSoundEffect.Error.ResourceError)

    def test_invalid_note_name(self):
        # Test that an invalid note name raises an exception
        print('invalid name')
        #with self.assertRaises(KeyError):
            #self.ui.play_sound('c4')  # 'H' is not a valid note name
        #self.assertEqual('c4',self.ui.key_sounds['c4'])
         
        keyname="h4"
        self.assertTrue(True if keyname in self.ui.key_sounds.keys() else False,"key name is invalid")
         

if __name__ == '__main__':
    unittest.main()
