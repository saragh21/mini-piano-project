 
import unittest
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QMainWindow,QApplication
from PianoWidget1 import PianoWidget1
from StavesClass import Staves
from Metronome import Metronome
from Piano_graphic_user_interface import piano_GUI
from unittest.mock import MagicMock
import sys

class TestUi_MainWindow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)
    def setUp(self):
        
        mainwindow= QMainWindow()
        self.staves = Staves()
        self.ui = PianoWidget1(self.staves)
        self.gui=piano_GUI(400)
        self.metronome = Metronome()
        self.ui.updateView = MagicMock()
        self.ui.setupUi(mainwindow)
        #print('hello')   

    def test_invalid_sound_path(self):
 
        # Check if an error occurred
        self.assertNotEqual(self.ui.key_sounds['c4'].status(), QSoundEffect.Status.Ready)


    def test_invalid_note_name(self):
        keyname = "h4"  # Example of an invalid key name
        self.assertFalse(keyname in self.ui.key_sounds, "key name is invalid")

    def test_play_sound_valid_key(self):
        # Assuming 'c4' is a valid key
        try:
            self.ui.play_sound('c4')
        except Exception as e:
            self.fail(f"play_sound('c4') raised {type(e).__name__} unexpectedly!")

    def test_play_sound_invalid_key(self):
        # Assuming 'h4' is an invalid key
        with self.assertRaises(KeyError):
            self.ui.play_sound('h4')

    def test_init_staves(self):
        # Test that the staves are initialized correctly
        self.assertEqual(len(self.staves.stave_lines), 1)
        self.assertEqual(len(self.staves.stave_lines[0]), 5)

    def test_change_time_signature(self):
        # Test that changing the time signature works correctly
        self.metronome.change_time_signature('3/4')
        self.assertEqual(self.metronome.time_signature, '3/4')

    def test_metronome_toggle(self):
        # Test that toggling the metronome updates the is_metronome_on flag
        self.metronome.toggle_metronome()
        self.assertTrue(self.metronome.is_metronome_on)

        self.metronome.toggle_metronome()
        self.assertFalse(self.metronome.is_metronome_on)

    def test_staves_add_note(self):
        # Test that adding a note to the staves works correctly
        self.staves.add_quarter_note('c4')
        self.assertEqual(len(self.staves.notes), 1)
    
    def test_sound_playing(self):
    # Test the sound playing functionality
    # Assuming 'c4' is a valid key
        try:
            self.ui.play_sound('c4')
        except Exception as e:
            self.fail(f"play_sound('c4') raised {type(e).__name__} unexpectedly!")

        # Assuming 'h4' is an invalid key
        with self.assertRaises(KeyError):
            self.ui.play_sound('h4')

    def test_drawing_staves(self):
        # Test the drawing of the staves
        self.assertEqual(len(self.staves.stave_lines), 1)
        self.assertEqual(len(self.staves.stave_lines[0]), 5)

    def test_adding_notes(self):
        # Test the addition of notes to the staves
        # Assuming 'c4' is a valid key
        self.staves.add_quarter_note('c4')
        self.assertEqual(len(self.staves.notes), 1)

        # Assuming 'h4' is an invalid key
        with self.assertRaises(KeyError):
            self.staves.add_quarter_note('h4')

    def test_metronome(self):
        # Test the metronome functionality
        self.metronome.toggle_metronome()
        self.assertTrue(self.metronome.is_metronome_on)

        self.metronome.toggle_metronome()
        self.assertFalse(self.metronome.is_metronome_on)

        self.metronome.change_time_signature('3/4')
        self.assertEqual(self.metronome.time_signature, '3/4')


    def test_updating_view(self):
        # Replace updateView with a mock method
        self.gui.updateView = MagicMock()

        # Do something that should cause updateView to be called...
        self.ui.play_sound('c4')

        # Check if updateView was called
        self.gui.updateView.assert_called_once()

    def test_handling_invalid_inputs(self):
        # Test play_sound with an invalid key
        with self.assertRaises(KeyError):
            self.ui.play_sound('invalid_key')

        # Test add_quarter_note with an invalid key
        with self.assertRaises(KeyError):
            self.staves.add_quarter_note('invalid_key')

    def test_visibility_of_notes(self):
        # Add a note
        self.staves.add_quarter_note('c4')

        # Check if the note has the correct Z-value
        note_head = self.staves.notes[-1]
        self.assertEqual(note_head.zValue(), 1)


if __name__ == '__main__':
    unittest.main()

    suite = unittest.TestSuite()
    suite.addTest(TestUi_MainWindow('test_adding_notes'))  
    runner = unittest.TextTestRunner()
    runner.run(suite)
