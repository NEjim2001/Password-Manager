from encryption import Encryption, SEED

encryption = Encryption(SEED)


class User:
    """
    A class for handling user behavior
    """

    def login(self, passcode):
        """
        Method to check if user's input passcode matches stored passcode

        """
        stored_passcode = self.get_passcode()
        if passcode == stored_passcode:
            return True

    def set_passcode(self, passcode):
        """
        Method to set user passcode if passcode is missing

        """
        with open("application_data/passcode_data.txt", "w") as data_file:
            encrypted_data = encryption.encrypt(passcode)
            data_file.write(encrypted_data)

    def get_passcode(self):
        """
        Method to get stored passcode if it exists

        """
        with open("application_data/passcode_data.txt", "r") as data_file:
            data = data_file.read()
            decrypted_data = encryption.decrypt(data, SEED)
            return decrypted_data
