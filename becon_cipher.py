import sys

# Text: "ponochevnyi"
# Chipher: sHOuLd wE StArt CLasS Now, or sHOULd We WAIT FOr evEryONe tO gET HeRE?

# Input values
n = 5
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'acbdefghijklmnopqrstuvwxyz'
string = 'sHOuLd wE StArt CLasS Now, or sHOULd We WAIT FOr evEryONe tO gET HeRE?' #sys.argv[1]

# Algorithm
crypt = {letter : key[i : i + n] for i, letter in enumerate(alphabet)}
decrypt = {key[i : i + n] : letter for i, letter in enumerate(alphabet)}

string = ''.join([s for s in string if s in alphabet + alphabet.upper()])
print(string)