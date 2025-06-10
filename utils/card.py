
"""defining the types and the attributes"""
class Symbol :
    
    def __init__(self, color : str, icon : str) -> None :
        """ Function that will define the attribute of the class.

        :param number_one: color = A str that will be extract from a list in the deck class.
        :param number_two: icon = A str that will be extract from a list in the deck class and merge with the color value."""
        self.color = color
        self.icon = icon 

    def __str__(self) -> None :
        """ Function that will print the value of the Symbol class calling the color and the icon 
        :return : a string with color and icon """
        return f"The symbol is {self.color} and {self.icon}"
      
class Card(Symbol) : 
    """Class defining the Card. It will be called in the others files to set lists of cards"""
    def __init__(self, color : str, icon : str, value : str) -> None :
        super().__init__(color, icon)
        self.value = value 
        """ Function that will define the parameters of the class Card.

        :param number_one: we call class Symbol by using super and get color and icon.
        :param number_two: we define the value who will be set in the class Deck.
        :return: ."""
    #defining string method to see a better result
    def __str__(self) -> None :
        return f"the card is {self.value}, {self.color}, {self.icon}"
    """ Function that will print the value of the Card  .
        :return: a string with value, color and icon ."""
