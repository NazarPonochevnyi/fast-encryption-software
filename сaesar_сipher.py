#-*-coding:utf8;-*-
#qpy:3
#qpy:console

'''
@Caesar's Cipher@

Comments:
You can change the array with the alphabet to your language,
and the program will work with your language.

Also, pay attention to the line with the switch, changing +/-,
you can change the program for encryption / decryption.

Author: Nazar Ponochevnyi
'''


# Alphabet (you can change)
A = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']


# Input values
text = input('\nInput text: ').upper()
key = int(input('\nInput key: '))


# Basic proccess
result = ''
for t in text:
    if A.count(t) != 0:
        pos = A.index(t)
        pos = pos + key     #!!! Toggle (+/-) !!!
        if pos >= len(A):
            pos -= len(A)
        result += A[pos]
    else:
        result += t


# Output values
print('\nEncrypted\Decrypted text:', result)
