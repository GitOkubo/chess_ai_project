import pandas as pd
from data_loader import extract_boards_from_csv
from evaluator import simple_evaluate
from config import game_amount
from board_utils import display_board
from best_move import select_best_move_from_fen

results = []
a_array, winners, boards = extract_boards_from_csv("test/data/games.csv", game_amount)
idx = 0
for array, winner, board in zip(a_array, winners, boards):
    idx += 1
    fen = board.fen()
    score = simple_evaluate(array)
    display_board(array)        
    print(f"Game {idx} Final Evaluation (White) : {score}") 
    print(f"Game Winner : {winner}")
    print(f"Next Best Move (White) : {select_best_move_from_fen(fen)}")
    print()
    results.append({"Game" : idx, "Final Score": score})

# 結果を保存
df_result = pd.DataFrame(results)
df_result.to_csv("test/data/evaluation_results.csv", index=False)