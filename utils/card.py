""" In this part :
Create a class called Symbol with two attributes:

color which is a string.
icon which is a single character out of this list [♥, ♦, ♣, ♠].
1.2 Card
In the same file, create a class Card that inherits from Symbol and add an attribute:

value which is a string (one of ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K'])"""

from typing import List
class Symbol :
    def __init__(self, color : str, icon : str):
        self.color = color
        self.icon = icon 

    def __str__(self) :
        return f"The symbol is {self.color} and {self.icon}"

class Card(Symbol) : 
    def __init__(self, color : str, icon : str, value : str) :
        super().__init__(color, icon)
        self.value = value 
    def __str__(self) :
        return f"the card is {self.value}, {self.color}, {self.icon}"
