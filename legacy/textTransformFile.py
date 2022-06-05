#!/usr/bin/env python
# DEPRECIATED

from sys import argv as argv
from string import digits as digits
from string import uppercase as uppercase
from string import maketrans as maketrans
from string import punctuation as punctuation
from pyperclip import copy as copy

### Var ###

# Ensure all arguments given
try:
    x = argv[2]
except:
    print 'Usage: [call script] [transformation] [input text] \nFor options give \'help help\' as input'
    quit()

# Get input & sanitise
encode_type = argv[1]
file = argv[2]
if encode_type == 'help' and file == 'help':
    print 'Options: hex, binary, rot18, reverse, caesar[numb], vigenere[key]\n ONLY ACCEPTS ".txt" documents'
    quit()
f = open(file, "r+")
inp = f.read().split('\n')
f.close()
for i in range(len(inp)):
    if inp[i] == '':
        del inp[i]
    else:
        inp[i] = inp[i].upper()

### Functions ###


def encode_hex(plaintext):

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

    ss = []
    for char in plaintext:
        if char in list(uppercase):
            ss.append(char.encode('rot13'))
        elif char in digits:
            a = (int(char) + 5) % 10
            ss.append(str(a))
        else:
            ss.append(char)
        res = ''.join(ss)

    return res


def caesar(plaintext, shift):

    # Uses translate to shift all possible characters to new alphabet
    shifted_alphabet = uppercase[shift % 26:] + uppercase[:shift % 26]
    table = maketrans(uppercase, shifted_alphabet)
    return plaintext.translate(table)


def vigenere(plaintext, key):

    count = 0
    key = key.upper().replace(' ', '')
    alphabet = list(uppercase)
    resPart = []

    for char in range(len(plaintext)):
        if plaintext[char] in alphabet:
            resPart.append(alphabet[(alphabet.index(
                plaintext[char]) + alphabet.index(key[((char - count) % len(key))])) % 26])
            # append the corresponding alphabet character after being shifted the by the amount of the current key letter
            # var count allows for non A-Z characters to pass through without causing disruption to the current key letter

        else:
            resPart.append(plaintext[char])
            count += 1
    res = ''.join(resPart)

    return res


### MAIN ###
if encode_type == 'hex':
    r = open(file[:-4] + '_' + encode_type + '.txt', 'w+')
    for x in range(len(inp)):
        r.write(encode_hex(inp[x]) + '\n')
    r.close()
    print 'encoded'
elif encode_type == 'binary':
    r = open(file[:-4] + '_' + encode_type + '.txt', 'w+')
    for x in range(len(inp)):
        r.write(encode_binary(inp[x]) + '\n')
    r.close()
    print 'encoded'
elif encode_type == 'rot18':
    r = open(file[:-4] + '_' + encode_type + '.txt', 'w+')
    for x in range(len(inp)):
        r.write(rot18(inp[x]) + '\n')
    r.close()
    print 'encoded'
elif encode_type == 'reverse':
    r = open(file[:-4] + '_' + encode_type + '.txt', 'w+')
    for x in range(len(inp)):
        r.write(inp[x][::-1] + '\n')
    r.close()
    print 'encoded'
elif encode_type[:6] == 'caesar':
    r = open(file[:-4] + '_' + encode_type + '.txt', 'w+')
    for x in range(len(inp)):
        r.write(caesar(inp[x] + '\n', int(encode_type[6:])))
    r.close()
    print 'encoded'
elif encode_type[:8] == 'vigenere':
    r = open(file[:-4] + '_' + encode_type + '.txt', 'w+')
    for x in range(len(inp)):
        r.write(vigenere(inp[x] + '\n', encode_type[8:]))
    r.close()
    print 'encoded'
elif encode_type == 'help':
    print 'Options: hex, binary, rot18, reverse, caesar[numb], vigenere[key]\n ONLY ACCEPTS ".txt" documents'
else:
    print 'Transformation not found\nFor options give \'help help\' as input'
