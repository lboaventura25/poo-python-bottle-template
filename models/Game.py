import copy
from BoardInitialize import Board
from pawn import Pawn
from queen import Queen
from rook import Rook
from knight import Knight
from bishop import Bishop
from king import King

class Game:

    def __init__(self):
        
        self.board = Board()    
        self.turn = 'white'

        

    def getPiece(self, position):

        col = ord(position[0]) - ord('a')
        row = 8 - int(position[1])
        return self.board.game[row][col]

    def setPiece(self, position, piece):

        col = ord(position[0]) - ord('a')
        row = 8 - int(position[1])
        self.board.game[row][col] = piece

    def isKingInCheck(self, board, color):
        
        enemy_color = "black" if color == "white" else "white"

        for row in range(8):
            for col in range(8):
                attacker = board.game[row][col]
                if attacker is not None and attacker.color == enemy_color:
                    pos = chr(col + ord('a')) + str(8 - row)
                    if attacker.isCheck(pos, board, color):
                        return True
        
        return False
    
    def try_move(self, start, end):
        """Tenta realizar uma jogada e retorna JSON baseado no BOAS práticas do Bottle"""

        # 1. Validar formato
        if len(start) != 2 or len(end) != 2:
            return {"valid": False, "error": "Invalid input format"}

        piece = self.getPiece(start)

        if piece is None:
            return {"valid": False, "error": "No piece at start position"}

        if piece.color != self.turn:
            return {"valid": False, "error": "Not your piece"}

        # 2. Simular jogada
        temp_board = copy.deepcopy(self.board)
        self.setPieceOn(temp_board, end, piece)
        self.setPieceOn(temp_board, start, None)

        if self.isKingInCheck(temp_board, self.turn):
            return {"valid": False, "error": "Illegal move: King would be in check"}

        # 3. Executar jogada real
        if not piece.makeMoves(start, end, self.board):
            return {"valid": False, "error": "Invalid move for this piece"}

        # 4. Checar se deu cheque no inimigo
        enemy_color = "black" if self.turn == "white" else "white"
        in_check = self.isKingInCheck(self.board, enemy_color)

        # 5. Trocar turno
        self.turn = enemy_color

        # 6. Retornar resultado
        return {
            "valid": True,
            "check": in_check,
            "turn": self.turn,
            "board": self.board.to_matrix() if hasattr(self.board, "to_matrix") else None
        }

    # método auxiliar para mexer peças no board temporário
    def setPieceOn(self, board, position, piece):

        col = ord(position[0]) - ord('a')
        row = 8 - int(position[1])
        board.game[row][col] = piece



        