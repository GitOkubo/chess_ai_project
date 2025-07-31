def simple_evaluate(board):
    piece_values = {
        'P': 1,
        'N': 3,
        'B': 3,
        'R': 5,
        'Q': 9,
        'K': 0  # 特別扱いするので、ここでは0
    }
    score = 0
    for row in board:
        for piece in row:
            if piece is None:
                continue
            color, kind = piece[0], piece[1]  # 例: 'wP' → color='w', kind='P'
            value = piece_values.get(kind.upper(), 0)
            if color == 'w':
                score += value  # 白のコマは加算
            else:
                score -= value  # 黒のコマは減算
    return score