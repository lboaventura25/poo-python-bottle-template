from piece import Piece

class Knight(Piece):

    def __init__(self, color):
        
        super().__init__(color)
        self.symbol = 'n'

    def makeMoves(self,input,output,board):

        start = self.convertMoves(input)
        end = self.convertMoves(output)

        startLine = start[1]
        startColumn = start[0]

        endLine = end[1]
        endColumn = end[0]

        game = board.game

        isPossible = True

        rowDiff = abs(endLine - startLine)
        colDiff = abs(endColumn - startColumn)

        if not ((rowDiff == 2 and colDiff == 1) or (rowDiff == 1 and colDiff == 2)):

            isPossible = False

        if isPossible == True:

            target = game[endLine][endColumn]

            if target is None or (target is not None and target.color != self.color):

                game[startLine][startColumn] = None
                game[endLine][endColumn] = self

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

        isPossible = True

        rowDiff = abs(endLine - startLine)
        colDiff = abs(endColumn - startColumn)

        if not ((rowDiff == 2 and colDiff == 1) or (rowDiff == 1 and colDiff == 2)):

            isPossible = False

        if isPossible == True:

            target = board.game[endLine][endColumn]

            if target is None or (target is not None and target.color != self.color):

                return True

            else:

                return False

        else:

            return False

    def findKing(self,board,color):

        for row in range(len(board.game)):

            for col in range(len(board.game[row])):

                if board.game[row][col] is not None:

                    if (board.game[row][col].color == color
                       and board.game[row][col].symbol == 'k'):

                            return [row,col]