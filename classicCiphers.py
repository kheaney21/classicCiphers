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
	'Encrypt or Decrypt via Caesar algorithm, spaces are kept for readability after decryption'
	uppercase = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
	lowercase = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
	
	shift = 3
	#encrypt if e
	if(x == "e"):
		pltext = str(file)
		ctext = []
		for i in pltext:
			if (i in uppercase):
				#check if out of bounds
				if(uppercase.index(i) + shift > 25):
					ctext[i] = uppercase[uppercase.index(i) + shift - 26]
				else:
					ctext[i] = uppercase[uppercase.index(i) + shift]
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
		ctext = str(file)
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
		pltext = text
		ctext = ""
		#for i in pltext:
	
	#decrypt if d
	else:
		ctext = text
		pltext = ""
		 
def polyalpha(x, text):
	'Encrypt or Decrypt via poly-alphabetic algorithm (vigenere), spaces kept for readability after decryption'
	uppercase = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
	lowercase = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
	
	key = cipher
	count = 0
	
	#encrypt if e
	if(x == "e"):
		pltext = str(file)
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
		ctext = str(file)
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
