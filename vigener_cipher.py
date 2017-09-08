#-*-coding:utf8;-*-
#qpy:3
#qpy:console

'''
@Vigener's Cipher@

Comments:
You can change the array with the alphabet to your language,
and the program will work with your language.

Also, pay attention to the line with the switch, changing +/-,
you can change the program for encryption / decryption.

Author: Ponochevnyi Nazar
'''


# Alphabet (You can change)
A = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']


# Input
text = input('\nInput your text: ').upper()
key = input('\nInput your key: ').upper()


# Basic Processes
i = 0
result = ''
for t in text:
    if A.count(t) != 0:
        if i == len(key):
            i = 0
        sm = A.index(key[i]) + 1
        pos = A.index(t) + sm    #!!! Toggle (+/-) !!! 
        if pos >= len(A):
            pos -= len(A)
        result += A[pos]
        i += 1
    else:
        result += t

    
# Output
print('\nYour encrypted/decrypted text:', result)
