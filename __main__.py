# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright © 2021-present demiurge

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import datetime
import random_card_picker

from coin_flipper import Coins
from lucille_clifton import Fullness
from random_number_generator import RandomNumbers

print("I'm Happy Hazard (v0.1.1-77).")
print("Here's what I can do: ")
print("- flip a coin")
print("- generate a random number")
print("- pick a card")
print("- write a poem")
choice = input("What would you like to do? [card/coin/num/poem]: ")


def card():
    """
    """

    time_started = datetime.datetime.now()

    time_finished = datetime.datetime.now()

    time_elapsed = time_finished - time_started

    print(random_card_picker.one_random_card())
    print(f"About {time_elapsed}")


def coin():
    """
    """

    time_started = datetime.datetime.now()

    time_finished = datetime.datetime.now()

    time_elapsed = time_finished - time_started

    coins = Coins()

    print(coins.one_coin_flip())
    print(f"About {time_elapsed}")


def full():
    """
    """

    time_started = datetime.datetime.now()

    full = Fullness()
    line1 = full.blessing_the_boats()
    line2 = full.cutting_greens()
    line3 = full.nineteen_ninety_four()
    line4 = full.blessing_the_boats()
    line5 = full.cutting_greens()
    line6 = full.nineteen_ninety_four()

    time_finished = datetime.datetime.now()
    time_elapsed = time_finished - time_started

    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    print(f"About {time_elapsed}")


def num():
    """
    Asks the user for the lowest and highest possible numbers, gets a
    timestamp of when the random number started generating, and assigns the
    RandomNumbers() class to a variable, and passes the user input through
    its one_random_number() function. It then gets a timestamp of when the
    random number was generated, and determines how much time had elapsed.
    Both the random number and the elapsed time are then show to the user.
    """

    minimum_number = input("What is the minimum number?: ")
    maximum_number = input("What is the maximum number?: ")

    time_started = datetime.datetime.now()

    randnum = RandomNumbers()
    random_number = randnum.one_random_number(minimum_number, maximum_number)

    time_finished = datetime.datetime.now()
    time_elapsed = time_finished - time_started

    print(random_number)
    print(f"About {time_elapsed}")


def main():
    """
    """

    global choice

    if choice == "card":
        card()

    elif choice == "coin":
        coin()

    elif choice == "num":
        num()

    elif choice == "poem":
        full()

    else:
        pass


if __name__ == "__main__":
    main()
