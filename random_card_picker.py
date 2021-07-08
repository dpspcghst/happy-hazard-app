import os
import random

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "clover_suit.txt")) as f:
    clover_suit = [card.rstrip('\r\n ') for card in f.readlines() if card != ""]

with open(os.path.join(dir_path, "diamond_suit.txt")) as f:
    diamond_suit = [card.rstrip('\r\n ') for card in f.readlines() if card != ""]

with open(os.path.join(dir_path, "heart_suit.txt")) as f:
    heart_suit = [card.rstrip('\r\n ') for card in f.readlines() if card != ""]

with open(os.path.join(dir_path, "spade_suit.txt")) as f:
    spade_suit = [card.rstrip('\r\n ') for card in f.readlines() if card != ""]

all_cards = clover_suit + diamond_suit + heart_suit + spade_suit


def one_random_card():
    """
    """

    choice = random.choice(all_cards)

    return choice
