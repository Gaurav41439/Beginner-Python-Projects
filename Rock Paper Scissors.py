from getpass import getpass
print('how many rounds?')
t = input()
p1 = int(0)
p2 = int(0)
for t in range(int(t)):
  print('put your input as R P or S')

  player1 = getpass()
  player2 = getpass()
  if player1== "R":
    if player2 == "R":
      print('tie')
    elif player2=="S":
      print('player1 wins')
      p1 = p1+1
    else:
      print('player2 wins')
      p2 = p2+1

  elif player1 =='S':
    if player2== 'R':
      print('player2 wins')
      p2 = p2+1
    elif player2 =='S':
      print('tie')
    else:
      print('player1 wins')
      p1 = p1+1
  elif player1== 'P':

    if player2 == 'S':
      print('player2 wins')
      p2 = p2+1
    elif player2 == 'R':
      print('player1 wins')
      p1 = p1+1
    else:
      print('tie')

print( "score is:")
print('p1 got' + str(p1))
print('p2 got' + str(p2))
if p1 > p2:
  print('player1 is the winner!')
else:
  print('player 2 is the winner!')  