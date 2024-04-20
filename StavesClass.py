from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsLineItem

class Staves(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.draw_staves()

    def draw_staves(self):
        # painter.setPen(Qt.PenStyle.SolidLine)
        # painter.setBrush(Qt.GlobalColor.black)
        # painter.drawLine(self.line())
        line1 = QGraphicsLineItem(0, 0, 700, 0)   # First line
        line2 = QGraphicsLineItem(0, 20, 700, 20)  # Second line
        line3 = QGraphicsLineItem(0, 40, 700, 40)  # Third line
        line4 = QGraphicsLineItem(0, 60, 700, 60)  # Fourth line
        line5 = QGraphicsLineItem(0, 80, 700, 80)  # Fifth line

        self.scene.addItem(line1)
        self.scene.addItem(line2)
        self.scene.addItem(line3)
        self.scene.addItem(line4)
        self.scene.addItem(line5)

    
    def draw_notes(self,**note_shape):
        pass

    def draw_clef(self,clef):
        pass

    def draw_time_signiture(self,**time_signiture):
        pass

    def change_time_signiture(self,**time_signiture):
        pass

    def reset_position(self,position):
        pass

    def get_name(self,*name):
        pass

    def get_lenght(self):
        pass

    def get_position(self,position):
        pass

    def is_sharp(self,sharp):
        pass

    