#-*-coding:utf8;-*-
#qpy:3
#qpy:console

'''
@Key Generator@

Comments:
Coming soon you can generating keys for you message!

Author: Ponochevnyi Nazar
'''

import random

output_file = 'key.txt' # name of the file in which the key is saved
length_key = 1000000 # required key length

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "G", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] # you can change

result = ''.join([random.choice(alphabet) for _ in range(length_key)])

file = open(output_file, 'w')
file.write(result)
file.close()
