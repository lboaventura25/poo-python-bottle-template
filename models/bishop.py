from piece import Piece
from king import King

class Bishop(Piece):

    def __init__(self, color):

        super().__init__(color)
        self.symbol = 'b'

    def propagate(self,dx,dy,board,i,j):

        game = board.game
        size = len(game)

        ni, nj = i + dx, j + dy  # next position

        if 0 <= ni < size and 0 <= nj < size:

            if game[ni][nj] is None:

                return True

        return False

    def checkDiagonal(self, board, startLine, startColumn, endLine, endColumn):

        if startLine == endLine and startColumn == endColumn:
            return False

        if abs(endLine - startLine) != abs(endColumn - startColumn):

            return False

        elif endLine > startLine and endColumn > startColumn:

            dx = 1
            dy = 1

            if startLine + dx == endLine and startColumn + dy == endColumn:
                return True

            isPossible = self.propagate(dx,dy,board,startLine,startColumn)

            if isPossible == True:

                return self.checkDiagonal(board,startLine + 1,startColumn + 1,endLine,endColumn)

            elif isPossible == False:

                return False

        elif endLine > startLine and endColumn < startColumn:

            dx = 1
            dy = -1

            if startLine + dx == endLine and startColumn + dy == endColumn:
                return True

            isPossible = self.propagate(dx,dy,board,startLine,startColumn)

            if isPossible == True:

                return self.checkDiagonal(board,startLine + 1,startColumn - 1,endLine,endColumn)

            elif isPossible == False:

                return False

        elif endLine < startLine and endColumn < startColumn:

            dx = -1
            dy = -1

            if startLine + dx == endLine and startColumn + dy == endColumn:
                return True

            isPossible = self.propagate(dx,dy,board,startLine,startColumn)

            if isPossible == True:

                return self.checkDiagonal(board,startLine - 1,startColumn - 1,endLine,endColumn)

            elif isPossible == False:

                return False

        elif endLine < startLine and endColumn > startColumn:

            dx = -1
            dy = 1

            if startLine + dx == endLine and startColumn + dy == endColumn:
                return True

            isPossible = self.propagate(dx,dy,board,startLine,startColumn)

            if isPossible == True:

                return self.checkDiagonal(board,startLine - 1,startColumn + 1,endLine,endColumn)

            elif isPossible == False:

                return False


    def makeMoves(self,input,output,board):

        start = self.convertMoves(input)
        end = self.convertMoves(output)

        startLine = start[1]
        startColumn = start[0]

        endLine = end[1]
        endColumn = end[0]

        game = board.game

        isPossible = self.checkDiagonal(board,startLine,startColumn,endLine,endColumn)

        if (isPossible == True
           and game[endLine][endColumn] is not None
           and game[endLine][endColumn].color != self.color
           ):

            game[startLine][startColumn] = None
            game[endLine][endColumn] = self

            return True

        elif (isPossible == True
           and game[endLine][endColumn] is None
           ):

            game[startLine][startColumn] = None
            game[endLine][endColumn] = self

            return True

        else:

            return False

    def isCheck(self,input,board,color):

        start = self.convertMoves(input)

        startLine = start[1]
        startColumn = start[0]

        position = self.findKing(board,color)
        row = position[0]
        column = position[1]

        isPossible = self.checkDiagonal(board, startLine, startColumn, row, column)

        return isPossible

    def findKing(self,board,color):

        for row in range(len(board.game)):

            for col in range(len(board.game[row])):

                if board.game[row][col] is not None:

                    if (board.game[row][col].color == color
                       and board.game[row][col].symbol == 'k'):

                            return [row,col]


