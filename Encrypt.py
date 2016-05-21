# import tkMessageBox
# from string import maketrans
# class E:
	
# 	def Encrypt(self,path):
# 		Og_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789."
# 		semiog_string = "!)@(#*$&%^<:{}?0192837465/qazmlp>;[t]\|=-`~JKLWERxcvnVAsbrgeZO."

# 		try:

# 			plain_file = open(path,'r')
# 			file = open("Encrypted.txt",'w')
# 			listline = plain_file.readlines()
		
# 			for i in xrange(len(listline)):
# 				for x in listline[i]:
# 					table = maketrans(Og_string,semiog_string)
# 					file.write(x.translate(table))


# 			file.close()
# 			plain_file.close()
# 			tkMessageBox.showinfo("Enigma",
# 				"Encrypted.txt Created" )

			
# 		except:

# 			tkMessageBox.showerror(
# 			"Enigma","Empty"
# 			)



import tkMessageBox
import os
from string import maketrans
class E:
	
	def Encrypt(self,path,key_one,key_two,key_three):

		numalpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

		combo_one = "ad456bc78gqrstMNGHIJpOPhmnoDEFQRuvwxyzijklABef23CKLSTU1VWXYZ09"
		combo_two = "ad456bc78gqrstMNGHIJpOPhmnoDEFQRuvwxyzijklABef23CKLSTU1VWXYZ09"
		combo_three = "ad456bc78gqrstMNGHIJpOPhmnoDEFQRuvwxyzijklABef23CKLSTU1VWXYZ09"
		x, y, z = key_one, key_two, key_three

		if os.path.exists(path):
			plain_file = open(path,'r')
			file = open("combo_one.txt",'w')
			listline = plain_file.readlines()
		
			#FIRST STEP 
			
			temp = combo_one[0:x]
			combo_one = combo_one[x:63]
			combo_one +=temp

			for i in xrange(len(listline)):
				for j in listline[i]:
					table = maketrans(numalpha,combo_one)
					file.write(j.translate(table))

			file.close()
			plain_file.close()

			#SECOND STEP
			file_temp = open("combo_one.txt",'r')
			listline = file_temp.readlines()
			file = open("combo_two.txt",'w')


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
					table = maketrans(numalpha,combo_two)
					file.write(j.translate(table))

			file_temp.close()
			file.close()
			os.remove("combo_one.txt")

			#Third Step
			file_temp = open("combo_two.txt",'r')
			listline = file_temp.readlines()
			file = open("Encrypted.txt",'w')

			z = 62-z
			temp = combo_three[z:63]
			combo_three = combo_three[0:z]
			temp+=combo_three
			combo_three = temp

			for i in xrange(len(listline)):
				for j in listline[i]:
					table = maketrans(numalpha,combo_three)
					file.write(j.translate(table))

			file_temp.close()
			os.remove("combo_two.txt")
			file.close()



			tkMessageBox.showinfo("Enigma",
				"Encrypted.txt Created" )

			
		else:

			tkMessageBox.showerror(
			"Enigma","Empty"
			)



