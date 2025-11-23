from tkinter.messagebox import RETRY
from xmlrpc.client import FastUnmarshaller

from piece import Piece

class King(Piece):

    def __init__(self, color):
       
        super().__init__(color)
        self.symbol = 'k'

    def makeMoves(self, input, output, board):

        start = self.convertMoves(input)
        end = self.convertMoves(output)

        startLine = start[1]
        startColumn = start[0]

        endLine = end[1]
        endColumn = end[0]

        game = board.game

        isPossible = False

        if not hasattr(self, "hasMoved"):
            self.hasMoved = False

        # Brancas
        if self.color == "white" and not self.hasMoved:
            # e1 → g1
            if startLine == 7 and startColumn == 4 and endLine == 7 and endColumn == 6:
                if self.castle(board, startLine, startColumn, endLine, endColumn):
                    self.hasMoved = True
                    return True
                else:
                    return False  # stop here if castle failed

            # e1 → c1
            elif startLine == 7 and startColumn == 4 and endLine == 7 and endColumn == 2:
                if self.castle(board, startLine, startColumn, endLine, endColumn):
                    self.hasMoved = True
                    return True
                else:
                    return False

        # Pretas
        if self.color == "black" and not self.hasMoved:
            # e8 → g8
            if startLine == 0 and startColumn == 4 and endLine == 0 and endColumn == 6:
                if self.castle(board, startLine, startColumn, endLine, endColumn):
                    self.hasMoved = True
                    return True
                else:
                    return False

            # e8 → c8
            elif startLine == 0 and startColumn == 4 and endLine == 0 and endColumn == 2:
                if self.castle(board, startLine, startColumn, endLine, endColumn):
                    self.hasMoved = True
                    return True
                else:
                    return False

        if (endLine == startLine - 1) and (endColumn == startColumn + 1):

            isPossible = True

        elif (endLine == startLine) and (endColumn == startColumn + 1):

            isPossible = True

        elif (endLine == startLine + 1) and (endColumn == startColumn + 1):

            isPossible = True

        elif (endLine == startLine + 1) and (endColumn == startColumn):

            isPossible = True

        elif (endLine == startLine + 1) and (endColumn == startColumn - 1):

            isPossible = True

        elif (endLine == startLine - 1) and (endColumn == startColumn - 1):

            isPossible = True

        elif (endLine == startLine) and (endColumn == startColumn - 1):

            isPossible = True

        elif (endLine == startLine - 1) and (endColumn == startColumn):

            isPossible = True

        else:

            isPossible = False



        if isPossible == True:

            if (game[endLine][endColumn] is not None
               and game[endLine][endColumn].color != self.color):

                game[startLine][startColumn] = None
                game[endLine][endColumn] = self
                self.hasMoved = True

                return True

            elif (game[endLine][endColumn] is None):

                game[startLine][startColumn] = None
                game[endLine][endColumn] = self
                self.hasMoved = True

                return True

            else:

                return False

        else:

            return False

    def isCheck(self, input, board, color):

        start = self.convertMoves(input)

        startLine = start[1]
        startColumn = start[0]

        position = self.findKing(board, color)
        endLine = position[0]
        endColumn = position[1]

        isPossible = False

        if (endLine == startLine - 1) and (endColumn == startColumn + 1):

            isPossible = True

        elif (endLine == startLine) and (endColumn == startColumn + 1):

            isPossible = True

        elif (endLine == startLine + 1) and (endColumn == startColumn + 1):

            isPossible = True

        elif (endLine == startLine + 1) and (endColumn == startColumn):

            isPossible = True

        elif (endLine == startLine + 1) and (endColumn == startColumn - 1):

            isPossible = True

        elif (endLine == startLine - 1) and (endColumn == startColumn - 1):

            isPossible = True

        elif (endLine == startLine) and (endColumn == startColumn - 1):

            isPossible = True

        elif (endLine == startLine - 1) and (endColumn == startColumn):

            isPossible = True

        else:

            isPossible = False

        return isPossible

    def findKing(self,board,color):

        for row in range(len(board.game)):

            for col in range(len(board.game[row])):

                if board.game[row][col] is not None:

                    if (board.game[row][col].color == color
                       and board.game[row][col].symbol == 'k'):

                            return [row,col]

    def castle(self, board, startLine, startColumn, endLine, endColumn):

            if startLine == endLine and (startColumn + 2) == endColumn:

                if (board.game[startLine][startColumn + 1] is None
                    and board.game[startLine][startColumn + 2] is None
                ):

                    board.game[startLine][startColumn + 2] = self
                    board.game[startLine][startColumn + 1] = board.game[startLine][startColumn + 3]
                    board.game[startLine][startColumn + 3] = None
                    board.game[startLine][startColumn] = None

                    return True

            elif startLine == endLine and (startColumn - 2) == endColumn:

                if (board.game[startLine][startColumn -1] is None
                    and board.game[startLine][startColumn - 2] is None
                    and board.game[startLine][startColumn - 3] is None
                ):

                    board.game[startLine][startColumn - 2] = self
                    board.game[startLine][startColumn - 1] = board.game[startLine][startColumn -4]
                    board.game[startLine][startColumn - 4] = None
                    board.game[startLine][startColumn] = None

                    return True

            return False



