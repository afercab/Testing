import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 4009))

print "Welcome to the Number-Guessing game!!!!"
print "Please type a number between 0 and 10`. If you find it then you win! So..."

while True:
    guess = raw_input("What's the Number I am looking for?")

    s.send(guess)
    serverAnswer = s.recv(80)
    if serverAnswer == "No":        
        guess = (int(raw_input("Make another guess...")))
        s.send(guess)
        print s.recv(80)
    if serverAnswer == "Yes":
        print "Nice Guess!!!"
        attempts = s.recv(80)
        print attempts, "attempts were needed"
        s.close()
        
