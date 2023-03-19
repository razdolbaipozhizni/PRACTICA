import transliteration

def block2(arr_lex):
    global znak         #заполняем список знаков (из 1 блока, но без пробела)
    znak = ('равно', 'запятая', 'меньше', 'больше', 'скобка1', 'скобка2', 'равно', 'тчкзпт')
    global word16       #эта переменная нужна, если в строке могут быть 16-ричные константы
    word16 = list('ABCDEFabcdef')
    global numb         #и эта переменная нужна, если в строке могут быть 16-ричные константы
    numb = list('0123456789')
    global result
    result = ''
    global resultWords
    resultWords = []
    global i
    i = -1
    global arr
    arr = arr_lex
    arr.append(('&', 'конец'))
    space()
    return resultWords

def space():
    global result       #отмечаем некоторые глобальные переменные заново, чтобы можно было их изменять
    global resultWords
    global i
    i += 1
    temp = arr[i][1]
    if temp == 'буква':
        result += arr[i][0]
        ident()
    elif temp == 'цифра':
        result += arr[i][0]
        whole()
    elif temp == 'пробел':
        space()
    elif temp in znak:
        resultWords.append((arr[i][0], arr[i][1]))
        space()
    elif temp == 'доллар':
        resultWords.append((arr[i][0], arr[i][1]))
        whole16()

def ident():
    global result
    global resultWords
    global i
    i += 1
    temp = arr[i][1]
    if temp == 'буква':
        result += arr[i][0]
        ident()
    elif temp == 'цифра':
        result += arr[i][0]
        ident()
    elif temp == 'пробел':
        resultWords.append((result, 'ИДЕНТИФ'))
        result = ''
        space()
    elif temp in znak:
        resultWords.append((result, 'ИДЕНТИФ'))
        result = ''
        resultWords.append((arr[i][0], arr[i][1]))
        space()
    elif temp == 'доллар':
        resultWords.append((result, 'ИДЕНТИФ'))
        result = ''
        resultWords.append((arr[i][0], arr[i][1]))
        whole16()
    elif temp == 'конец':
        resultWords.append((result, 'ИДЕНТИФ'))
        result = ''

def whole():
    global result
    global resultWords
    global i
    i += 1
    temp = arr[i][1]
    if temp == 'буква':
        err()
    elif temp == 'цифра':
        result += arr[i][0]
        whole()
    elif temp == 'пробел':
        resultWords.append((result, 'ЦЕЛОЕ'))
        result = ''
        space()
    elif temp in znak:
        resultWords.append((result, 'ЦЕЛОЕ'))
        result = ''
        resultWords.append((arr[i][0], arr[i][1]))
        space()
    elif temp == 'доллар':
        resultWords.append((result, 'ЦЕЛОЕ'))
        result = ''
        resultWords.append((arr[i][0], arr[i][1]))
        whole16()
    elif temp == 'конец':
        resultWords.append((result, 'ЦЕЛОЕ'))
        result = ''

def whole16():                  #это состояние нужно, если в строке могут быть 16-ричные константы, которым надо
    global result               #присвоить класс 'ЦЕЛОЕ'
    global resultWords
    global i
    i += 1
    temp = arr[i][1]
    temp1 = arr[i][0]
    if temp1 in word16:
        result += arr[i][0]
        whole16()
    elif temp == 'цифра':
        result += arr[i][0]
        whole16()
    elif (temp == 'буква'):     #если мы после знака доллара встречаем букву не из 16-ричной системы, то значит,
        if result[0] in numb:   #мы встретили идентификатор (надо снова проверить, что он начинается не с цифры)
            err()
        else:
            result += arr[i][0]
            ident()
    elif temp == 'пробел':
        if result != '':        #поскольку целое 16-ричное число мы можем и не встретить (ошибка не лексического блока),
                                #то перед добавлением элемента result в массив, важно проверить, что там что-то есть
                                #это, кнш, можно зачем-то реализовать через отдельное состояние, но кому это надо, лол
            resultWords.append((result, 'ЦЕЛОЕ'))
            result = ''
        space()
    elif temp in znak:
        if result != '':
            resultWords.append((result, 'ЦЕЛОЕ'))
            result = ''
        resultWords.append((arr[i][0], arr[i][1]))
        space()
    elif temp == 'доллар':
        if result != '':
            resultWords.append((result, 'ЦЕЛОЕ'))
            result = ''
        resultWords.append((arr[i][0], arr[i][1]))
        whole16()
    elif temp == 'конец':
        if result != '':
            resultWords.append((result, 'ЦЕЛОЕ'))
            result = ''

def err():
    print('Ошибка в лексике')


