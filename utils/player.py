
"""I am getting the Card class from the card file, the typing module to create list type and the random module to shuffle the card 
while in the deck class"""
from card import Card
from typing import List
import random

class Player :
    """ That class will set one player (we think about getting four players) It will mainly define how to get a list of cards and how to play
     to distribute each time a card until the desk is empty."""
    def __init__(self, name: str):
        """ Function that will define the attributes of the class. In this one, we need to define a lot with :
        :param number_one: .
        :param number_two: .
        :return: . 
        """
        self.name = name
        self.cards : list[Card] = []
        self.turn_count : int = 0
        self.number_of_cards : int = 0
        self.history : list[Card] = []
    
    
    #defining the string of the class
    def __str__(self):
        return f"the player has {self.number_of_cards} in hand"
    
    
    def play(self) : 
        """ Function that will play the card game, 
        :attribute number_one: pick a card in the desk
        :attribute number_two: remove the chosen card from the deck
        :attribute number_three: appending the card history of the player
        :attribute number_four: removing the chosen card from the hand of the player
        :printing and return: 
    """
        chosen_card = random.choice(self.cards)
        self.cards.remove(chosen_card)
        self.history.append(chosen_card)
        self.number_of_cards -= 1
        print(f"{self.name}, {self.turn_count} played : {chosen_card})
        return chosen_card


class Deck : 
    #converting the deck into a empty list with typing
    def __init__(self):
        self.deck : list[Card]= []
        
    """I am doing the list to append the self.deck list. Then a loop calling the Card class. 
    As we have attribute a color to each icon, we might have 52 cards in the list"""
    def fill_deck(self) :
        icons = [("red","♥"),("red","♦"),("black","♣"), ("black","♠")]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for color, icon in icons  : 
            for value in values : 
                card = Card(color, icon, value)
                self.deck.append(card)
    
    """Now the list is complete, we use shuffle (import from random) to "mix" the list. """
    def shuffle(self) : 
        return shuffle(self.deck)
    
    
    def distribute(self, players: List[Player]) :
        """installed numpy to split the list and trying to add it to the players list "self.cards". In the attrbutes of numpy I put the list 
        and 4 to
     display use it. But then I tried another method """
        """self.cards = np.array_split(self.deck, 4)"""
        total_cards_per_person = len(self.deck) // len(players)
        
        for player in players:
            for i in range(total_cards_per_person):
                chosen_card = self.deck[i]
                player.cards.append(chosen_card)
                self.deck.remove(chosen_card)

    def __string__(self) : 
        return f"The deck has {len(self.deck)} cards in it"



















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
