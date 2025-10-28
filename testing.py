import random
import time #<--- fitur tembakan loading

#  Konfigurasi dasar 
BOARD_SIZE = 5

SHIP_LENGTH = 3

SHIP_COUNT = 3

MAX_ATTEMPTS = 10

#  Buat papan kosong 
board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
hidden = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

#  Nama kapal 
ship_names = ["Going Merry", "Queen Mama", "Red Force"]

#  Tempatkan kapal 
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

#  Fungsi cetak papan 
def show_board(b):
    print("\n    ", end="")  # cetak header kolom angka di atas
    for i in range(BOARD_SIZE):
        print(f"{i+1}   ", end="")  # papan mulai dari 1
    print()
    print("  +" + "---+" * BOARD_SIZE)  # garis atas papan
    
    for i in range(BOARD_SIZE):
        print(f"{i+1:2}|", end="")  # cetak nomor baris di kiri
        for j in range(BOARD_SIZE):
            print(f" {b[i][j]} |", end="")  # isi tiap kotak
        print()
        print("  +" + "---+" * BOARD_SIZE)  # garis bawah tiap baris
    print()

# Permainan dimulai 
print("                  Selamat datang di Battleship!                     ")
print("Sudah saatnya dirimu dan kru mu menjadi Yonko terkenal dan mematikan")
print("              Kalahkan Mereka semua dan rebut gelarnya!!            ")

hits = 0
total_parts = SHIP_COUNT * SHIP_LENGTH
sunk = [0] * SHIP_COUNT  # Hitungan tiap kapal

for turn in range(MAX_ATTEMPTS):
    print(f"Percobaan ke-{turn+1}:")
    show_board(hidden)
    
    row_in = input("Baris (1-5): ")
    col_in = input("Kolom (1-5): ")

    # cek apakah input berupa angka
    if not (row_in.isdigit() and col_in.isdigit()):
        print("Masukkan angka ya!\n")
        continue

    row = int(row_in) - 1
    col = int(col_in) - 1
    
    # FITUR TEMBAK LOADING
    print("Menembak", end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    time.sleep(0.3)
    print("BOOM!\n")

    cell = board[row][col]
    if cell in ['1', '2', '3']:
        ship_id = int(cell) - 1
        sunk[ship_id] += 1
        hidden[row][col] = 'X'
        hits += 1
        print(f" Meriam mu mengenai {ship_names[ship_id]}!")
        if sunk[ship_id] == SHIP_LENGTH:
            print(f" HAHAHA!! Kapal {ship_names[ship_id]} tenggelam!\n")
        else:
            print()
    else:
        hidden[row][col] = '-'
        print(" Meleset!\n")

    if hits == total_parts:
        print(" Semua kapal tenggelam! Kamu menang!\n")
        break

if hits < total_parts:
    print(" Kesempatan habis! Ini posisi kapal sebenarnya:")
    show_board(board)