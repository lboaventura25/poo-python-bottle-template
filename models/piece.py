class Piece:

    def __init__(self,color):

        self.color = color

    def makeMoves(self):

        raise NotImplementedError("This piece cannot move directly. Use subclass rules.")

    def isCheck(self):

        raise NotImplementedError("This piece cannot move directly. Use subclass rules.")

    def convertMoves(self, input):

        col = ord(input[0].lower()) - ord('a')
        row = 8 - int(input[1])

        return [col, row]

