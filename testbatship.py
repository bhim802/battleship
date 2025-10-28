import random

BOARD_SIZE = 5

SHIP_LENGTH = 3

SHIP_COUNT = 3

MAX_ATTEMPTS = 10


board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
hidden = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


ship_names = ["A", "B", "C"]

for s in range(SHIP_COUNT):
    placed = False
    while not placed:
        arah = random.choice(['h', 'v'])
        if arah == 'h':
            r = random.randint(0, BOARD_SIZE - 1)
            c = random.randint(0, BOARD_SIZE - SHIP_LENGTH)
            
            # Penempatan kapal horizontal
            if all(board[r][c + i] == ' ' for i in range(SHIP_LENGTH)):
                for i in range(SHIP_LENGTH):
                    board[r][c + i] = str(s + 1)
                placed = True
        else:
            r = random.randint(0, BOARD_SIZE - SHIP_LENGTH)
            c = random.randint(0, BOARD_SIZE - 1)
            
            # Penempatan kapal vertikal
            if all(board[r + i][c] == ' ' for i in range(SHIP_LENGTH)):
                for i in range(SHIP_LENGTH):
                    board[r + i][c] = str(s + 1)
                placed = True