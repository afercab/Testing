import socket
import random


def create_and_bind_socket():
    global server_socket
    ip = "127.0.0.1"
    port = 4008
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((ip, port))
        server_socket.listen(1)
    except ValueError:
        raise ValueError("Could not open a connection.")


def check_data_is_integer():
    global guess

    try:
        guess = int(guess)
    except ValueError:
        raise ValueError("You should have used an integer as first parameter.")


def game_logic(counter):
    global guess
    while answer != guess:
        counter += 1
        if answer == guess:
            connection.send("Yes")
            connection.send(counter)
            break
        else:
            connection.send("No")
        guess = int(connection.recv(80))
        connection.close()


create_and_bind_socket()
print "Waiting..."
while True:
    try:
        (connection, address) = server_socket.accept()
    except ValueError:
        raise ValueError("Connection could not be accepted.")
    print "Connection  from", address
    print connection.recv(80)

    answer = random.randrange(0, 10)
    attempts = 0
    guess = connection.recv(80)
    check_data_is_integer()
    game_logic(attempts)
