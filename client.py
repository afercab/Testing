import socket


def create_and_bind_socket():
    global connection
    host = "127.0.0.1"
    port = 4009
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.bind((host, port))
    except ValueError:
        raise ValueError("Could not open a connection.")


def successful_try():
    print "Nice Guess!!!"
    attempts = connection.recv(80)
    print attempts, "attempts were needed"
    connection.close()


def wrong_guess():
    global guess
    guess = (int(raw_input("Make another guess...")))
    connection.send(guess)
    print connection.recv(80)


create_and_bind_socket()
print "Welcome to the Number-Guessing game!!!!"
print "Please type a number between 0 and 10`. If you find it then you win! So..."

while True:
    guess = raw_input("What's the Number I am looking for?")

    connection.send(guess)
    serverAnswer = connection.recv(80)
    if serverAnswer == "No":
        wrong_guess()
    if serverAnswer == "Yes":
        successful_try()
