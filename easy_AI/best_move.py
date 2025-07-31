import chess

# 評価関数（2Dリストを引数）
def simple_evaluate(board_2d):
    piece_values = {
        "P": 1, "N": 3, "B": 3, "R": 5, "Q": 9, "K": 0
    }
    score = 0
    for row in board_2d:
        for cell in row:
            if isinstance(cell, str) and len(cell) == 2:
                color, piece = cell[0], cell[1]
                value = piece_values.get(piece.upper(), 0)
                score += value if color == "w" else -value
    return score

# python-chess.Board → 2Dリスト（"wP", "bN"など）
def convert_board_to_2dlist(board):
    board_2d = []
    for rank in range(8):
        row = []
        for file in range(8):
            square = chess.square(file, 7 - rank)  # 上から順
            piece = board.piece_at(square)
            if piece is None:
                row.append(".")
            else:
                color = "w" if piece.color == chess.WHITE else "b"
                row.append(color + piece.symbol().upper())
        board_2d.append(row)
    return board_2d

# 最善手を選ぶ（1手読み、白番または黒番も可）
def select_best_move_from_fen(fen):
    board = chess.Board(fen)
    is_white = board.turn

    best_score = -float("inf") if is_white else float("inf")
    best_move = None

    for move in board.legal_moves:
        board_copy = board.copy()
        board_copy.push(move)

        board_2d = convert_board_to_2dlist(board_copy)
        score = simple_evaluate(board_2d)

        if is_white and score > best_score:
            best_score = score
            best_move = move
        elif not is_white and score < best_score:
            best_score = score
            best_move = move

    return best_move

