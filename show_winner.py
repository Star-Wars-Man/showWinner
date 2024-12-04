def timeline():
    print("Starting timeline game")
    showGameMenu()
    setUpNewGame()
    play()
    showWinner()

def showGameMenu():
    print("Game Menu")
    number_of_players=input("how many players? max of 8: ")
    bots_on=int(input("Bots? if so how many?: "))
    bots_on=False
    bot_difficulty=10
    return number_of_players

import json
def shuffle_cards(deck):
    # TODO, really shuffle it
    return deck

def setUpNewGame(number_of_players):
    deck=[]
    print("loading game cards...")
    with open('cards.json')as f:
        deck = json.load(f)
    print(f"setting up game for {number_of_players} players")
    starting_player=0
    shuffled_deck=shuffle_cards(deck)
    player_hands=[]
    for i in range(number_of_players):
        player_hand=[shuffled_deck.pop()]
        player_hands.append(player_hand)

    return{
        "player_turn": starting_player,
        "player_hands": player_hands,
        "deck":shuffled_deck
    }


def play(game_settings, starting_game_table):
    #current_player=1
    #while not game_over():
        #take_turn(current_player)
        #current_player=pick_next_player()
    player_hands=starting_game_table["player_hands"]


def showWinner(final_hands):
    winning_player=0
    winning_player_score=0
    for i, hand in enumerate(final_hands):
        print(f" player {i} had {len(hand)} cards!")
        if len(hand)>winning_player_score:
            winning_player=i
            winning_player_score=len(hand)
    print(f"player {winning_player} won!!")


timeline()