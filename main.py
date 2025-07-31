from minimax_search import find_best_move
from board_evaluator import evaluate_board
from utils.data_loader import load_game_data

def main():
    print("チェスAIを起動します。")
    
    board = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP2PP/RNBQKBNR w KQkq - 0 1"
    print("評価値:", evaluate_board(board))
    
    best_move = find_best_move(board, depth=2)
    print("推奨手:", best_move)

if __name__ == "__main__":
    main()
