def block1(string):     #блок создаёт из полученной строки список из символов и их класса
    alph = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')     #создаём и заполняем список алфавита
    num = list('0123456789')     #список цифр
    chek = True     #создаём переменную для проверки на ошибку
    # ...и отдельно создаём словарь всех прочих допустимых в строке символов
    dollar = ('$', 'доллар')
    opbrace = ('(', 'скобка1')
    clbrace = (')', 'скобка2')
    space = (' ', 'пробел')
    semicolon = (';', 'тчкзпт')
    comma = (',', 'запятая')
    less = ('<', 'меньше')
    more = ('>', 'больше')
    equally = ('=', 'равно')
    sym = {'$':dollar,' ':space,',':comma,';':semicolon,'=':equally,'<':less,'>':more,'(':opbrace,')':clbrace}

    arr = []     #создаём  список, куда помещаем символы, одновременно присваивая им классы
    for i in string:
        if i in alph:
            alph1 = (i, 'буква')
            arr.append(alph1)
        elif i in num:
            num1 = (i, 'цифра')
            arr.append(num1)
        elif i in sym.keys():
            arr.append(sym.get(i))
        else:
            err = (i, 'ошибка')
            arr.append(err)
            print('Недопустимый символ')
    return arr


