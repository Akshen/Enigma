#!/usr/bin/python
# -'''- coding: utf-8 -'''-
 
import sys,os
import tkMessageBox
from Tkinter import * 
from Decrypt import *
from Encrypt import *
from tkFileDialog import askopenfilename,askdirectory

class Enigma:
	"""Main class which creates frame and all the widgets"""
	def __init__(self, master):
		master.minsize(width=468, height=276)
		master.maxsize(width=768, height=576)
		frame = Frame(master)
		
		self.textinput = Entry(width=25)
		self.textinput.place(x=90,y=60)
		
		self.btn_3 = Button(text='Browse',command=self.fileManager)
		self.btn_3.place(x=300,y=60)

		frame.pack()
		self.btn_1 = Button(frame, text='Encrypt',command=self.Encryptor)
		self.btn_1.pack(pady=100,side=LEFT)

		self.btn_2 = Button(frame, text='Decrypt',command=self.Decryptor)
		self.btn_2.pack(pady=100,side=RIGHT)

	
	#Browse Button reads and sets path on Entry
	def fileManager(self):
		self.filepath = askopenfilename(initialdir='/home/ronin',filetypes=[("Text files","*.txt")])
		self.directory = os.path.join(self.filepath)
		self.textinput.insert(0,self.directory)

		

	def Decryptor(self):
		self.path = self.textinput.get()
		Decrypt_obj = D()
		Decrypt_obj.Decrypt(self.path)
		self.textinput.delete(0,END)



	def Encryptor(self):
		self.path = self.textinput.get()
		Encrypt_obj = E()
		Encrypt_obj.Encrypt(self.path)
		self.textinput.delete(0,END)
		
		

	



def main():
	
	root = Tk()
	root.wm_title("Enigma")
	app = Enigma(root)
	root.mainloop()


if __name__ == '__main__':
	main()