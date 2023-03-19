import lexical

def block3(arr_lex):
    lex = arr_lex
    arr = []
    keywords = ('while', 'do', 'if', 'then')
    banwords = ('and', 'end', 'nil', 'set', 'array', 'file', 'not', 'begin', 'for', 'of', 'to',
                'case', 'function', 'or', 'type', 'const', 'goto', 'packed', 'until', 'div',
                'procedure', 'var', 'in', 'program', 'downto', 'label', 'record', 'with', 'else',
                'mod', 'div', 'repeat')
    logconst = ('true', 'false')
    for i in lex:
        if i[0].lower() in keywords:
            arr.append('КЛЮЧЕВОЕСЛОВО_' + i[0].upper())
        elif i[0].lower() in logconst:
            arr.append('ЛОГКОНСТ_' + i[0].upper())
        elif i[0].lower() in banwords:
            arr.append('ОШИБКА')
            print('Недопустимое название переменной')
        else:
            arr.append(i[1])
    return arr