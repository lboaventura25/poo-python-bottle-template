from piece import Piece

class Queen(Piece):

    def __init__(self, color):
        
        super().__init__(color)
        self.symbol = 'q'

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

        isPossible = True

        if startLine == endLine:

            if endColumn > startColumn :

                for i in range((startColumn + 1), endColumn, +1):

                    if game[startLine][i] is not None:

                        isPossible = False
                        break

            else:

                for i in range((startColumn - 1), endColumn, -1):

                    if game[startLine][i] is not None:

                        isPossible = False
                        break

        elif startColumn == endColumn:

            if endLine > startLine:

                for i in range((startLine + 1), endLine, +1):

                    if game[i][startColumn] is not None:

                        isPossible = False
                        break

            else:

                for i in range((startLine - 1), endLine, -1):

                    if game[i][startColumn] is not None:

                        isPossible = False
                        break

        elif abs(endLine - startLine) == abs(endColumn - startColumn):

            isPossible = self.checkDiagonal(board, startLine, startColumn, endLine, endColumn)

        else:

            isPossible = False



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

    def isCheck(self, input, board, color):

        start = self.convertMoves(input)

        startLine = start[1]
        startColumn = start[0]

        position = self.findKing(board, color)
        endLine = position[0]
        endColumn = position[1]

        isPossible = True

        if startLine == endLine:

            if endColumn > startColumn :

                for i in range((startColumn + 1), endColumn, +1):

                    if board.game[startLine][i] is not None:

                        isPossible = False
                        break

            else:

                for i in range((startColumn - 1), endColumn, -1):

                    if board.game[startLine][i] is not None:

                        isPossible = False
                        break

        elif startColumn == endColumn:

            if endLine > startLine:

                for i in range((startLine + 1), endLine, +1):

                    if board.game[i][startColumn] is not None:

                        isPossible = False
                        break

            else:

                for i in range((startLine - 1), endLine, -1):

                    if board.game[i][startColumn] is not None:

                        isPossible = False
                        break

        elif abs(endLine - startLine) == abs(endColumn - startColumn):

            isPossible = self.checkDiagonal(board, startLine, startColumn, endLine, endColumn)

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

