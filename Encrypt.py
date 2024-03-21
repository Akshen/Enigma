import os
import re
import tkinter.messagebox as messagebox

class Encryptor:
    """
    A class to encrypt plaintext files using a three-key encryption algorithm.

    The encryption process involves three steps:
    1. Rearrange the characters of the original string using the first key.
    2. Perform a custom swap operation based on the second key.
    3. Rearrange the characters again using the third key.

    The encrypted text is then written to a new file with the specified name.
    """

    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.combo_strings = ["ad456bc78gqrstMNGHIJpOPhmnoDEFQRuvwxyzijklABef23CKLSTU1VWXYZ09"] * 3

    def encrypt_file(self, input_path, key1, key2, key3, output_name=None):
        """
        Encrypt the contents of a file using the provided keys and write the encrypted text to a new file.

        Args:
            input_path (str): The path to the plaintext file.
            key1 (int): The first encryption key (0-62).
            key2 (int): The second encryption key (0-62).
            key3 (int): The third encryption key (0-62).
            output_name (str, optional): The desired name for the encrypted file. If not provided, defaults to "Encrypted.txt".

        Returns:
            bool: True if the encryption was successful, False otherwise.
        """
        if not os.path.exists(input_path):
            messagebox.showerror("Enigma", "Input file does not exist")
            return False

        self._initialize_combo_strings(key1, key2, key3)

        try:
            with open(input_path, 'r') as plaintext_file:
                plaintext = plaintext_file.read()

            encrypted_text = self._encrypt_text(plaintext)

            output_name = self._get_valid_output_name(output_name)

            with open(output_name, 'w') as encrypted_file:
                encrypted_file.write(encrypted_text)

            messagebox.showinfo("Enigma", f"{output_name} created successfully")
            return True

        except Exception as e:
            messagebox.showerror("Enigma", str(e))
            return False

    def _initialize_combo_strings(self, key1, key2, key3):
        """
        Initialize the combo strings based on the provided keys.

        Args:
            key1 (int): The first encryption key (0-62).
            key2 (int): The second encryption key (0-62).
            key3 (int): The third encryption key (0-62).
        """
        self.combo_strings[0] = self._rearrange_string(self.combo_strings[0], key1)
        self.combo_strings[1] = self._swap_string(self.combo_strings[1], key2)
        self.combo_strings[2] = self._rearrange_string(self.combo_strings[2], 62 - key3)

    def _encrypt_text(self, plaintext):
        """
        Encrypt the given plaintext using the three-step encryption process.

        Args:
            plaintext (str): The plaintext to be encrypted.

        Returns:
            str: The encrypted text.
        """
        # Step 1: Rearrange characters using the first combo string
        encrypted_text = self._translate_string(plaintext, self.combo_strings[0])

        # Step 2: Perform custom swap operation using the second combo string
        encrypted_text = self._translate_string(encrypted_text, self.combo_strings[1])

        # Step 3: Rearrange characters using the third combo string
        encrypted_text = self._translate_string(encrypted_text, self.combo_strings[2])

        return encrypted_text

    def _rearrange_string(self, string, key):
        """
        Rearrange the characters of the given string based on the provided key.

        Args:
            string (str): The string to be rearranged.
            key (int): The key used for rearranging the characters (0-62).

        Returns:
            str: The rearranged string.
        """
        temp = string[0:key]
        string = string[key:] + temp
        return string

    def _swap_string(self, string, key):
        """
        Perform a custom swap operation on the given string based on the provided key.

        Args:
            string (str): The string to be swapped.
            key (int): The key used for the swap operation (0-62).

        Returns:
            str: The swapped string.
        """
        mid = 31
        first_half = key // 2
        second_half = key - first_half
        point_one = mid - first_half
        point_two = mid + second_half

        temp_one = string[0:point_one]
        temp_two = string[point_two:]
        string = string[point_one:point_two] + temp_one + temp_two
        return string

    def _translate_string(self, string, combo_string):
        """
        Translate the characters of the given string using the provided combo string.

        Args:
            string (str): The string to be translated.
            combo_string (str): The combo string used for translation.

        Returns:
            str: The translated string.
        """
        translation_table = str.maketrans(self.alphabet, combo_string)
        return string.translate(translation_table)

    def _get_valid_output_name(self, output_name):
        """
        Get a valid output file name, handling existing file conflicts and invalid characters.

        Args:
            output_name (str, optional): The desired name for the output file. If not provided, defaults to "Encrypted.txt".

        Returns:
            str: A valid output file name.
        """
        if not output_name:
            output_name = "Encrypted.txt"
        else:
            output_name = re.sub(r'[^a-zA-Z0-9_]', '', output_name) + ".txt"

        if os.path.exists(output_name):
            root, ext = os.path.splitext(output_name)
            i = 1
            while os.path.exists(f"{root}_{i}{ext}"):
                i += 1
            output_name = f"{root}_{i}{ext}"

        return output_name