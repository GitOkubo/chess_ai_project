import pandas as pd

def load_game_data(filepath):
    """
    棋譜CSVを読み込んで、盤面や手のリストに変換する関数
    """
    df = pd.read_csv(filepath)
    games = df["moves"].tolist()  # 例: "e4 e5 Nf3 Nc6 ..." の文字列
    return games
