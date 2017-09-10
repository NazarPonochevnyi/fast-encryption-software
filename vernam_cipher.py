#-*-coding:utf8;-*-
#qpy:3
#qpy:console

'''
@Vernam's Cipher@
Comments:

Soon the code will appear :)

Author: Nazar Ponochevnyi
'''

# Import some module
import ast
import numpy as np # pip install numpy


# XOR function
def xor(aa, bb):
    a = np.frombuffer(aa, dtype=np.byte)
    b = np.frombuffer(bb, dtype=np.byte)
    return np.bitwise_xor(a, b).tostring()


# Input values
while True:
    action = input('\nInput action: ').strip()
    if action in ['en', 'de']: break
    else: print('\nIncorrect action!')
while True:
    text = ast.literal_eval("b'{}'".format(input('\nInput text: ').strip().replace('\'', '`')))
    key = ast.literal_eval("b'{}'".format(input('\nInput key: ').strip().replace('\'', '`')))
    if len(key) >= len(text):
        key = key[:len(text)]
        break
    print('\nInput text and a key of equal length!\n')


# Basic processes
result = xor(text, key)


# Output values
if action == 'en':
    result = str(result)
    print('\nEncrypted text:')
    print(result.replace('b\'', '').replace(result[-2] + '\'', result[-2]))
else:
    print('\nDecrypted text:')
    print(result.decode().replace('`', '\''))
