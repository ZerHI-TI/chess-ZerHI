from PyQt6.QtWidgets import (
    QWidget, QGridLayout, QPushButton, QLabel
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

from gameLogic import logic_bishop, logic_king, logic_knight, logic_pawn, logic_queen, logic_rook

class BoardWidget(QWidget):
    current_color = 'white'
    captured_pieces_black = []
    captured_pieces_white = []
    
    def __init__(self):
        super().__init__()
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.selected_piece = None
        self.selected_position = None

        self.pieces_unicode = {
            'white': {'king': '♔', 'queen': '♕', 'rook': '♖', 
                     'bishop': '♗', 'knight': '♘', 'pawn': '♙'},
            'black': {'king': '♚', 'queen': '♛', 'rook': '♜', 
                     'bishop': '♝', 'knight': '♞', 'pawn': '♟'}
        }

        self.setup_board()

    def setup_board(self):
        for row in range(8):
            for col in range(8):
                square = QPushButton()
                square.setFixedSize(70, 70)
                if (row+col) % 2 == 0:
                    square.setStyleSheet("""
                        QPushButton {
                            background-color: #f0d9b5;
                            border: 1px solid #b58863;
                            font-size: 40px;
                        }
                    """) 
                else:
                    square.setStyleSheet("""
                        QPushButton {
                            background-color: #b58863;
                            border: 1px solid #f0d9b5;
                            font-size: 40px;
                        }
                    """)
                square.clicked.connect(lambda checked, r=row, c=col: self.square_clicked(r,c))
                self.grid_layout.addWidget(square, row, col)
                self.board[row][col] = square
        self.init_position_piece()

    def init_position_piece(self):
        name_piece = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']

        for col, piece in enumerate(name_piece):
            self.place_piece(7, col, 'white', piece)
        
        for col in range(8):
            self.place_piece(6, col, 'white', 'pawn')
        for col in range(8):
            self.place_piece(1, col, 'black', 'pawn')

        for col, piece in enumerate(name_piece):
            self.place_piece(0, col, 'black', piece)

    def place_piece(self, row, col, color, piece_type):
        piece_icon = self.pieces_unicode[color][piece_type]
        button = self.board[row][col]
        button.setText(piece_icon)
        button.setProperty('color', color)
        button.setProperty('piece_type', piece_type)

    def square_clicked(self, row, col):
        button = self.board[row][col]
        if self.selected_piece is None:
            if button.text():
                self.selected_piece = button
                self.selected_position = (row, col)
                button.setStyleSheet(button.styleSheet() + "QPushButton { border: 3px solid green; }")
        else:
            self.move_piece(self.selected_position, (row, col))
            
            prev_button = self.board[self.selected_position[0]][self.selected_position[1]]
            prev_button.setStyleSheet(prev_button.styleSheet().replace(
                "border: 3px solid green;", ""))
            
            self.selected_piece = None
            self.selected_position = None

    def move_piece(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        from_button = self.board[from_row][from_col]
        to_button = self.board[to_row][to_col]
        # СЮДА НАДО БУДЕТ СДЕЛАТЬ ПРОВЕРКУ НА ДОПУСТИМОСТЬ 
        if from_button.property('color') == self.current_color:
            match from_button.property('piece_type'):
                case 'pawn':
                    logic_pawn(from_button.property('color'), from_pos, to_pos, from_button, to_button)
                case 'king':
                    logic_king(from_pos, to_pos, from_button, to_button)
                case 'queen':
                    logic_queen(from_pos, to_pos, from_button, to_button, self.board)
                case 'rook':
                    logic_rook(from_pos, to_pos, from_button, to_button, self.board)
                case 'bishop':
                    logic_bishop(from_pos, to_pos, from_button, to_button, self.board)
                case 'knight':
                    logic_knight(from_pos, to_pos, from_button, to_button)
            
        # if not to_button.text():
        #     to_button.setText(from_button.text()) 
        #     to_button.setProperty('color', from_button.property('color'))
        #     to_button.setProperty('piece_type', from_button.property('piece_type'))
        #     from_button.setText("") 
        #     from_button.setProperty('color', None)
        #     from_button.setProperty('piece_type', None)