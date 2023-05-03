import random
from replit import clear


def calculate(cards):
  total = 0
  for card in cards:
    plain_card = card[1::]
    if plain_card == "K" or plain_card == "Q" or plain_card == "J":
      plain_card = 10
      total += plain_card
    elif plain_card == "A":
      plain_card = 11
      total += plain_card
    else:
      total += int(plain_card)

    if total == 21 and len(cards) == 2:
      return 0

  if total > 21:
    for card in cards:
      plain_card = card[1::]
      if plain_card == "A":
        total -= 10
        if total < 22:
          break
  return total


def dealCards():

  deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
  pwint = ['♠', '♥', '♦', '♣']

  card = random.choice(deck)
  power = random.choice(pwint)
  power_card = f"{power}{card}"

  return power_card


def compare(user_score, ai_score, p_card, ai_card):

  if user_score == ai_score:
    return "DRAW"
  elif ai_score == 0:
    return "YOU LOSE! AI BLACKJACK!"
  elif user_score == 0:
    return "YOU WIN! BLACKJACK!"
  elif user_score > 21:
    return "YOU LOSE! BUSTED!"
  elif ai_score > 21:
    return "YOU WIN! AI BUSTED!"
  elif user_score < 22 and len(p_card) == 5:
    return "BINGO 5x"
  elif ai_score < 22 and len(ai_card) == 5:
    return "AI BINGO 5x"
  elif user_score > ai_score:
    return "YOU WIN!"
  elif ai_score > user_score:
    return "YOU LOSE"


def gameStart():
  print('''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/                  
    ''')
  player_cards = []
  ai_cards = []
  is_game_over = False

  for _ in range(2):
    player_cards.append(dealCards())
    ai_cards.append(dealCards())

  player_score = calculate(player_cards)
  ai_score = calculate(ai_cards)
  print(f"Your Cards : {player_cards} and Current Score : {player_score}")
  print(f"AI First Card : {ai_cards[0]}\n")

  while not is_game_over:
    if player_score == 0 or ai_score == 0 or player_score > 21 or len(
        player_cards) == 5:
      is_game_over = True
    else:
      should_deal = input("Type 'y' to get another card, or 'n' : ")
      if should_deal == "y":
        player_cards.append(dealCards())
        player_score = calculate(player_cards)
        print(
          f"Your Cards : {player_cards} and Current Score : {player_score}")
      else:
        is_game_over = True

  if player_score > 21 or len(player_cards) == 5:
    print()
  else:
    while ai_score != 0 and ai_score < 17 and len(ai_cards) < 5:
      ai_cards.append(dealCards())
      ai_score = calculate(ai_cards)

  print()
  print(f"Your Cards : {player_cards}")
  print(f"AI Cards : {ai_cards}")
  print()
  print(compare(player_score, ai_score, player_cards, ai_cards))
  print()


while input("Play a game of BLACKJACK? Type 'y' or 'n' : ").lower() == "y":
  print()
  gameStart()
