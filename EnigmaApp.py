# -'''- coding: utf-8 -'''-

import os
import tkinter as tk
from tkinter import messagebox, filedialog

from key_validator import KeyValidator
from decrypt import Decrypt
from encrypt import Encrypt


class Enigma:
    """Main class which creates frame and all the widgets"""

    def __init__(self, master):
        master.minsize(width=468, height=276)
        master.maxsize(width=768, height=576)
        master.title("Enigma")

        frame = tk.Frame(master)
        frame.pack()

        # Label and entries for keys
        label_keys = tk.Label(frame, text="KEYS:", font="-weight bold")
        label_keys.grid(row=0, column=0, padx=10, pady=10)

        self.key_entries = [
            tk.Entry(frame, width=3) for _ in range(3)
        ]
        for i, entry in enumerate(self.key_entries):
            entry.grid(row=0, column=i + 1, padx=5)

        # Input file path entry and browse button
        self.input_path = tk.Entry(frame, width=24)
        self.input_path.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        browse_btn = tk.Button(frame, text="Browse", command=self.browse_file)
        browse_btn.grid(row=1, column=3, padx=10)

        # Output file name entry and label
        label_output_file = tk.Label(
            frame,
            text="Enter Name for output file (default Encrypted.txt/Decrypted.txt)",
        )
        label_output_file.grid(row=2, column=0, columnspan=4, padx=10, pady=5)

        self.output_name = tk.Entry(frame, width=18)
        self.output_name.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

        # Encrypt and Decrypt buttons
        encrypt_btn = tk.Button(frame, text="Encrypt", command=self.encrypt_file)
        encrypt_btn.grid(row=4, column=0, padx=10, pady=10)

        decrypt_btn = tk.Button(frame, text="Decrypt", command=self.decrypt_file)
        decrypt_btn.grid(row=4, column=3, padx=10, pady=10)

    def browse_file(self):
        """Open a file dialog to select input file"""
        file_path = filedialog.askopenfilename(
            initialdir=os.path.expanduser("~"), filetypes=[("Text files", "*.txt")]
        )
        if file_path:
            self.input_path.delete(0, tk.END)
            self.input_path.insert(0, file_path)

    def get_keys(self):
        """Retrieve and validate user-entered keys"""
        keys = [entry.get() for entry in self.key_entries]
        if not all(keys):
            messagebox.showinfo("Enigma", "Please enter all keys")
            return None

        try:
            keys = [int(key) for key in keys]
        except ValueError:
            messagebox.showinfo("Enigma", "Keys must be integers")
            return None

        validator = KeyValidator()
        if not validator.validate_keys(*keys):
            messagebox.showinfo("Enigma", "Invalid keys")
            return None

        return keys

    def encrypt_file(self):
        """Encrypt the selected input file"""
        keys = self.get_keys()
        if not keys:
            return

        input_path = self.input_path.get()
        if not input_path:
            messagebox.showerror("Enigma", "Please select an input file")
            return

        output_name = self.output_name.get() or "Encrypted.txt"

        try:
            encryptor = Encrypt()
            encryptor.encrypt_file(input_path, *keys, output_name)
            messagebox.showinfo("Success", "File encrypted successfully")
            self.clear_inputs()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decrypt_file(self):
        """Decrypt the selected input file"""
        keys = self.get_keys()
        if not keys:
            return

        input_path = self.input_path.get()
        if not input_path:
            messagebox.showerror("Enigma", "Please select an input file")
            return

        output_name = self.output_name.get() or "Decrypted.txt"

        try:
            decryptor = Decrypt()
            decryptor.decrypt_file(input_path, *keys, output_name)
            messagebox.showinfo("Success", "File decrypted successfully")
            self.clear_inputs()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_inputs(self):
        """Clear all input fields"""
        self.input_path.delete(0, tk.END)
        self.output_name.delete(0, tk.END)
        for entry in self.key_entries:
            entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = Enigma(root)
    root.mainloop()


if __name__ == "__main__":
    main()