'''
@Caesar's Cipher@

Comments:
--------
'''


#Alphabet
A = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']


#Input
your_text = input('Input text: ')
key = int(input('Input key: '))
your_text = your_text.upper()


#Basic proccess
result = ''
for t in your_text:
    if t != ' ':
        pos = A.index(t)
        pos += key #    !!! Toggle (+/-) !!!
        if pos > len(A) - 1:
            pos -= len(A)
        result += A[pos]
    else:
        result += ' '


#Output
print('Enctypted text:', result)
