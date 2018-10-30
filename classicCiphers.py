import sys
#file input/output

def caesarEn(filename):
	'Encrypt with caesar cipher with offset 1'
	
	offset = {
		"a" : "b", "b" : "c", "c" : "d",
		"d" : "e", "e" : "f", "f" : "g",
		"g" : "h", "h" : "i", "i" : "j",
		"j" : "k", "k" : "l", "l" : "m",
		"m" : "n", "n" : "o", "o" : "p",
		"p" : "q", "q" : "r", "r" : "s",
		"s" : "t", "t" : "u", "u" : "v",
		"v" : "w", "w" : "x", "x" : "y", "y" : "z", "z" : "a",
		"A" : "B", "B" : "C", "C" : "D",
		"D" : "E", "E" : "F", "F" : "G",
		"G" : "H", "H" : "I", "I" : "J",
		"J" : "K", "K" : "L", "L" : "M",
		"M" : "N", "N" : "O", "O" : "P",
		"P" : "Q", "Q" : "R", "R" : "S",
		"S" : "T", "T" : "U", "U" : "V",
		"V" : "W", "W" : "X", "X" : "Y", "Y" : "Z","Z" : "A",
	}
	
	#read file as string
	plainText = open(filename, "r+")
	
	#replace characters
	cipher = ""
	for i in plainText:
		if i in offset:
			cipher += offset[i]
		else:
			cipher += i
	#overwrite original file
	print(cipher)
	plainText.write(cipher)
	
def caesarDec(filename):
	'Decrypt caesar cipher with offset 1'
	
	offset = {
		"a" : "z", "b" : "a", "c" : "b",
		"d" : "c", "e" : "d", "f" : "e",
		"g" : "f", "h" : "g", "i" : "h",
		"j" : "i", "k" : "j", "l" : "k",
		"m" : "l", "n" : "m", "o" : "n",
		"p" : "o", "q" : "p", "r" : "q",
		"s" : "r", "t" : "s", "u" : "t",
		"v" : "u", "w" : "v", "x" : "w", "y" : "x", "z" : "y",
		"A" : "Z", "B" : "A", "C" : "B",
		"D" : "C", "E" : "D", "F" : "E",
		"G" : "F", "H" : "G", "I" : "H",
		"J" : "I", "K" : "J", "L" : "K",
		"M" : "L", "N" : "M", "O" : "N",
		"P" : "O", "Q" : "P", "R" : "Q",
		"S" : "R", "T" : "S", "U" : "T",
		"V" : "U", "W" : "V", "X" : "W", "Y" : "X","Z" : "Y",
	}
	
	#read file as string
	cipher = open(filename, "w+")
	
	#replace characters
	plainText = ""
	for i in cipher:
		if i in offset:
			plainText += offset[i]
		else:
			plainText += i
	#overwrite original file
	cipher.write(plainText)

def subEn(filename):
	'Encrypt with substitution cipher'
	
	sub = {
		"a" : "q", "b" : "w", "c" : "e",
		"d" : "r", "e" : "t", "f" : "y",
		"g" : "u", "h" : "i", "i" : "o",
		"j" : "p", "k" : "a", "l" : "s",
		"m" : "d", "n" : "f", "o" : "g",
		"p" : "h", "q" : "j", "r" : "k",
		"s" : "l", "t" : "z", "u" : "x",
		"v" : "c", "w" : "v", "x" : "b", "y" : "n", "z" : "m",
		"A" : "Q", "B" : "W", "C" : "E",
		"D" : "R", "E" : "T", "F" : "Y",
		"G" : "U", "H" : "I", "I" : "O",
		"J" : "P", "K" : "A", "L" : "S",
		"M" : "D", "N" : "F", "O" : "G",
		"P" : "H", "Q" : "J", "R" : "K",
		"S" : "L", "T" : "Z", "U" : "X",
		"V" : "C", "W" : "V", "X" : "B", "Y" : "N","Z" : "M",
		}
		
	#read file as string
	plainText = open(filename, "w+")
	
	#create new file (read character by character)
	cipher = ""
	for i in plainText:
		if i in sub:
			cipher += sub[i]
		else:
			cipher += i
	#overwrite original file
	plainText.write(cipher)
		
def subDec(filename):
	'Decrypt substitution cipher'
	
	sub = {
		"q" : "a", "w" : "b", "e" : "c",
		"r" : "d", "t" : "e", "y" : "f",
		"u" : "g", "i" : "h", "o" : "i",
		"p" : "j", "a" : "k", "s" : "l",
		"d" : "m", "f" : "n", "g" : "o",
		"h" : "p", "j" : "q", "k" : "r",
		"l" : "s", "z" : "t", "x" : "u",
		"c" : "v", "v" : "w", "b" : "x", "n" : "y", "m" : "z",
		"Q" : "A", "W" : "B", "E" : "C",
		"R" : "D", "T" : "W", "Y" : "F",
		"U" : "G", "I" : "H", "O" : "I",
		"P" : "J", "A" : "K", "S" : "L",
		"D" : "M", "F" : "N", "G" : "O",
		"H" : "P", "J" : "Q", "K" : "R",
		"L" : "S", "Z" : "T", "X" : "U",
		"C" : "V", "V" : "W", "B" : "X", "N" : "Y","M" : "Z",
	}
	
	#read file as string
	cipher = open(filename, "w")
	
	#create new file (read character by character)
	plainText = ""
	for i in cipher:
		if i in sub:
			plainText += sub[i]
		else:
			plainText += i
	#overwrite original file
	cipher.write(plainText)

def polyAlphaEn(filename):
	'Encrypt with poly-alphabetic cipher'

def polyAlphaDec(filename):
	'Decrypt poly-alphabetic cipher'
	
def transEn(filename):
	'Encrypt with transposition cipher'

def transDec(filename):
	'Decrypt transposition cipher'
	
def getInput():
	'Get user input'

	filename = raw_input("Enter file name with extension \n")

	choice = input("1 - Encrypt, 2 - Decrypt \n")
	
	method = input("1 - Caesar, 2 - Substitution, 3 - Poly-alphabetic, 4 - Transposition, 5 - \n")
	
	#encrypt
	if choice == 1:
		if method == 1:
			caesarEn(filename)
		elif method == 2:
			subEn(filename)
		elif method == 3:
			polyAlphaEn(filename)
		elif method == 4:
			transEn(filename)
		elif method == 5:
			print("error")
		else:
			print("Invalid Input")
		
	#decrypt
	elif choice == 2:
		if method == 1:
			caesarDec(filename)
		elif method == 2:
			subDec(filename)
		elif method == 3:
			polyAlphaDec(filename)
		elif method == 4:
			transDec(filename)
		elif method == 5:
			print("error")
		else:
			print("Invalid Input")
	else:
		print("Invalid Input")
		
getInput()

	
	


