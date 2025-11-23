    # método auxiliar para mexer peças no board temporário
    def setPieceOn(self, board, position, piece):

        col = ord(position[0]) - ord('a')
        row = 8 - int(position[1])
        board.game[row][col] = piece