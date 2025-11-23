from typing import is_protocol

from piece import Piece

class Rook(Piece):

    def __init__(self, color):
        
        super().__init__(color)
        self.symbol = 'r'
        
    #@override
    def makeMoves(self,input,output,board):

        start = self.convertMoves(input)
        end = self.convertMoves(output)

        startLine = start[1]
        startColumn = start[0]

        endLine = end[1]
        endColumn = end[0]

        game = board.game

        isPossible = True

        #this next block checks if there isnt a piece blocking a way for THE ROOOOOKKKKK to walk

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

        else:

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