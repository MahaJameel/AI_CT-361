import time
from tictactoe import TicTacToeGame, minimax_basic, minimax_pruning


def test_algorithm_speed():
    basic_game = TicTacToeGame()
    pruning_game = TicTacToeGame()

    print("\nTesting basic minimax...")
    start_time = time.time()
    play_full_game(basic_game, use_pruning=False)
    print(f"Time taken: {time.time() - start_time:.4f} seconds\n")

    print("\nTesting minimax with alpha-beta pruning...")
    start_time = time.time()
    play_full_game(pruning_game, use_pruning=True)
    print(f"Time taken: {time.time() - start_time:.4f} seconds\n")

def play_full_game(game, use_pruning=True):
    current_player = 'X'
    while game.has_moves_left() and not game.winner:
        print(f"\n{current_player}'s turn.")
        
        if use_pruning:
            move_info = minimax_pruning(game, current_player)
        else:
            move_info = minimax_basic(game, current_player)

        chosen_move = move_info['move']
        score = move_info['score']

        print(f"{current_player} plays at {chosen_move} with a score of {score}")

        game.make_move(chosen_move, current_player)
        game.display()
        print()

        current_player = 'O' if current_player == 'X' else 'X'

    print("Game Over!")
    print(f"Winner: {game.winner if game.winner else 'Draw'}")

def play_against_ai():
    game = TicTacToeGame()
    player_symbol = input("Choose your symbol (X = first, O = second): ").upper()
    ai_symbol = 'O' if player_symbol == 'X' else 'X'
    current_player = 'X'

    while game.has_moves_left() and not game.winner:
        game.display()
        if current_player == player_symbol:
            move = None
            while move not in game.available_moves():
                try:
                    move = int(input("Your move (0-8): "))
                    if move not in game.available_moves():
                        print("Invalid or occupied tile. Try again.")
                except ValueError:
                    print("Enter a valid number between 0 and 8.")
            game.make_move(move, player_symbol)
        else:
            print(f"\nAI ({ai_symbol}) is thinking...")
            move_info = minimax_pruning(game, ai_symbol)
            ai_move = move_info['move']
            print(f"AI plays at {ai_move} with a score of {move_info['score']}")
            game.make_move(ai_move, ai_symbol)

        current_player = 'O' if current_player == 'X' else 'X'

    game.display()
    if game.winner == player_symbol:
        print("Congratulations! You win!")
    elif game.winner == ai_symbol:
        print("You lost. AI wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    if input("\nDo you want to play against AI, or Test Algorithm Speeds? \n P [Play] / T [Test]): ").lower() == 'y':
        play_against_ai()
    else:
        test_algorithm_speed()

