from piece import Piece
from queen import Queen

class Pawn(Piece):

    def __init__(self,color):
            
        super().__init__(color)
        self.symbol = 'p'
        self.has_moved = False

    #@override
    def makeMoves(self,input,output,board):

        start = self.convertMoves(input)
        end = self.convertMoves(output)

        startLine = start[1]
        startColumn = start[0]

        endLine = end[1]
        endColumn = end[0]

        game = board.game

        size = len(board.game)

        if not (0 <= endLine < size and 0 <= endColumn < size):
            return False

        if self.color == 'white':

            if (startColumn == endColumn 
            and (startLine - 2) == endLine
            and self.has_moved == False  
            and game[startLine - 1][startColumn] is None
            and game[endLine][endColumn] is None):
                
                game[endLine][endColumn] = self
                game[startLine][startColumn] = None
                self.has_moved = True

                return True 

            elif (startColumn == endColumn
                and (startLine - 1) == endLine
                and game[endLine][endColumn] is None):
                
                    game[endLine][endColumn] = self
                    game[startLine][startColumn] = None
                    self.has_moved = True
                    if self.color == 'white' and endLine == 0:
                        game[endLine][endColumn] = Queen('white')

                    return True
            
            elif ((startColumn - 1 == endColumn or startColumn + 1 == endColumn)
                and endLine == startLine - 1
                and game[endLine][endColumn] is not None
                and game[endLine][endColumn].color != self.color):

                    game[endLine][endColumn] = self
                    game[startLine][startColumn] = None
                    self.has_moved = True
                    if self.color == 'white' and endLine == 0:
                        game[endLine][endColumn] = Queen('white')

                    return True
        
            else:
                
                #movimento inválido
                return False

        elif self.color == 'black':

            if (startColumn == endColumn 
            and (startLine + 2) == endLine
            and self.has_moved == False 
            and game[startLine + 1][startColumn] is None
            and game[endLine][endColumn] is None):
                
                game[endLine][endColumn] = self
                game[startLine][startColumn] = None
                self.has_moved = True

                return True 

            elif (startColumn == endColumn
                and (startLine + 1) == endLine
                and game[endLine][endColumn] is None):
                
                    game[endLine][endColumn] = self
                    game[startLine][startColumn] = None
                    self.has_moved = True
                    if self.color == 'black' and endLine == 7:
                        game[endLine][endColumn] = Queen('black')

                    return True
            
            elif ((startColumn + 1 == endColumn or startColumn - 1 == endColumn)
                and endLine == startLine + 1
                and game[endLine][endColumn] is not None
                and game[endLine][endColumn].color != self.color):

                    game[endLine][endColumn] = self
                    game[startLine][startColumn] = None
                    self.has_moved = True
                    if self.color == 'black' and endLine == 7:
                        game[endLine][endColumn] = Queen('black')

                    return True
        
            else:
                
                #movimento inválido
                return False

    def isCheck(self, input, board, color):

        start = self.convertMoves(input)

        startLine = start[1]
        startColumn = start[0]

        position = self.findKing(board, color)
        endLine = position[0]
        endColumn = position[1]

        if self.color == 'white':

            if (endLine == startLine - 1
               and startColumn == endColumn + 1
               and board.game[endLine][endColumn] is not None
               and board.game[endLine][endColumn].color != self.color
            ):

                return True

            elif(endLine == startLine - 1
               and startColumn == endColumn - 1
               and board.game[endLine][endColumn] is not None
               and board.game[endLine][endColumn].color != self.color):

                return True

            else:

                return False

        elif self.color == 'black':

            if (endLine == startLine + 1
               and startColumn == endColumn + 1
               and board.game[endLine][endColumn] is not None
               and board.game[endLine][endColumn].color != self.color
            ):

                return True

            elif(endLine == startLine + 1
               and startColumn == endColumn - 1
               and board.game[endLine][endColumn] is not None
               and board.game[endLine][endColumn].color != self.color):

                return True

            else:

                return False

    def findKing(self,board,color):

        for row in range(len(board.game)):

            for col in range(len(board.game[row])):

                if board.game[row][col] is not None:

                    if (board.game[row][col].color == color
                       and board.game[row][col].symbol == 'k'):

                            return [row,col]