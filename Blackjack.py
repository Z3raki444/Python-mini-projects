import random

# ASCII Art
logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
    |  \/ K|                            _/ |
    `------'                           |__/
"""

cards = [
    {'rank': 'A', 'value': 11},
    {'rank': '2', 'value': 2},
    {'rank': '3', 'value': 3},
    {'rank': '4', 'value': 4},
    {'rank': '5', 'value': 5},
    {'rank': '6', 'value': 6},
    {'rank': '7', 'value': 7},
    {'rank': '8', 'value': 8},
    {'rank': '9', 'value': 9},
    {'rank': '10', 'value': 10},
    {'rank': 'J', 'value': 10},
    {'rank': 'Q', 'value': 10},
    {'rank': 'K', 'value': 10},
]

def deal_card():
    return random.choice(cards).copy()

def calculate_score(hand):
    score = sum(card['value'] for card in hand)
    # Adjust for Aces
    aces = sum(1 for card in hand if card['rank'] == 'A')
    while score > 21 and aces:
      score -= 10
      aces -= 1
    return score

def display_hand(hand, hide_first=False):
    art = []
    for i, card in enumerate(hand):
      if hide_first and i == 0:
        art.append("[??]")
      else:
        art.append(f"[{card['rank']}]")
    return ' '.join(art)

def blackjack():
    print(logo)
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    game_over = False

    while not game_over:
      player_score = calculate_score(player_hand)
      dealer_score = calculate_score(dealer_hand)
      print(f"Your hand: {display_hand(player_hand)}, current score: {player_score}")
      print(f"Dealer's hand: {display_hand(dealer_hand, hide_first=True)}")

      if player_score == 21:
        print("Blackjack! You win!")
        return
      if player_score > 21:
        print("You went over 21. You lose.")
        return

      action = input("Type 'hit' to get another card, 'stand' to pass: ").lower()
      if action == 'hit':
        player_hand.append(deal_card())
      else:
        game_over = True

    # Dealer's turn
    while calculate_score(dealer_hand) < 17:
      dealer_hand.append(deal_card())
    dealer_score = calculate_score(dealer_hand)
    print(f"Dealer's final hand: {display_hand(dealer_hand)}, final score: {dealer_score}")

    if dealer_score > 21:
      print("Dealer went over 21. You win!")
    elif dealer_score == player_score:
      print("Draw!")
    elif player_score > dealer_score:
      print("You win!")
    else:
      print("You lose.")

if __name__ == "__main__":
    while input("Play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
      blackjack()