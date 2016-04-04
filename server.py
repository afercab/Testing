import socket
import random

l = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
l.bind(("127.0.0.1", 4008))
print "Waiting..."
print "Connection from", ca
while True:
  (s,  ca)  =  l.accept()
  print  "Connection  from",  ca
  print  s.recv(80)
  answer = random.randrange(0,10)
  attempts = 0
  guess = s.recv(80)
  guess = int(guess)
  while answer != guess :
    attempts = attempts + 1
    if( answer > guess ):
        s.send("No")
    if( answer < guess ):
        s.send("No") 
    if( answer == guess ):
        s.send("Yes")
        s.send(attempts)
        break;
    guess = int(s.recv(80))
    s.close()
