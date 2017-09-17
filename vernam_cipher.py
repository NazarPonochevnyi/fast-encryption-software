#-*-coding:utf8;-*-
#qpy:3
#qpy:console

'''
@Vernam's Cipher@
Comments:

To start the program, you must install the numpy module.
To do this, run the command line and type: pip install numpy.

For now, the program supports only English and ASCII encoding,
but in the near future, we will add support for the Russian
language and UTF-8 encoding.

If you need to encrypt a message, in the 'Input action:' field,
type 'en', and if you need to decrypt the message, enter 'de'
in the 'Input action:' field.

Author: Nazar Ponochevnyi
'''

# Import some module
import ast
import numpy as np # pip install numpy


# Functions
def xor(aa, bb):
    a = np.frombuffer(aa, dtype=np.byte)
    b = np.frombuffer(bb, dtype=np.byte)
    return str(np.bitwise_xor(a, b).tostring())

def btrip(string):
    return string.replace('b\'', '').replace(string[-2] + '\'', string[-2])


# Input values
while True:
    action = input('\nInput action: ').strip()
    if action in ['en', 'de']: break
    print('\nIncorrect action!')
while True:
    try:
        text = ast.literal_eval("b'{}'".format(input('\nInput text: ').strip().replace('\'', '`')))
        key = ast.literal_eval("b'{}'".format(input('\nInput key: ').strip().replace('\'', '`')))
        if len(key) >= len(text):
            key = key[:len(text)]
            break
        print('\nInput text and a key of equal length!\n')
    except SyntaxError:
        print('\nInput only ASCII literal characters!\n')


# Basic processes
result = xor(text, key)


# Output values
if action == 'en': print('\nEncrypted text:\n' + btrip(result))
else: print('\nDecrypted text:\n' + btrip(result.encode().decode()).replace('`', '\''))
