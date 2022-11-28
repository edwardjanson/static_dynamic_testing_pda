import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    

    def test_card_is_ace(self):
        card_game = CardGame()
        ace = Card("hearts", 1)
        self.assertEqual(1, card_game.check_for_ace(ace))
    

    def test_highest_card(self):
        card_game = CardGame()
        card1 = Card("spades", 10)
        card2 = Card("clubs", 8)
        self.assertEqual(card1, card_game.highest_card(card1, card2))
    
    
    def test_cards_total(self):
        card_game = CardGame()
        cards = [Card("diamonds", 1), Card("clubs", 2), Card("spades", 3)]
        self.assertEqual("You have a total of 6", card_game.cards_total(cards))
        
