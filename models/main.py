import copy
from BoardInitialize import Board
from pawn import Pawn
from queen import Queen
from rook import Rook
from knight import Knight
from bishop import Bishop
from king import King

def getPiece(board, position):
    col = ord(position[0]) - ord('a')
    row = 8 - int(position[1])
    return board.game[row][col]

def setPiece(board, position, piece):
    col = ord(position[0]) - ord('a')
    row = 8 - int(position[1])
    board.game[row][col] = piece

def isKingInCheck(board, color):
    """Return True if the king of `color` is in check."""
    enemy_color = "black" if color == "white" else "white"

    for row in range(8):
        for col in range(8):
            attacker = board.game[row][col]
            if attacker is not None and attacker.color == enemy_color:
                pos = chr(col + ord('a')) + str(8 - row)
                if attacker.isCheck(pos, board, color):
                    return True
    return False


def main():
    board = Board()
    print("♟️ Xadrez Boaventura!")
    turn = "white"

    while True:
        board.displayBoard()
        print(f"\nIt's {turn}'s turn.")

        while True:
            move = input("Enter your move (ex: e2 e4) or 'q' to quit: ").strip()
            if move.lower() == "q":
                print("Game ended.")
                return

            parts = move.split()
            if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) != 2:
                print("❌ Invalid input format. Use like: e2 e4.")
                continue

            start, end = parts
            piece = getPiece(board, start)
            if piece is None:
                print("❌ No piece at that position.")
                continue

            if piece.color != turn:
                print("❌ That's not your piece.")
                continue

            # Manda o jogo pra outro tabuleiro hipotetico pra ver se n tem cheque
            temp_board = copy.deepcopy(board)
            setPiece(temp_board, end, piece)
            setPiece(temp_board, start, None)

            # Ve se o rei ta em cheque
            if isKingInCheck(temp_board, turn):
                print("🚫 Illegal move: Your king would be in CHECK!")
                continue  # retry the move (real board untouched)

            # Jogada no Tabuleiro Real

            print(f"Trying move {start} -> {end}")

            if not piece.makeMoves(start, end, board):
                print("❌ Invalid move for this piece.")
                continue

            break  # Feito

        # Oponente em Cheque
        enemy_color = "black" if turn == "white" else "white"
        if isKingInCheck(board, enemy_color):
            print(f"⚠️ {turn.capitalize()} puts the {enemy_color} king in CHECK!")

        # Acabou o turno
        turn = enemy_color


if __name__ == "__main__":
    main()
