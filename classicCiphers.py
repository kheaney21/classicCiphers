import sys
import os

def getInput():
	'Prompt user for input'
	choice = input("1 - encrypt, 2 - decrypt\n")
	alg = input("1 - Caesar, 2 - Substitution, 3 - Poly-Alphabetic, 4 - Transposition 5 - Other\n")
	filename = raw_input("Enter filename including extension\n")
	try:
		file = open(filename, "r+")
	except IOError:
		print("File not found")
	
	if(choice == 1):
		if(alg == 1):
			caesar("e", file)
		elif(alg == 2):
			sub("e", file)
		elif(alg == 3):
			polyalpha("e", file)
		elif(alg == 4):
			transposition("e", file)
		elif(alg == 5):
			other("e", file)
		else:
			print("Invalid Input")
		
	elif (choice == 2):
		if(alg == 1):
			caesar("d", file)
		elif(alg == 2):
			sub("d", file)
		elif(alg == 3):
			polyalpha("d", file)
		elif(alg == 4):
			transposition("d", file)
		elif(alg == 5):
			other("d", file)
		else:
			print("Invalid Input")	
	else:
		print("invalid Input")
		
		
def caesar(x, file):
	'Encrypt or Decrypt via Caesar algorithm'
	uppercase = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
	lowercase = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
	
	shift = 3
	#encrypt if e
	if(x == "e"):
		pltext = file.read()
		ctext = []
		for i in pltext:
			if (i in uppercase):
				#check if out of bounds
				if(uppercase.index(i) + shift > 25):
					ctext.append(uppercase[uppercase.index(i) + shift - 26])
				else:
					ctext.append(uppercase[uppercase.index(i) + shift])
			elif (i in lowercase):
				#check if out of bounds 
				if(lowercase.index(i) + shift > 25):
					ctext.append(lowercase[lowercase.index(i) + shift - 26])
				else:
					ctext.append(lowercase[lowercase.index(i) + shift])
			else:
				continue
		#print ctext
		print(''.join(ctext))		
		#overwrite file***
		filename = os.path.basename(file.name)
		newFile = open(filename, 'w')
		newFile.write(''.join(ctext))
		
	#decrypt if d
	else:
		ctext = file.read()
		pltext = []
		for i in ctext:
			if (i in uppercase):
				#check if out of bounds
				if(uppercase.index(i) - shift < 0):
					pltext.append(uppercase[uppercase.index(i) - shift + 26])
				else:
					pltext.append(uppercase[uppercase.index(i) - shift])
			elif (i in lowercase):
				#check if out of bounds
				if(lowercase.index(i) - shift < 0):
					pltext.append(lowercase[lowercase.index(i) - shift + 26])
				else:
					pltext.append(lowercase[lowercase.index(i) - shift])
			else:
				continue
				
		#print pltext
		print(''.join(pltext))		
		#overwrite file***
		filename = os.path.basename(file.name)
		newFile = open(filename, 'w')
		newFile.write(''.join(pltext))
		
def sub(x, file):
	'Encrypt or Decrypt via substitution algorithm'
	#encrypt if e
	if(x == "e"):
		pltext = file.read()
		ctext = []
		
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
		
		for i in pltext:
			if(i in sub):
				ctext.append(sub[i])
			else:
				continue
		#print ctext
		print(''.join(ctext))		
		#overwrite file***
		filename = os.path.basename(file.name)
		newFile = open(filename, 'w')
		newFile.write(''.join(ctext))
			
	
	#decrypt if d
	else:
		ctext = file.read()
		pltext = []
		
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
		
		for i in ctext:
			if(i in sub):
				pltext.append(sub[i])
			else:
				continue
		#print ctext
		print(''.join(pltext))		
		#overwrite file***
		filename = os.path.basename(file.name)
		newFile = open(filename, 'w')
		newFile.write(''.join(pltext))
		 
def polyalpha(x, file):
	'Encrypt or Decrypt via poly-alphabetic algorithm (vigenere), spaces kept for readability after decryption'
	uppercase = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
	lowercase = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
	
	key = cipher
	count = 0
	
	#encrypt if e
	if(x == "e"):
		pltext = file.read()
		ctext = []
		for i in pltext:
			#count to iterate through key, reset when count is greater than length of key
			if (count > len(key)):
				count = 0
			shift = lowercase.index(key[count])
			#increment count
			count = count + 1
			if (pltext[i] in uppercase):
				#check if out of bounds
				if(uppercase.index(i) + shift > 25):
					ctext.append(uppercase[uppercase.index(i) + shift - 26])
				else:
					ctext.append(uppercase[uppercase.index(i) + shift])
			elif (i in lowercase):
				#check if out of bounds
				if(lowercase.index(i) + shift > 25):
					ctext.append(lowercase[lowercase.index(i) + shift - 26])
				else:
					ctext.append(lowercase[lowercase.index(i) + shift])
			#if punctuation/space
			else:
				count = count - 1
				continue
				
		#print ctext
		print(''.join(ctext))		
		#overwrite file***
		filename = os.path.basename(file.name)
		newFile = open(filename, 'w')
		newFile.write(''.join(ctext))
			
	#decrypt if d
	else:
		ctext = file.read()
		pltext = []
		for i in ctext:
			#count to iterate through key, reset when count is greater than length of key
			if (count > len(key)):
				count = 0
			shift = lowercase.index(key[count])
			if (ctext[i] in uppercase):
				#check if out of bounds
				if(uppercase.index(i) - shift < 0):
					pltext.append(uppercase[uppercase.index(i) - shift + 26])
				else:
					pltext.append(uppercase[uppercase.index(i) - shift])
			elif (ctext[i] in lowercase):
				#check if out of bounds
				if(lowercase.index(i) - shift < 0):
					pltext.append(lowercase[lowercase.index(i) - shift + 26])
				else:
					pltext.append(lowercase[lowercase.index(i) - shift])
			else:
				continue
				
		#print pltext
		print(''.join(pltext))		
		#overwrite file***
		filename = os.path.basename(file.name)
		newFile = open(filename, 'w')
		pltext = newFile.write(''.join(pltext))

def transposition(x, text):
	'Encrypt or Decrypt via transposition algorithm'
	#encrypt if e
	if(x == "e"):
		pltext = text
		ctext = ""
		#for i in pltext:
	
	#decrypt if d
	else:
		ctext = text
		pltext = ""

def other(x, text):
	'Encrypt or Decrypt via other algorithm'
	
		
getInput()
