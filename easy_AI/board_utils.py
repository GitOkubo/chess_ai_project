def display_board(board):
    print("  a b c d e f g h")
    for i, row in enumerate(board):
        line = f"{8 - i} "
        for piece in row:
            if piece is None:
                line += ". "
            else:
                color = piece[0]
                kind = piece[1]
                symbol = kind.lower() if color == 'b' else kind.upper()
                line += symbol + " "
        line += f"{8 - i}"
        print(line)
    print("  a b c d e f g h")