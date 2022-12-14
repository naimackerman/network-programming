import re
import math


def encrypt(*args, **kwargs):
    # Get plainText and keywors
    plainText = Element('plainText').element.value
    key = Element('keyword').element.value

    alphabets = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

    # Make plainText and keyword uppercase
    plainText = plainText.upper()
    key = key.upper()

    # Replace any character except alphabet
    plainText = re.sub(r'[^a-zA-Z]+', '', plainText)
    key = re.sub(r'[^a-zA-Z]+', '', key)

    # Replace J with I
    key = key.replace('J', 'I')

    # Check if both characters same, indent letter X to seperate them
    for i in range(0, len(plainText), 2):
        letter1 = plainText[i]
        letter2 = ''
        if i+1 < len(plainText):
            letter2 = plainText[i+1]

        if letter1 == letter2:
            plainText = plainText[0:i+1] + 'X' + plainText[i+1:len(plainText)]

    # Check length of plainText, append Z when odd
    if len(plainText) % 2 == 1:
        plainText += 'Z'

    # Handle letter J occurance in plainText
    plainText = plainText.replace('J', 'I')

    print('plaintext -> ', plainText)
    print('key -> ', key)

    # Concat and remove duplicate letter
    str = key + alphabets
    for i in range(len(alphabets)):
        letter = str[i]
        pos = str.find(letter, i + 1)

        # While duplicate letter found
        while pos > -1:
            # Delete duplicate letter which in the middle
            str = str[0:pos] + str[pos+1:len(str)]
            # Check if duplicate letter are still found
            pos = str.find(letter, i + 1)

    print('str -> ', str)

    # Create 5x5 key table
    row = [['' for x in range(5)] for y in range(5)]
    for i in range(5):
        row[i] = ''

    for i in range(5):
        for j in range(5):
            row[i] += str[5 * i + j]

    # Display 5x5 key table
    table = ""
    for i in range(5):
        table += '|' + row[i] + '|' + '\n'

    Element('keyTable').element.innerHTML = table
    
    print('array: ')
    for i in range(5):
        print('|' + row[i] + '|')

    # Substitution
    shift = 1
    result = ''
    for i in range(0,  len(plainText), 2):
        # Example:
        # keyword -> indonesia negara kaya dan jaya
        # plaintext -> GO OD BR OY OM SY SW EY EP CL EA NY
        # table, will be ->
        # I N D O E
        # S A G R K
        # Y B C F H
        # L M P Q T
        # U V W X Z

        pos1 = str.find(plainText[i])  # G -> 7
        pos2 = str.find(plainText[i + 1])  # O -> 3

        # Get X and Y coordinate
        x1 = pos1 % 5  # 7 % 5 = 2
        y1 = math.floor(pos1 / 5)  # 7 / 5 = 1
        x2 = pos2 % 5  # 3 % 5 = 3
        y2 = math.floor(pos2 / 5)  # 3 / 5 = 0

        # x1 = 2, y1 = 1
        # x2 = 3, y2 = 0
        # row[2][1] -> G
        # row[3][0] -> )

        # If y coordinate (y) are same, shift to right 1 point
        # else If x coordinate (x) are same, shift to bottom 1 point
        # else swap x1 and x2

        if y1 == y2:
            x1 = (x1 + shift) % 5
            x2 = (x2 + shift) % 5
        elif x1 == x2:
            y1 = (y1 + shift) % 5
            y2 = (y2 + shift) % 5
        else:
            temp = x1
            x1 = x2
            x2 = temp

        # x1 = 3, y1 = 1
        # x2 = 2, y2 = 0
        # row[3][1] -> R
        # row[2][0] -> D

        result += row[y1][x1] + row[y2][x2]

    # Display plain diagraph
    msg = ''
    for i in range(len(plainText)):
        msg += plainText[i]
        if (i + 1) % 2 == 0:
            msg += ' '

    Element('plainDigraph').element.innerHTML = msg

    # Display final result / ciphertext
    finalResult = ''
    for i in range(len(result)):
        finalResult += result[i]
        if (i + 1) % 2 == 0:
            finalResult += ' '

    Element('ciphertext').element.innerHTML = finalResult

    # return finalResult


# print('~ Playfair Cipher Encryption ~')
# print('Input Key: ', end='')
# key = input()
# print('Input Plaintext: ', end='')
# plainText = input()
# print()

# res = encrypt(plainText, key)
# print('\nCiphertext: ', res)
