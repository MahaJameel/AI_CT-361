class TicTacToeGame:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winner = None

    def display(self):
        for i in range(3):
            print('| ' + ' | '.join(self.board[i * 3:(i + 1) * 3]) + ' |')

    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            if self.check_winner(player):
                self.winner = player
            return True
        return False

    def check_winner(self, player):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in win_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def has_moves_left(self):
        return ' ' in self.board

    def available_moves(self):
        return [i for i, tile in enumerate(self.board) if tile == ' ']


def minimax_basic(game_state, current_player):
    opponent = 'O' if current_player == 'X' else 'X'

    if game_state.winner == opponent:
        return {'move': None, 'score': 1 if opponent == 'X' else -1}
    if not game_state.has_moves_left():
        return {'move': None, 'score': 0}

    best_move = None
    if current_player == 'X':
        best_score = float('-inf')
        for move in game_state.available_moves():
            game_state.make_move(move, current_player)
            result = minimax_basic(game_state, opponent)
            game_state.board[move] = ' '
            game_state.winner = None

            if result['score'] > best_score:
                best_score = result['score']
                best_move = move
    else:
        best_score = float('inf')
        for move in game_state.available_moves():
            game_state.make_move(move, current_player)
            result = minimax_basic(game_state, opponent)
            game_state.board[move] = ' '
            game_state.winner = None

            if result['score'] < best_score:
                best_score = result['score']
                best_move = move

    return {'move': best_move, 'score': best_score}


def minimax_pruning(game_state, current_player, alpha=float('-inf'), beta=float('inf')):
    opponent = 'O' if current_player == 'X' else 'X'

    if game_state.winner == opponent:
        return {'move': None, 'score': 1 if opponent == 'X' else -1}
    if not game_state.has_moves_left():
        return {'move': None, 'score': 0}

    best_move = None

    if current_player == 'X':
        best_score = float('-inf')
        for move in game_state.available_moves():
            game_state.make_move(move, current_player)
            result = minimax_pruning(game_state, opponent, alpha, beta)
            game_state.board[move] = ' '
            game_state.winner = None

            if result['score'] > best_score:
                best_score = result['score']
                best_move = move

            alpha = max(alpha, result['score'])
            if beta <= alpha:
                break
    else:
        best_score = float('inf')
        for move in game_state.available_moves():
            game_state.make_move(move, current_player)
            result = minimax_pruning(game_state, opponent, alpha, beta)
            game_state.board[move] = ' '
            game_state.winner = None

            if result['score'] < best_score:
                best_score = result['score']
                best_move = move

            beta = min(beta, result['score'])
            if beta <= alpha:
                break

    return {'move': best_move, 'score': best_score}
