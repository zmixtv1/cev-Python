import socket

def play_game():
    host = socket.gethostname()
    port = 9999
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("Jogo de Batalha Naval - Cliente")

    while True:
        target = input("Informe o tiro (por exemplo, A1): ")

        client_socket.sendto(target.encode(), (host, port))

        response, _ = client_socket.recvfrom(1024)
        print(response.decode())

        if response.decode() == "Jogador venceu!":
            break

    client_socket.close()

if __name__ == "__main__":
    play_game()
