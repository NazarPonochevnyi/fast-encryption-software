#-*-coding:utf8;-*-
#qpy:3
#qpy:console

'''
@Vernam's Cipher@
Comments:

Soon the code will appear :)

Author: Ponochevnyi Nazar
'''

# Import some module
import numpy as np # pip install numpy


# XOR function
def slow_xor(aa, bb):
    a = np.frombuffer(aa, dtype=np.byte)
    b = np.frombuffer(bb, dtype=np.byte)
    return np.bitwise_xor(a, b).tostring()


# Input values
while True:
    text = input('Input your text: ').encode()
    key = input('Input your key: ').encode()
    if len(text) == len(key): break
    print('\nInput text and a key of equal length!\n')


# Basic processes
result = slow_xor(text, key)


# Output values
print('Your encrypted/decrypted text:', result)
