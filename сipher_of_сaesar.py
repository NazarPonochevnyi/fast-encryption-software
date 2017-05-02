import random


#

A = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']


your_text = input('Input text: ')
your_text = your_text.upper()
key = random.randint(1,25)


result = ''
for t in your_text:
    if t != ' ':
        pos = A.index(t)
        pos += key
        if pos > len(A) - 1:
            pos -= len(A)
        result += A[pos]
    else:
        result += ' '

print(result)
