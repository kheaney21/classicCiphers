import sys

def getInput():
	'Prompt user for input'
	choice = input("1 - encrypt, 2 - decrypt")
	alg = ("1 - Caesar, 2 - Substitution, 3 - Poly-Alphabetic, 4 - Transposition 5 - Other")
	filename = raw_input("Enter filename including extension")
	pltext = 
	
	if(choice == 1):
			if(alg == 1):
				caesar(e, pltext)
			elif(alg == 2):
				sub(e, pltext)
			elif(alg == 3):
				polyalpha(e, pltext)
			elif(alg == 4):
				transposition(e, pltext)
			elif(alg == 5):
				other(e, pltext)
			else:
				print("Invalid Input")
		
	elif (choice == 2):
			if(alg == 1):
				caesar(d, pltext)
			elif(alg == 2):
				sub(d, pltext)
			elif(alg == 3):
				polyalpha(d, pltext)
			elif(alg == 4):
				transposition(d, pltext)
			elif(alg == 5):
				other(d, pltext)
			else:
				print("Invalid Input")	
	else:
		print("invalid input)
		
		
def caesar(x, text):
	'Encrypt or Decrypt via Caesar algorithm'
	#padded by 3 for adding/subtracting index
	uppercase = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
	lowercase = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
	
	#encrypt if e
	if(x == "e"):
		pltext = text
		ctext = ""
		for i in pltext:
			if (i in uppercase):
				#check if out of bounds
				if(uppercase(index(pltext[i]) + 3 > 25):
					ctext[i] = uppercase(index(pltext[i]) + 3 + 26
				else:
					ctext[i] = uppercase(index(pltext[i]) + 3)
			else:
				if(lowercase(index(pltext[i]) + 3 > 25):
					ctext[i] = lowercase(index(pltext[i]) + 3 + 26
				else:
					ctext[i] = lowercase(index(pltext[i]) + 3)
	
	#decrypt if d
	else(x == "d"):
		ctext = text
		pltext = ""
		for i in ctext:
			if (i in uppercase):
				#check if out of bounds
				if(uppercase(index(ctext[i]) - 3) < 0):
					pltext[i] = lowercase(index(ctext[i]) - 3 + 26)
				else:
					pltext[i] = uppercase(index(ctext[i]) - 3)
			else:
				#check if out of bounds
				if(lowercase(index(ctext[i]) - 3) < 0):
					pltext[i] = lowercase(index(ctext[i]) - 3 + 26)
				else:
					pltext[i] = lowercase(index(ctext[i]) - 3)
		
def sub(x, text):
	'Encrypt or Decrypt via substitution algorithm'
	#encrypt if e
	if(x == "e"):
	
	#decrypt if d
	else(x == "d"):
	
def polyalpha(x, text):
	'Encrypt or Decrypt via poly-alphabetic algorithm'
	#encrypt if e
	if(x == "e"):
	
	#decrypt if d
	else(x == "d"):

def transposition(x, text):
	'Encrypt or Decrypt via transposition algorithm'
	#encrypt if e
	if(x == "e"):
	
	#decrypt if d
	else(x == "d"):

def other(x, text):
	'Encrypt or Decrypt via other algorithm'
	
		
getInput()
	
	
