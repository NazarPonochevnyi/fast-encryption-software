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

Author: Ponochevnyi Nazar.
'''


#Alphabet (You can change)
A = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']


#Input
your_text = input('\nInput text: ')
key = int(input('\nInput key: '))
your_text = your_text.upper()


#Basic proccess
result = ''
for t in your_text:
    if A.count(t) != 0:
        pos = A.index(t)
        pos += key     #!!! Toggle (+/-) !!!
        if pos >= len(A):
            pos -= len(A)
        result += A[pos]
    else:
        result += t


#Output
print('\nEncrypted text:', result)
