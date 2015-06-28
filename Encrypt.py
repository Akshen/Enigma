import tkMessageBox
from string import maketrans
class E:
	
	def Encrypt(self,path):
		Og_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789."
		semiog_string = "!)@(#*$&%^<:{}?0192837465/qazmlp>;[t]\|=-`~JKLWERxcvnVAsbrgeZO."

		try:

			plain_file = open(path,'r')
			file = open("Encrypted.txt",'w')
			listline = plain_file.readlines()
		
			for i in xrange(len(listline)):
				for x in listline[i]:
					table = maketrans(Og_string,semiog_string)
					file.write(x.translate(table))


			file.close()
			plain_file.close()
			tkMessageBox.showinfo("Enigma",
				"Encrypted.txt Created" )

			
		except:

			tkMessageBox.showwarning(
			"Enigma","Empty"
			)


