import os
import re
import tkinter.messagebox as messagebox

class Decryptor:
    """
    A class to decrypt encrypted files using a three-key decryption algorithm.

    The decryption process involves three steps:
    1. Rearrange the characters of the encrypted string using the third key.
    2. Perform a custom swap operation based on the second key.
    3. Rearrange the characters again using the first key.

    The decrypted text is then written to a new file with the specified name.
    """

    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.combo_strings = ["ad456bc78gqrstMNGHIJpOPhmnoDEFQRuvwxyzijklABef23CKLSTU1VWXYZ09"] * 3

    def decrypt_file(self, input_path, key1, key2, key3, output_name=None):
        """
        Decrypt the contents of an encrypted file using the provided keys and write the decrypted text to a new file.

        Args:
            input_path (str): The path to the encrypted file.
            key1 (int): The first decryption key (0-62).
            key2 (int): The second decryption key (0-62).
            key3 (int): The third decryption key (0-62).
            output_name (str, optional): The desired name for the decrypted file. If not provided, defaults to "Decrypted.txt".

        Returns:
            bool: True if the decryption was successful, False otherwise.
        """
        if not os.path.exists(input_path):
            messagebox.showerror("Enigma", "Input file does not exist")
            return False

        self._initialize_combo_strings(key3, key2, key1)

        try:
            with open(input_path, 'r') as encrypted_file:
                encrypted_text = encrypted_file.read()

            decrypted_text = self._decrypt_text(encrypted_text)

            output_name = self._get_valid_output_name(output_name)

            with open(output_name, 'w') as decrypted_file:
                decrypted_file.write(decrypted_text)

            messagebox.showinfo("Enigma", f"{output_name} created successfully")
            return True

        except Exception as e:
            messagebox.showerror("Enigma", str(e))
            return False

    def _initialize_combo_strings(self, key3, key2, key1):
        """
        Initialize the combo strings based on the provided keys.

        Args:
            key3 (int): The third decryption key (0-62).
            key2 (int): The second decryption key (0-62).
            key1 (int): The first decryption key (0-62).
        """
        self.combo_strings[2] = self._rearrange_string(self.combo_strings[2], 62 - key3)
        self.combo_strings[1] = self._swap_string(self.combo_strings[1], key2)
        self.combo_strings[0] = self._rearrange_string(self.combo_strings[0], key1)

    def _decrypt_text(self, encrypted_text):
        """
        Decrypt the given encrypted text using the three-step decryption process.

        Args:
            encrypted_text (str): The encrypted text to be decrypted.

        Returns:
            str: The decrypted text.
        """
        # Step 1: Rearrange characters using the third combo string
        decrypted_text = self._translate_string(encrypted_text, self.combo_strings[2])

        # Step 2: Perform custom swap operation using the second combo string
        decrypted_text = self._translate_string(decrypted_text, self.combo_strings[1])

        # Step 3: Rearrange characters using the first combo string
        decrypted_text = self._translate_string(decrypted_text, self.combo_strings[0])

        return decrypted_text

    def _rearrange_string(self, string, key):
        """
        Rearrange the characters of the given string based on the provided key.

        Args:
            string (str): The string to be rearranged.
            key (int): The key used for rearranging the characters (0-62).

        Returns:
            str: The rearranged string.
        """
        temp = string[key:] + string[:key]
        return temp

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

        temp_one = string[point_one:point_two]
        temp_two = string[:point_one] + string[point_two:]
        string = temp_two + temp_one
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
        translation_table = str.maketrans(combo_string, self.alphabet)
        return string.translate(translation_table)

    def _get_valid_output_name(self, output_name):
        """
        Get a valid output file name, handling existing file conflicts and invalid characters.

        Args:
            output_name (str, optional): The desired name for the output file. If not provided, defaults to "Decrypted.txt".

        Returns:
            str: A valid output file name.
        """
        if not output_name:
            output_name = "Decrypted.txt"
        else:
            output_name = re.sub(r'[^a-zA-Z0-9_]', '', output_name) + ".txt"

        if os.path.exists(output_name):
            root, ext = os.path.splitext(output_name)
            i = 1
            while os.path.exists(f"{root}_{i}{ext}"):
                i += 1
            output_name = f"{root}_{i}{ext}"

        return output_name