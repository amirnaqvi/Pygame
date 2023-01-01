import random
botlist = [0,1,2,3]
print("Cricket")
name = input("What's your name? ")
print(f"Hello {name}!,you are going to play cricket with the bot")
print('''Rules of the game:
1.You have to select whether you want to bat first or bowl.
2.Now you have to enter a number from 0 to 3 the bot will enter another.
3.The sum of both the numbers will be the total run on the ball.
4. If you and bot select same number, the batsman will be out.
5. Every player will have 3 wickets.
6. The one who scores maximum runs will win the match.''')
ready = input(f'Are you ready?,{name}! Yes/No: ')
if (ready == 'yes' or ready == "Yes" or ready == "YES"):
  print("Let's star the game.")
  toss = input('What you want to do.Bat/Bowl?: ')
  if toss == 'bat' or toss == "Bat" or toss == "BAT":
    out1 = 0
    runPl = 0
    runB = 0
    while (out1<3):
      plnum = int(input('Enter a number between 0 and 3: '))
      ("Bot has enterd")
      botn = botlist[random.randint(0,3)]
      botnum = int(botn)
      print('Bot has entered:', botnum)
      
      if plnum == botnum:
        print('Out!')
        out1 += 1
      else:
        print("You have scored:", plnum + botnum)
        runPl += plnum + botnum
    print(f"Now you have to bowl!, You have scored {runPL} runs.")
    input('Are you ready?: ')
    out2 = 0
    while (out2<3):
      plnum = int(input('Enter a number between 0 and 3: '))
      ("Bot has enterd")
      botn = botlist[random.randint(0,3)]
      botnum = int(botn)
      print('Bot has entered:', botnum)
      
      if plnum == botnum:
        print('Out!')
        out2 += 1
      else:
        print("Bot has scored:", plnum + botnum)
        runB += plnum + botnum
    print(f'You have scored: {runPl} runs./n Bot have scored {runB} runs')
    if runPl > runB:
      print(f'{name} has won the match!/n  Congractulations, Hope you enjoyed the game.')
    else:
      print('Bot has won the match!/n Better luck next time./n Hope you enjoyed the game.')
      
  else:
    out3 = 0
    runPl = 0
    runB = 0
    while (out3<3):
      plnum = int(input('Enter a number between 0 and 3: '))
      botn = botlist[random.randint(0,3)]
      botnum = int(botn)
      print('Bot has entered:', botnum)
      
      if plnum == botnum:
        print('Out!')
        out3 += 1
      else:
        print("Bot has scored:", plnum + botnum)
        runB += plnum + botnum
    print(f"Now you have to bat!, Bot has scored {runB} runs.")
    input('Are you ready?: ')
    out4 = 0
    while (out4<3):
      plnum = int(input('Enter a number between 0 and 3: '))
      botn = botlist[random.randint(0,3)]
      botnum = int(botn)
      print('Bot has entered:', botnum)
      
      if plnum == botnum:
        print('Out!')
        out4 += 1
      else:
        print("You have scored:", plnum + botnum)
        runPl += plnum + botnum
    print(f'You have scored: {runPl} runs./n Bot have scored {runB} runs')
    if runPl > runB:
      print(f'''{name} has won the match!
      Congractulations, Hope you enjoyed the game.''')
    else:
      print('''Bot has won the match!
      Better luck next time.
      Hope you enjoyed the game.''') 
    print('Thankyou!')
else:
  print('Thankyou!')

