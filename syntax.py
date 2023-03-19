import identifical

def block4(arr_lex):
    i = -1
    global test
    test = 'REJECT'
    global arr
    arr = arr_lex
    arr.append('конец')
    start(i)
    return test

def start(i):
    i += 1
    if arr[i] == 'КЛЮЧЕВОЕСЛОВО_WHILE':
        while1(i)

def while1(i):
    i += 1
    if arr[i] == 'ЛОГКОНСТ_FALSE' or arr[i] == 'ЛОГКОНСТ_TRUE':
        do1(i)

def do1(i):
    i += 1
    if arr[i] == 'КЛЮЧЕВОЕСЛОВО_DO':
        if1(i)

def if1(i):
    i += 1
    if arr[i] == 'КЛЮЧЕВОЕСЛОВО_IF':
        iden(i)

def iden(i):
    i += 1
    if arr[i] == 'ИДЕНТИФ':
        znak(i)

def znak(i):
    i += 1
    if arr[i] == 'равно':
        dollar(i)
    elif arr[i] == 'больше':
        if arr[i + 1] == 'равно':
            i += 1
        dollar(i)
    elif arr[i] == 'меньше':
        if arr[i + 1] == 'равно' or arr[i + 1] == 'больше':
            i += 1
        dollar(i)

def dollar(i):
    i += 1
    if arr[i] == 'доллар':
        whole(i)

def whole(i):
    i += 1
    if arr[i] == 'ЦЕЛОЕ':
        then(i)

def then(i):
    i += 1
    if arr[i] == 'КЛЮЧЕВОЕСЛОВО_THEN':
        iden2(i)

def iden2(i):
    i += 1
    if arr[i] == 'ИДЕНТИФ':
        opbrace(i)

def opbrace(i):
    i += 1
    if arr[i] == 'скобка1':
        iden3(i)

def iden3(i):
    i += 1
    if arr[i] == 'ИДЕНТИФ':
        if arr[i + 1] == 'запятая':
            i += 1
            iden3(i)
        else:
            clbrace(i)

def clbrace(i):
    i += 1
    if arr[i] == 'скобка2':
        semicolon(i)

def semicolon(i):
    i += 1
    if arr[i] == 'тчкзпт':
        end(i)

def end(i):
    global test
    i += 1
    if arr[i] == 'конец':
        test = 'ACCEPT'