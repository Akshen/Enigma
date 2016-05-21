import tkMessageBox

class KV():
	def keyvalidator(self,key_one,key_two,key_three):
		
		if(key_one >=63 or key_one <=0):
			print key_one
			tkMessageBox.showwarning("Enigma",
				"Key should be between 1-62")
			return 0

		if(key_two >=63 or key_two <=0):
			print key_two
			tkMessageBox.showwarning("Enigma",
				"Key should be between 1-62")
			return 0

		if(key_three>=63 or key_three <=0):
			print key_three
			tkMessageBox.showwarning("Enigma",
				"Key should be between 1-62")
			return 0


		return 1


	