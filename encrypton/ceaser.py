# ceaser.py

import sys

"""
@TODO: Maybe add a salt of sorts to encode? How can we make a simple cypher a little better?
@TODO: Encoded input break by bruteforce?
"""
def encode(text, shift):
    resultBuff = []
    encodedText = str()

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            resultBuff.append(chr(shifted))
        else:
            resultBuff.append(char)

    encodedText = ''.join(resultBuff)

    return encodedText

def decode(text, shift):
    resultBuff = []
    decodedText = str()

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base - shift) % 26 + base
            resultBuff.append(chr(shifted))
        else:
            resultBuff.append(char)

    decodedText = ''.join(resultBuff)

    return decodedText
