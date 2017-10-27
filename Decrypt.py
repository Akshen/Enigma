import tkMessageBox
import os
import re
from string import maketrans


class D:
	''' Decrypt Class'''
	def Decrypt(self,path,key_one,key_two,key_three,filen=None):
		'''This function Decrypts the given inputfile'''

		numalpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

		combo_one = "ad456bc78gqrstMNGHIJpOPhmnoDEFQRuvwxyzijklABef23CKLSTU1VWXYZ09"
		combo_two = "ad456bc78gqrstMNGHIJpOPhmnoDEFQRuvwxyzijklABef23CKLSTU1VWXYZ09"
		combo_three = "ad456bc78gqrstMNGHIJpOPhmnoDEFQRuvwxyzijklABef23CKLSTU1VWXYZ09"
		x, y, z = key_one, key_two, key_three
		filename = filen

		if os.path.exists(path):
			plain_file = open(path,'r')
			file = open("combo_two.txt",'w')
			listline = plain_file.readlines()

			#First Step
			z = 62-z
			temp = combo_three[z:63]
			combo_three = combo_three[0:z]
			temp+=combo_three
			combo_three = temp

			for i in xrange(len(listline)):
				for j in listline[i]:
					table = maketrans(combo_three,numalpha)
					file.write(j.translate(table))

			plain_file.close()
			file.close()

			#Second Step
			file_temp = open("combo_two.txt",'r')
			listline = file_temp.readlines()
			file = open("combo_one.txt",'w')

			mid = 31
			first_half = y/2
			second_half = y-first_half

			point_one = mid-first_half
			point_two = mid + second_half

			temp_one = combo_two[0:point_one]
			temp_two = combo_two[point_two:63]
			combo_two = combo_two[point_one:point_two]
			combo_two +=temp_one
			temp_two +=combo_two
			combo_two = temp_two

			for i in xrange(len(listline)):
				for j in listline[i]:
					table = maketrans(combo_two,numalpha)
					file.write(j.translate(table))

			file_temp.close()
			os.remove("combo_two.txt")
			file.close()

			#Third Step
			file_temp = open("combo_one.txt",'r')
			listline = file_temp.readlines()

			if filename is not None:
				if os.path.exists(filename+".txt"): #Check if Filename already exists
					tkMessageBox.showerror("Enigma",
						"File already exists, please change filename")
					return 0
				else:
					if re.match("^[a-zA-Z0-9_]*$", filename): #Check if Filename is as required
						file = open(filename+".txt", "w")
					else:
						filename = re.sub("[^A-Za-z0-9]+", '', filename) #remove special characters
						file = open(filename+".txt", "w")
			else:
				filename = "Decrypted.txt"
				if os.path.exists(filename): #Check if Filename already exists
					tkMessageBox.showerror("Enigma",
						"File already exists, please change filename")
					return 0
				file = open(filename, "w")

			temp = combo_one[0:x]
			combo_one = combo_one[x:63]
			combo_one +=temp

			for i in xrange(len(listline)):
				for j in listline[i]:
					table = maketrans(combo_one,numalpha)
					file.write(j.translate(table))

			file_temp.close()
			os.remove("combo_one.txt")
			file.close()

			tkMessageBox.showinfo("Enigma",
				"{0} Created".format(filename))
			return 1
		else:
			return 0
