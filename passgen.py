import random


class PasswordGen:
    """
    A class for generating random passwords with a mix of letters, numbers, and symbols.
    """

    def __init__(self):
        self.password_list = []

    def generate_password(self):
        """
        Generates a random password with a mix of letters, numbers, and symbols.

        Returns:
        - str: The generated password.
        """
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v',
                   'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R',
                   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        for char in range(nr_letters):
            self.password_list.append(random.choice(letters))

        for char in range(nr_symbols):
            self.password_list += random.choice(symbols)

        for char in range(nr_numbers):
            self.password_list += random.choice(numbers)

        random.shuffle(self.password_list)

        return "".join(self.password_list)

    def reset(self):
        """
        Resets the password list to an empty list.
        """
        self.password_list = []
