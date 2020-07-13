#!/usr/bin/env python

import argparse

def encrypt(string, shift):
    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return cipher

def decrypt(string, shift):
    text = ''
    for char in string:
        if char == ' ':
            text = text + char
        elif  char.isupper():
            text = text + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            text = text + chr((ord(char) - shift - 97) % 26 + 97)
    return text



def loadmsg(filename):
    if not args.file:
        print("Please specify a message file")
    else:
        with open(filename, 'r') as file:
            msg = file.read().replace('\n', '')
    return msg

FUNCTION_MAP = {'enc' : encrypt,
                'dec' : decrypt}

parser = argparse.ArgumentParser(description='enc/decrypt messages with Caesar Cipher')
parser.add_argument('operator', choices=FUNCTION_MAP.keys())
parser.add_argument('file',
                    help='File message')
parser.add_argument('-s', type=int, metavar='s', default=3,
                    help='Shift number (integer)')
args = parser.parse_args()




func = FUNCTION_MAP[args.operator]
print(func(loadmsg(args.file), args.s))


