from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from PyQt6.QtCore import QTimer
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl

class Metronome(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.time_signature = '4/4'  # Default time signature
        self.beat_count = 0
        self.init_ui()
        self.is_metronome_on = False
        self.metronome_timer = QTimer()
        self.click_sound = QSoundEffect()
        self.click_sound.setSource(QUrl.fromLocalFile("click.wav"))

    def init_ui(self):
        self.time_signature_label = QLabel(self.time_signature, self)
        self.time_signature_label.setStyleSheet("font-size: 18pt; font-weight: bold;")

        self.metronome_button = QPushButton("Metronome Off", self)
        self.metronome_button.setStyleSheet("background-color: red;")
        self.metronome_button.clicked.connect(self.toggle_metronome)

        self.time_signature_4_4_button = QPushButton("4/4", self)
        self.time_signature_4_4_button.clicked.connect(lambda: self.change_time_signature('4/4'))

        self.time_signature_3_4_button = QPushButton("3/4", self)
        self.time_signature_3_4_button.clicked.connect(lambda: self.change_time_signature('3/4'))

        time_signature_layout = QHBoxLayout()
        time_signature_layout.addWidget(self.time_signature_4_4_button)
        time_signature_layout.addWidget(self.time_signature_3_4_button)

        layout = QVBoxLayout()
        layout.addWidget(self.time_signature_label)
        layout.addLayout(time_signature_layout)
        layout.addWidget(self.metronome_button)
        self.setLayout(layout)

    def toggle_metronome(self):
        if self.is_metronome_on:
            self.metronome_button.setText("Metronome Off")
            self.metronome_button.setStyleSheet("background-color: red;")
            self.metronome_timer.stop()
            self.beat_count = 0
        else:
            self.metronome_button.setText("Metronome On")
            self.metronome_button.setStyleSheet("background-color: green;")
            self.metronome_timer.timeout.connect(self.play_click)
            self.set_interval()
            self.metronome_timer.start()

        self.is_metronome_on = not self.is_metronome_on

    def set_interval(self):
        if self.time_signature == '4/4':
            self.metronome_timer.setInterval(1000)  # Set interval to 1000ms for 4/4
        elif self.time_signature == '3/4':
            self.metronome_timer.setInterval(750)  # Set interval to 750ms for 3/4

    def change_time_signature(self, signature):
        self.time_signature = signature
        self.time_signature_label.setText(self.time_signature)
        if self.is_metronome_on:
            self.set_interval()
            self.metronome_timer.start()

    def play_click(self):
        if self.click_sound.isLoaded():
            self.click_sound.play()
            self.beat_count += 1
            if (self.time_signature == '4/4' and self.beat_count >= 4) or \
               (self.time_signature == '3/4' and self.beat_count >= 3):
                self.beat_count = 0
        else:
            print("Sound file not loaded.")
