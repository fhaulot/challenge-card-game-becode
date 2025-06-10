"""In player.py create a class Player that contains these attributes:

cards which is a list of Card. (you will need to import Card from card.py). In a real card game, this is equivalent to the cards that the player has in his hands.
turn_count which is an int starting a 0.
number_of_cards which is an int starting at 0.
history which is a list of Card that will contain all the cards played by the player.
And some methods:

play() that will:
randomly pick a Card in cards.
Add the Card to the Player's history.
Print: {PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}.
Return the Card.


Create a Deck class that contains:

An attribute cards which is going to contain a list of object of Card.
A fill_deck() method that will fill cards with a complete card game (an instance of 'A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K' for each possible symbol [♥, ♦, ♣, ♠]). Your deck should contain 52 cards at the end.
A shuffle() method that will shuffle all the list of cards.
A distribute() that will take a list of Player as parameter and will distribute the cards evenly between all the players."""

from card.py import Card

turn_count = int(0)
number_of_cards = int(0)
history = Card[(contain all the cards played by the player)]

from typing import List
from random import shuffle
















class Deck : 
    icons = [("red","♥"),("red","♦"),("black","♣"), ("black","♠")]
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
   
    
    def __init__(self):
        self.deck : list[Card]= []
        
    
    def fill_deck(self) :
        icons = [("red","♥"),("red","♦"),("black","♣"), ("black","♠")]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for color, icon in icons  : 
            for value in values : 
                card = Card(color, icon, value)
                self.deck.append(card)
    
    def shuffle(self) : 
        return shuffle(self.deck)
    
    def distribute(self) :
        return 
