import numpy as np
import chess

def extract_features(board):
    """
    駒の種類ごとの差分を特徴量として抽出する（白 - 黒）。
    戻り値は以下の順:
    [pawn_diff, bishop_diff, rook_diff, knight_diff, queen_diff]
    """
    piece_counts = {
        'P': 0, 'N': 0, 'B': 0, 'R': 0, 'Q': 0,
        'p': 0, 'n': 0, 'b': 0, 'r': 0, 'q': 0,
    }

    for piece in board.piece_map().values():
        symbol = piece.symbol()
        if symbol in piece_counts:
            piece_counts[symbol] += 1

    pawn_diff   = piece_counts['P'] - piece_counts['p']
    bishop_diff = piece_counts['B'] - piece_counts['b']
    rook_diff   = piece_counts['R'] - piece_counts['r']
    knight_diff = piece_counts['N'] - piece_counts['n']
    queen_diff  = piece_counts['Q'] - piece_counts['q']

    return np.array([pawn_diff, bishop_diff, rook_diff, knight_diff, queen_diff], dtype=np.float32)

def evaluate_board(fen):
    """
    FENから盤面を読み込み、特徴量を抽出して評価値（0〜1）を返す。
    """
    board = chess.Board()
    try:
        board.set_fen(fen)
    except ValueError as e:
        print(f"Invalid FEN: {e}")
        return None

    features = extract_features(board)

    # 仮の係数と切片（自分の学習結果に差し替えてOK）
    weights = np.array([0.24335144, 0.37209904, 0.36420548, 0.3327036, 0.4823955], dtype=np.float32)
    intercept = 0.07532935  # ← 自分の値に置き換えてOK

    score = np.dot(features, weights) + intercept
    probability = 1 / (1 + np.exp(-score))

    # ★★★改善点：黒番なら確率を反転する（白の勝率 → 黒の勝率）
    if not board.turn:
        probability = 1.0 - probability

    return probability


# 使用例
if __name__ == "__main__":
    sample_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    prob = evaluate_board(sample_fen)
    print(f"評価値（）: {prob:.3f}")
