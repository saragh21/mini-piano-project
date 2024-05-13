 
from PyQt6.QtWidgets import QGraphicsLineItem, QGraphicsItem, QGraphicsRectItem, QGraphicsScene, QGraphicsEllipseItem, QGraphicsTextItem
from PyQt6.QtGui import QPen, QBrush, QFont
from PyQt6.QtCore import Qt
 

class Staves(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.stave_lines = []
        self.notes = []
        self.time_signature = '4/4'  # Default time signature
        self.time_signature_item = None
        self.note_count = 0  # Initialize note count
        self.current_x_position = 50  # Starting x-position for the first note
        self.stave_length = 700  # Initialize stave length
        self.init_staves()
        self.draw_time_signature()

    def init_staves(self):
        pen = QPen(Qt.GlobalColor.black, 2)
        stave_count = 2  # Number of staves
        lines_per_stave = 5  # Number of lines per stave
        stave_spacing = 15  # Space between each line
        stave_length = 700  # Length of each stave line
        top_margin = 50  # Top margin for the first stave

        for stave_index in range(stave_count):
            stave = []
            for line_index in range(lines_per_stave):
                y = top_margin + stave_index * (lines_per_stave * stave_spacing + top_margin) + line_index * stave_spacing
                line = self.addLine(0, y, stave_length, y, pen)
                stave.append(line)
            self.stave_lines.append(stave)

    def add_quarter_note(self, key):
        # Define the vertical positions for each note on the stave
        note_positions = {
    'c4': self.stave_lines[0][4].line().y1() + 10,  # Below the first line
    'd4': self.stave_lines[0][4].line().y1(),  # On the first line
    'e4': self.stave_lines[0][3].line().y1(),  # On the second line
    'f4': self.stave_lines[0][3].line().y1() - 5,  # Between the second and third lines
    'g4': self.stave_lines[0][2].line().y1(),
            'a4': self.stave_lines[0][2].line().y1() - 5,
            'b4': self.stave_lines[0][1].line().y1(),
            'c5': self.stave_lines[0][1].line().y1() - 5,
            'd5': self.stave_lines[0][0].line().y1(),
            'e5': self.stave_lines[0][0].line().y1() - 5,
            'f5': self.stave_lines[1][4].line().y1(),
            'g5': self.stave_lines[1][4].line().y1() - 5,
            'a5': self.stave_lines[1][3].line().y1(),
            'b5': self.stave_lines[1][3].line().y1() - 5,
            'c6': self.stave_lines[1][2].line().y1(),
            # Define positions for black keys (sharps/flats)
            'c40': self.stave_lines[0][4].line().y1() + 5,
            'd40': self.stave_lines[0][4].line().y1() - 2.5,
            'f40': self.stave_lines[0][3].line().y1() - 2.5,
            'g40': self.stave_lines[0][2].line().y1() + 5,
            'a40': self.stave_lines[0][2].line().y1() - 2.5,
            'c50': self.stave_lines[0][1].line().y1() + 5,
            'd50': self.stave_lines[0][1].line().y1() - 2.5,
            'f50': self.stave_lines[0][0].line().y1() + 5,
            'g50': self.stave_lines[0][0].line().y1() - 2.5,
            'a50': self.stave_lines[1][4].line().y1() - 2.5,
        }
         


        # Use the current x-position for the new note
        x_position = self.current_x_position

         # Initialize y_position to a default value
        y_position = None

        # Check if the key is in the note_positions dictionary
        if key in note_positions:
            y_position = note_positions[key]
        
        # Create the note head (filled ellipse)
            note_head = QGraphicsEllipseItem(x_position, y_position, 10, 10)
            note_head.setBrush(QBrush(Qt.GlobalColor.black))

            # Create the note stem (line)
            stem_height = 35  
            note_stem = QGraphicsLineItem(x_position + 5, y_position, x_position + 5, y_position - stem_height)
            note_stem.setPen(QPen(Qt.GlobalColor.black, 2))

            # Add the note head and stem to the scene
            self.addItem(note_head)
            self.addItem(note_stem)
            # After adding the note head and stem to the scene
            print(note_head.boundingRect())
            print(note_stem.boundingRect())
            note_head.setZValue(1)  # Ensure the note head is drawn above the stave lines
            note_stem.setZValue(1)  # Ensure the note stem is drawn above the stave lines
            
            # Add a sharp symbol if the key is a black key
            if '0' in key:
                sharp = QGraphicsTextItem('#')
                sharp.setPos(x_position - 10, y_position - 20)  # Use x_position instead of note_x
                self.addItem(sharp)

        else:
        # Handle the case where the key is not found
            print(f"Key {key} not found in note positions")
            return  # Exit the function if the key is not valid

        # Increment the x-position for the next note
        self.current_x_position += 20 

        # Scroll the view if the current x-position is beyond the visible area
        views = self.views()
        if views and self.current_x_position > views[0].width():
            views[0].horizontalScrollBar().setValue(views[0].horizontalScrollBar().value() + 20)
        
        # Only print if y_position has been set
        if y_position is not None:
            print(f"Adding note {key} at x: {x_position}, y: {y_position}")

         # Check if we need to extend the stave lines
        if self.current_x_position > self.stave_length:
            self.extend_staves()

        # Check if we need to add a measure line
        self.note_count += 1
        if (self.time_signature == '4/4' and self.note_count % 4 == 0) or \
           (self.time_signature == '3/4' and self.note_count % 3 == 0):
            self.add_measure_line()

    
    def extend_staves(self):
        # Extend the stave lines
        new_stave_length = self.current_x_position + 100  # Extend by an arbitrary amount
        for stave in self.stave_lines:
            for line in stave:
                line.setLine(line.line().x1(), line.line().y1(), new_stave_length, line.line().y1())
        self.stave_length = new_stave_length  # Update the stave length

    def add_measure_line(self):
        # Add a vertical line at the current x-position to denote the end of a measure
        measure_line_y1 = self.stave_lines[0][0].line().y1() - 10  # Start above the first stave line
        measure_line_y2 = self.stave_lines[-1][-1].line().y1() + 10  # End below the last stave line
        measure_line = QGraphicsLineItem(self.current_x_position, measure_line_y1, self.current_x_position, measure_line_y2)
        measure_line.setPen(QPen(Qt.GlobalColor.black, 2))
        self.addItem(measure_line)

        # Update the stave length if necessary
        if self.current_x_position > self.stave_length:
            self.stave_length = self.current_x_position
         
    def draw_time_signature(self):
        # Check if time signature items exist and remove them
        if self.time_signature_item:
            for item in self.time_signature_item:
                self.removeItem(item)  # Remove each QGraphicsItem individually
        top_number_item = QGraphicsTextItem(self.time_signature.split('/')[0])
        top_number_item.setFont(QFont("Times New Roman", 16, QFont.Weight.Bold))
        top_number_item.setPos(20, self.stave_lines[0][0].line().y1() - 10)  
        
        # Create a new text item for the bottom number of the time signature
        bottom_number_item = QGraphicsTextItem(self.time_signature.split('/')[1])
        bottom_number_item.setFont(QFont("Times New Roman", 16, QFont.Weight.Bold))
        bottom_number_item.setPos(20, self.stave_lines[0][2].line().y1() - 10)  

         # Add the time signature items to the scene
        self.addItem(top_number_item)
        self.addItem(bottom_number_item)

        # Store the time signature items to remove them later if needed
        self.time_signature_item = (top_number_item, bottom_number_item)
    
    def set_time_signature(self, signature):
        self.time_signature = signature
        self.draw_time_signature()
        self.update()
    
    def update(self):
        # Redraw the scene if necessary
        self.invalidate()
