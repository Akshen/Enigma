#!/usr/bin/python
# -'''- coding: utf-8 -'''-
 
import sys,os
import tkMessageBox
from Tkinter import * 
from KeyValidator import *
from Decrypt import *
from Encrypt import *
from tkFileDialog import askopenfilename,askdirectory

class Enigma:
	"""Main class which creates frame and all the widgets"""
	def __init__(self, master):
		master.minsize(width=468, height=276)
		master.maxsize(width=768, height=576)
		frame = Frame(master)

		self.label = Label(text="KEYS", font="-weight bold")
		self.label.place(x=100,y=30)
		
		self.textinput1 = Entry(width=3)
		self.textinput1.place(x=150,y=30)
		self.textinput2 = Entry(width=3)
		self.textinput2.place(x=185,y=30)
		self.textinput3 = Entry(width=3)
		self.textinput3.place(x=220,y=30)
		self.btn_4 = Button(text='Check',command=self.validate)
		self.btn_4.place(x=270,y=27)
		
		self.textinput = Entry(width=25)
		self.textinput.place(x=90,y=60)
		
		self.btn_3 = Button(text='Browse',command=self.fileManager)
		self.btn_3.place(x=300,y=60)

		frame.pack()
		self.btn_1 = Button(frame, text='Encrypt',command=self.Encryptor)
		self.btn_1.pack(pady=100,side=LEFT)

		self.btn_2 = Button(frame, text='Decrypt',command=self.Decryptor)
		self.btn_2.pack(pady=100,side=RIGHT)
		self.flag = 0
		


	def validate(self):
		self.key_one = int(self.textinput1.get())
		self.key_two = int(self.textinput2.get())
		self.key_three = int(self.textinput3.get())

		validate_obj = KV()
		self.flag = validate_obj.keyvalidator(self.key_one,self.key_two,self.key_three)
		if self.flag:
			tkMessageBox.showinfo("Enigma",
				"KEYS are Valid")


	
	#Browse Button reads and sets path on Entry
	def fileManager(self):
		self.filepath = askopenfilename(initialdir='/home',filetypes=[("Text files","*.txt")])
		self.directory = os.path.join(self.filepath)
		self.textinput.insert(0,self.directory)

		

	def Decryptor(self):

		self.path = self.textinput.get()

		self.key_one = int(self.textinput1.get())
		self.key_two = int(self.textinput2.get())
		self.key_three = int(self.textinput3.get())
		
		Decrypt_obj = D()
		Decrypt_obj.Decrypt(self.path,self.key_one,self.key_two,self.key_three)
		self.textinput.delete(0,END)
		self.textinput1.delete(0,END)
		self.textinput2.delete(0,END)
		self.textinput3.delete(0,END)


	def Encryptor(self):
		self.path = self.textinput.get()
		if self.flag:
			self.key_one = int(self.textinput1.get())
			self.key_two = int(self.textinput2.get())
			self.key_three = int(self.textinput3.get())
		
		Encrypt_obj = E()
		Encrypt_obj.Encrypt(self.path,self.key_one,self.key_two,self.key_three)
		self.textinput.delete(0,END)
		self.textinput1.delete(0,END)
		self.textinput2.delete(0,END)
		self.textinput3.delete(0,END)
		
		

	



def main():
	
	root = Tk()
	root.wm_title("Enigma")
	app = Enigma(root)
	root.mainloop()


if __name__ == '__main__':
	main()