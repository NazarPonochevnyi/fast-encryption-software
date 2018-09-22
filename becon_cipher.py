import sys

# Example
# Text: "ponochevnyi"
# Chipher: sHOuLd wE StArt CLasS Now, or sHOULd We WAIT FOr evEryONe tO gET HeRE?

# Input values
n = 5
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'acbdefghijklmnopqrstuvwxyz'
Alphabet = alphabet.upper()
string = 'sHOuLd wE StArt CLasS Now, or sHOULd We WAIT FOr evEryONe tO gET HeRE?' # sys.argv[1]

# Algorithm
crypt = {letter: key[i: i + n] for i, letter in enumerate(alphabet)}
decrypt = {key[i: i + n]: letter for i, letter in enumerate(alphabet)}

code = ''
for s in string:
    if s in alphabet:
        code += 'a'
    if s in Alphabet:
        code += 'b'

text = [decrypt[code[i: i + n]] for i in range(0, 54, n)]

# Output values
print('Cipher: {}\nText: {}'.format(string, ''.join(text)))
