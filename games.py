
import random

money = 100

#flipping coin function
def coin_flip (bet_money, bet_name):
  global money
  coin_flip = random.randint(1, 2)
  if bet_money < 0:
    print("Yuo can't bet negative amount!")
    return 0
  if bet_money > money:
      print("Your balance excedes bet!")
      return 0
  if (coin_flip == 1) and (bet_name.title() == "Heads"):
    print('You bet Heads and you won '+ str(bet_money) +'$!')
    return bet_money
  elif (coin_flip == 2) and (bet_name.title() == "Tails"):
    print('You bet Tails and you won '+ str(bet_money) +'$!')
    return bet_money
  else:
    print('Your bet was not correct and you lost '+ str(bet_money) +'$!')
    return -bet_money
    


#cho_han function
def cho_han(bet_money, bet_name):
  global money
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  sum_of_dices = dice1 + dice2
  if bet_money < 0:
    print("Yuo can't bet negative amount!")
    return 0
  if bet_money > money:
      print("Your balance excedes bet!")
      return 0
  if(sum_of_dices % 2 == 0 and bet_name.title() == "Even"):
    print('You bet Even and you won '+ str(bet_money) +'$!')
    return bet_money
  elif(sum_of_dices % 2 != 0 and bet_name.title() == "Odd"):
    print('You bet Odd and you won '+ str(bet_money) +'$!')
    return bet_money
  else:
    print('Your guess was not correct and you lost '+ str(bet_money) +'$!')
    return -bet_money



# pick the random card function
def card_choice (bet_money):
  if bet_money < 0:
    print("Yuo can't bet negative amount!")
    return 0
  if bet_money > money:
    print("Your balance excedes bet!")
    return 0
  cards = list(range(1, 12))*4
  player_card = cards[random.randint(0, len(cards)-1)]
  print('Player card is: ' + str(player_card))
  cards.remove(player_card)
  opponent_card = cards[random.randint(0, len(cards)-1)]
  print('Opponent card is: ' + str(opponent_card))
  if (player_card > opponent_card):
    print('Your card ' + str(player_card) + ' is greater than opponent'+ 's card ' + str(opponent_card) + ' and you won ' + str(bet_money) +'$!')
    return bet_money
  elif (player_card < opponent_card):
    print('Your card ' + str(player_card) + ' is lower than opponent' +'s ' + 'card ' + str(opponent_card) + ' and you lost ' + str(bet_money) +'$!')
    return -bet_money
  else:
    print("There is w a draw!")
    return 0

#roulette function
def roulette(bet_money, bet):
  global money
  if bet_money < 0:
    print("Yuo can't bet negative amount!")
    return 0
  if bet_money > money:
    print("Your balance excedes bet!")
    return 0
  roulette_numbers = list(range(0, 37))
  winning_number = roulette_numbers[random.randint(0, len(roulette_numbers)-1)]
  print('The wining number is: ' + str(winning_number))
  if(winning_number ==  bet):
    print('You bet a correct number and you won '+ str(bet_money*35) +'$!')
    return bet_money * 35
  if(winning_number % 2 == 0 and bet == "even"):
    print('You bet Even and you won '+ str(bet_money) +'$!')
    return bet_money
  elif(winning_number % 2 != 0 and bet == "odd"):
    print('You bet Odd and you won '+ str(bet_money) +'$!')
    return bet_money
  else:
    print('Your guess was not correct and you lost '+ str(bet_money) +'$!')
    return -bet_money

# Call your game of chance functions here
money += coin_flip(10, "taiLS");
print('Your balance is :' +  str(money))
money += cho_han(10, "oDd");
print('Your balance is :' +  str(money))
money += card_choice(10)
print('Your balance is :' +  str(money))
money += roulette(10, 12)
print('Your balance is :' +  str(money))
