name = input('please enter your name -->  ')
print('hello' , name, 'welcome to this choice based adventure game')
play = input('are you ready to play? -->')
if play.lower() == "yes":
  print('Great!')
  choice = input('I deadly virus has spread across the globe, turning everyone into zombies with very few survivors , you with your two friends are hiding in a building, but you need supplies..... (GET OUT/ STAY) -->')
  if choice.lower() == "stay":
    print('you tried to stay but run out of supplies, the building was also captured by zombies....... GAME OVER!')
    quit
  elif choice.lower() == "getout":
    print('you decided to go out for supplies')
    choice = input('there is a supermarket nearby and a Mall a few miles away in the city where would you go? (MARKET/ MALL) --> ')
    if choice.lower() == "market":
      print("the market has no supplies left and is covered by the walking dead..... looks like you've come to an END")
    elif choice.lower() == "mall":
      print('You decided to go to the mall, it is a few miles away but will have enough supplies')
      choice = input('while walking towards the mall you see a horde of zombies in the front, you turn ....(LEFT/RIGHT) -->')
      if choice.lower() == 'left':
        print('you start runnnig towards left, you see a stranger with a jeep asking you to jump in... (GETIN/RUN) -->')
        choice = input()
        if choice.lower() == "run":
          print('you decided to keep running but cant go far, you come to an END')
          quit
        elif choice.lower() =='getin':
          print('you get in to the jeep and reach a safe house... YOU WIN!!')
      elif choice.lower() == "right":
        print('you run towards right, when the building in front of you collapses, engulfing you all...... GAME OVER')
        quit
else:
  quit