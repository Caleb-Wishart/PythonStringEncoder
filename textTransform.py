#!/usr/bin/env python3

import string
from sys import argv
from string import digits
from string import ascii_uppercase as uppercase


### Functions ###
functions = []


def encode(func: function):
    functions.append(func)

    def wrapper(*args, **kwargs):
        print("Encoding")
        result = func(*args, **kwargs)
        print("Finished encoding")
        return result
    return wrapper


def usage():
    print(f"""Usage: python3 {__file__} [transformation] [input text]
For help call python3 {__file__} help"""
          )


def help():
    sep = "\n\t"
    print(f"""Help--
Available functions are:
	{sep.join([f.__name__ for f in functions])}
          """)


@encode
def ehex(plaintext):
    print('encoding')

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


@encode
def ebinary(plaintext):
    print('encoding')

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


@encode
def rot18(plaintext):
    print('encoding')

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


@encode
def caesar(plaintext: string, shift: int):
    print('encoding')

    # Uses translate to shift all possible characters to new alphabet
    shifted_alphabet = uppercase[shift % 26:] + uppercase[:shift % 26]
    return plaintext.maketrans(uppercase, shifted_alphabet)


@encode
def vigenere(plaintext, key):
    print('encoding')

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
            # print plaintext[char], alphabet[ ( alphabet.index(plaintext[char]) + alphabet.index( key[ ( (char - count) % len(key)) ])) % 26],key[ ( (char - count) % len(key))]
        else:
            resPart.append(plaintext[char])
            count += 1
            # print plaintext[char],' ',key[ ( (char - count) % len(key))]
    res = ''.join(resPart)

    return res

### MAIN ###


if __name__ == "__main__":
    # Ensure all arguments given
    if len(argv) != 3:
        if len(argv) == 2 and argv[1] == "help":
            help()
        else:
            usage()
        quit()
    # Get input & sanitise
    encode_type = argv[1]
    inp = argv[2]
    inp = inp.upper().replace(' ', '')

    if encode_type == 'hex':
        print(inp)
        print(ehex(inp))
    elif encode_type == 'binary':
        print(inp)
        print(ebinary(inp))
    elif encode_type == 'rot18':
        print(inp)
        print(rot18(inp))
    elif encode_type == 'reverse':
        print(inp)
        print(inp[::-1])
    elif encode_type[:6] == 'caesar':
        print(inp)
        print(caesar(inp, int(encode_type[6:])))
    elif encode_type[:8] == 'vigenere':
        print(inp)
        print(vigenere(inp, encode_type[8:]))
    else:
        print('Transformation not found\nFor options give \'help help\' as input')
