from pawn import Pawn
from bishop import Bishop
from rook import Rook
from knight import Knight
from queen import Queen
from king import King

class Board:

    def __init__(self):
        
        self.initializeBoard()

    def initializeBoard(self):

        self.game = [
                    [Rook('black'),Knight('black'),Bishop('black'),Queen('black'),King('black'),Bishop('black'),Knight('black'),Rook('black')],
                    [Pawn('black'),Pawn('black'),Pawn('black'),Pawn('black'),Pawn('black'),Pawn('black'),Pawn('black'),Pawn('black')],
                    [None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None],                   
                    [None,None,None,None,None,None,None,None],
                    [Pawn('white'),Pawn('white'),Pawn('white'),Pawn('white'),Pawn('white'),Pawn('white'),Pawn('white'),Pawn('white')],
                    [Rook('white'),Knight('white'),Bishop('white'),Queen('white'),King('white'),Bishop('white'),Knight('white'),Rook('white')]
                    ]


    def displayBoard(self):

            print("   a  b  c  d  e  f  g  h")
            symbols = {
                "Pawn": "P",
                "Rook": "R",
                "Knight": "N",
                "Bishop": "B",
                "Queen": "Q",
                "King": "K"
            }

            for i, row in enumerate(self.game):
                print(8 - i, end=" ")
                for piece in row:
                    if piece is None:
                        print(" . ", end="")
                    else:
                        symbol = symbols[piece.__class__.__name__]
                        if piece.color == "black":
                            symbol = symbol.lower()
                        print(f" {symbol} ", end="")
                print("", 8 - i)
            print("   a  b  c  d  e  f  g  h")


