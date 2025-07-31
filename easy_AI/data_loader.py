import pandas as pd
import chess
from config import move_number

def board_to_array(board):
    """Board オブジェクトを 8×8 の配列に変換"""
    array = []
    for rank in board.board_fen().split("/"):
        row = []
        for c in rank:
            if c.isdigit():
                row.extend([None] * int(c))
            else:
                color = 'w' if c.isupper() else 'b'
                row.append(color + c.upper())
        array.append(row)
    return array

# CSVファイルの読み込み（必要に応じてパスを変更）
def extract_boards_from_csv(csv_path, game_amount):
    df = pd.read_csv(csv_path)
    df_sample = df.head(game_amount)
    board_arrays = []
    winners = []
    boards = []
    for idx, row in df_sample.iterrows():
        moves = row["moves"].split()
        winners.append(row["winner"])
        board = chess.Board()
        for move in moves[:move_number if move_number > 0 else len(moves)]:
            try:
                board.push_san(move)
            except ValueError as e:
                print(f"Invalid move '{move}' in game {idx}: {e}")
                break
        board_arrays.append(board_to_array(board))
        boards.append(board)
    return board_arrays, winners, boards