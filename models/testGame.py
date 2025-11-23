from Game import Game  # sua classe Game

def main():
    game = Game()
    print("♟️ Xadrez Boaventura Teste Interativo! ♟️")
    print("Tabuleiro inicial carregado a partir do BoardInitialize.\n")

    while True:
        # Usa o displayBoard da sua classe Board (bonito)
        game.board.displayBoard()
        print(f"Turno atual: {game.turn}\n")

        move = input("Digite sua jogada (ex: e2 e4) ou 'q' para sair: ").strip()
        if move.lower() == "q":
            print("Fim do teste.")
            break

        parts = move.split()
        if len(parts) != 2:
            print("❌ Formato inválido. Use como: e2 e4\n")
            continue

        start, end = parts
        result = game.try_move(start, end)

        # Mostra o dict completo do resultado
        print("Resultado do try_move:", result)

        # Linha de resumo amigável
        if result["valid"]:
            msg = f"✔ Jogada {start} -> {end} realizada! Turno agora: {result['turn']}"
            if result.get("check"):
                # Mostra que o rei inimigo está em cheque
                enemy_color = "black" if result['turn'] == "white" else "white"
                msg += f" ⚠️ Rei {enemy_color} em CHECK!"
        else:
            msg = f"❌ Jogada {start} -> {end} inválida: {result.get('error')}"

        print(msg + "\n")

if __name__ == "__main__":
    main()
