import socket
import random


ROWS = 10
COLS = 10

SUBMARINES = 3
CRUISERS = 2
CARRIER = 1

WATER = ' '
SHIP = 'S'
HIT = 'X'
MISS = 'O'

def create_board():
    return [[WATER for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    print("  " + " ".join(str(i) for i in range(1, COLS + 1)))
    for i in range(ROWS):
        print(chr(65 + i) + " " + " ".join(board[i]))

def place_ships(board):
    ships = [SUBMARINES, CRUISERS * 2, CARRIER * 3]
    for ship_size, count in zip(range(1, 4), ships):
        for _ in range(count):
            while True:
                orientation = random.choice(['horizontal', 'vertical'])
                if orientation == 'horizontal':
                    x = random.randint(0, COLS - ship_size)
                    y = random.randint(0, ROWS - 1)
                    if all(board[y][x+i] == WATER for i in range(ship_size)):
                        for i in range(ship_size):
                            board[y][x+i] = SHIP
                        break
                else:
                    x = random.randint(0, COLS - 1)
                    y = random.randint(0, ROWS - ship_size)
                    if all(board[y+i][x] == WATER for i in range(ship_size)):
                        for i in range(ship_size):
                            board[y+i][x] = SHIP
                        break

def check_hit(board, x, y):
    if board[y][x] == SHIP:
        board[y][x] = HIT
        return True
    else:
        board[y][x] = MISS
        return False

def check_game_over(board):
    for row in board:
        if SHIP in row:
            return False
    return True

def play_game():
    server_board = create_board()

    place_ships(server_board)

    host = socket.gethostname()
    port = 9999
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print("Jogo de Batalha Naval - Servidor")

    while True:
        data, address = server_socket.recvfrom(1024)
        data = data.decode()
        x, y = int(data[1]) - 1, ord(data[0].upper()) - 65

        hit = check_hit(server_board, x, y)
        if hit:
            server_socket.sendto("Hit".encode(), address)
        else:
            server_socket.sendto("Miss".encode(), address)

        if check_game_over(server_board):
            print("Jogador venceu!")
            break

        print("Tabuleiro do Servidor:")
        print_board(server_board)

    server_socket.close()

if __name__ == "__main__":
    play_game()
