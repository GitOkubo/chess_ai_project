import chess
from board_evaluator import evaluate_board


def minimax(board, depth, is_maximizing):
    if depth == 0 or board.is_game_over():
        board = board.fen()
        return evaluate_board(board)

    if is_maximizing:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, False)
            board.pop()
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, True)
            board.pop()
            min_eval = min(min_eval, eval)
        return min_eval
    
def find_best_move(fen, depth=2):
    board = chess.Board(fen)
    best_move = None
    best_value = float('-inf') if board.turn else float('inf')

    for move in board.legal_moves:
        board.push(move)
        value = minimax(board, depth - 1, not board.turn)
        board.pop()

        if board.turn and value > best_value:
            best_value = value
            best_move = move
        elif not board.turn and value < best_value:
            best_value = value
            best_move = move

    return best_move.uci() if best_move else None