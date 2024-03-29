#!/usr/bin/env python
# DEPRECIATED

from sys 		import argv 	 	as argv
from string 	import digits	 	as digits
from string 	import uppercase 	as uppercase
from string 	import maketrans 	as maketrans
from string 	import punctuation 	as punctuation
from pyperclip  import copy 	 	as copy

### Var ###

# Ensure all arguments given
try:
	x = argv[2]
except:
	print 'Usage: [call script] [transformation] [input text] \nFor options give \'help help\' as input'
	quit()

# Get input & sanitise
encode_type = argv[1]
inp = argv[2]
inp = inp.upper().replace(' ','')

### Functions ###
def encode_hex(plaintext):
	print 'encoding'

	ss = []
	for char in plaintext:
		if char in uppercase:
			ss.append(char.encode('hex'))
		elif char in digits:
			ss.append(char.encode('hex'))
		else:
			ss.append(char)
		res = ' '.join(ss)

	return res

def encode_binary(plaintext):
	print 'encoding'

	ss = []
	for char in plaintext:
		if char in uppercase:
			ss.append(format(ord(char), 'b'))
		elif char in digits:
			ss.append(format(ord(char), 'b'))
		else:
			ss.append(char)
		res = ' '.join(ss)

	return res

def rot18(plaintext):
	print 'encoding'

	ss = []
	for char in plaintext:
		if char in list(uppercase):
			ss.append(char.encode('rot13'))
		elif char in digits:
			a = (int(char) + 5) % 10
			ss.append(str(a))
		else:
			ss.append(char)
		res = ' '.join(ss)

	return res

def caesar(plaintext, shift):
	print 'encoding'

	# Uses translate to shift all possible characters to new alphabet
	shifted_alphabet = uppercase[shift % 26 :] + uppercase[:shift % 26]
	table = maketrans(uppercase, shifted_alphabet)
	return ' '.join(plaintext.translate(table))

def vigenere(plaintext, key):
	print 'encoding'

	count = 0
	key = key.upper().replace(' ','')
	alphabet = list(uppercase)
	resPart = []

	for char in range(len(plaintext)):
		if plaintext[char] in alphabet:
			resPart.append(alphabet[ ( alphabet.index(plaintext[char]) + alphabet.index( key[ ( (char - count) % len(key)) ])) % 26])
			# append the corresponding alphabet character after being shifted the by the amount of the current key letter
			# var count allows for non A-Z characters to pass through without causing disruption to the current key letter

		else:
			resPart.append(plaintext[char])
			count += 1
	res = ' '.join(resPart)

	return res

def reverse(plaintext):
	print 'encoding'

	ss = []
	for char in plaintext:
		ss.append(char)

		res = ' '.join(ss)

	return res[::-1]

### MAIN ###

# Put output into clipboard

if   encode_type 	 == 'hex': 		copy(encode_hex(inp))
elif encode_type 	 == 'binary': 	copy(encode_binary(inp))
elif encode_type	 == 'rot18': 	copy(rot18(inp))
elif encode_type	 == 'reverse': 	copy(reverse(inp))
elif encode_type[:6] =='caesar': 	copy(caesar(inp,int(encode_type[6:])))
elif encode_type[:8] =='vigenere':	copy(vigenere(inp,encode_type[8:]))
elif encode_type	 == 'help':  	print 'Options: hex, binary, rot18, reverse, caesar[numb], vigenere[key]'
else: print 'Transformation not found\nFor options give \'help help\' as input'