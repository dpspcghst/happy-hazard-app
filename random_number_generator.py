# imports modules for timestamps and randomization.
import random


class RandomNumbers():
    """
    """

    def one_random_number(self, minimum_number, maximum_number):
        """
        converts the variables to integers and uses randint from the random module
        to generate a random number between the lowest and highest possible
        numbers.
        """
        generated_number = random.randint(
            int(minimum_number),
            int(maximum_number)
        )

        """
        converts the variables to integers and checks to make sure the generated
        number is between the lowest and highest possible numbers.
        """
        if int(minimum_number) < int(generated_number) < int(maximum_number):

            return generated_number

        else:
            pass
