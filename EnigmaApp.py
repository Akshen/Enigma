
# -'''- coding: utf-8 -'''-
 
import sys,os
import tkMessageBox
import yaml
from textwrap import dedent
from Tkinter import * 
from KeyValidator import *
from Decrypt import *
from Encrypt import *
from tkFileDialog import askopenfilename, askdirectory


class Enigma:
	"""Main class which creates frame and all the widgets"""
	def __init__(self, master):
		master.minsize(width=468, height=276)
		master.maxsize(width=768, height=576)
		frame = Frame(master)

		self.label_keys = Label(text="KEYS:", font="-weight bold")
		self.label_keys.place(x=90,y=30)
		
		#For Keys
		self.textinput1 = Entry(width=3)
		self.textinput1.place(x=141,y=30)
		self.textinput2 = Entry(width=3)
		self.textinput2.place(x=180,y=30)
		self.textinput3 = Entry(width=3)
		self.textinput3.place(x=221,y=30)
		# self.btn_4 = Button(text='Check',command=self.validate)
		# self.btn_4.place(x=270,y=27)
		
		self.textinput = Entry(width=24)
		self.textinput.place(x=90,y=60)
		
		self.btn_3 = Button(text='Browse',command=self.fileManager)
		self.btn_3.place(x=320,y=60)

		#For Filename
		self.textinput4 = Entry(width=18)
		self.textinput4.place(x=90,y=110)
		self.label_outputfile = Label(
			text='Enter Name for output file(default Encrypted.txt/Decrypted.txt)'
			)
		self.label_outputfile.place(x=45,y=90)

		frame.pack()
		self.btn_1 = Button(frame, text='Encrypt',command=self.Encryptor)
		self.btn_1.pack(pady=150,side=LEFT)

		self.btn_2 = Button(frame, text='Decrypt',command=self.Decryptor)
		self.btn_2.pack(pady=150,side=RIGHT)
		self.flag = 0
		


	def validate(self):
		try:
			self.key_one = int(self.textinput1.get())
			self.key_two = int(self.textinput2.get())
			self.key_three = int(self.textinput3.get())
			
		except:
			tkMessageBox.showinfo("Enigma",
				"Please Enter All Keys" )

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
		self.key_one = self.textinput1.get()
		self.key_two = self.textinput2.get()
		self.key_three = self.textinput3.get()
		self.filename = self.textinput4.get()

		if len(self.key_one) == 0 or len(self.key_two) == 0 \
			or len(self.key_three) == 0:

			tkMessageBox.showinfo("Enigma",
				"Please enter Valid Keys" )
			return 0

		#Validating Keys
		validate_obj = KV()
		self.flag = validate_obj.keyvalidator(int(self.key_one),
					int(self.key_two),int(self.key_three))

		if self.flag == 0: return 0

		#Check Path
		if len(self.path) == 0:
			tkMessageBox.showerror("Enigma", 
				"Please Give a Input file.")
			return 0

		#Output Filename for Decrypted File
		if len(self.filename) == 0:
			self.filename = None

		if self.flag:
			Decrypt_obj = D()
			self.return_val = Decrypt_obj.Decrypt(self.path,int(self.key_one),
							int(self.key_two),int(self.key_three),self.filename)

			if self.return_val:	
				self.textinput.delete(0,END)
				self.textinput1.delete(0,END)
				self.textinput2.delete(0,END)
				self.textinput3.delete(0,END)
				self.textinput4.delete(0,END)
			else:
				tkMessageBox.showerror(
				"Enigma","Please give Input File "
				)

		
	def Encryptor(self):
		self.path = self.textinput.get()
		self.key_one = self.textinput1.get()
		self.key_two = self.textinput2.get()
		self.key_three = self.textinput3.get()
		self.filename = self.textinput4.get()

		if len(self.key_one) == 0 or len(self.key_two) == 0 \
			or len(self.key_three) == 0:

			tkMessageBox.showinfo("Enigma",
				"Please enter Valid Keys" )
			return 0

		#Validating Keys
		validate_obj = KV()
		self.flag = validate_obj.keyvalidator(int(self.key_one),
					int(self.key_two),int(self.key_three))

		if self.flag == 0: return 0

		#Check Path
		if len(self.path) == 0:
			tkMessageBox.showerror("Enigma", 
				"Please Give a Input file.")
			return 0

		#Output Filename for Encrypted File
		if len(self.filename) == 0:
			self.filename = None	

		if self.flag:
			Encrypt_obj = E()
			self.return_val = Encrypt_obj.Encrypt(self.path,int(self.key_one),
							int(self.key_two),int(self.key_three),self.filename)

			if self.return_val:	
				self.textinput.delete(0,END)
				self.textinput1.delete(0,END)
				self.textinput2.delete(0,END)
				self.textinput3.delete(0,END)
				self.textinput4.delete(0,END)
			else:
				tkMessageBox.showerror(
				"Enigma","Please give Input File "
				)

def main():
	root = Tk()
	root.wm_title("Enigma")
	app = Enigma(root)
	root.mainloop()

if __name__ == '__main__':
	main()