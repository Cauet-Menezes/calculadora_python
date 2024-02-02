""" Calculadora com while """

while True: 
    numero_um   = input('Digite o primeiro numero: ')
    numero_dois = input('Digite o segundo numero: ')
    operador    = input('Digite o operador: ')
    operadores_validos = '*/-+'

    numeros_validos   = None
    numero_um_float   = 0
    numero_dois_float = 0

    try:
       numero_um_float   = int(numero_um)
       numero_dois_float = int(numero_dois)
       numeros_validos   = True
    except: 
       numeros_validos: None
    
    if numeros_validos is None: 
       print('Um ou mais numeros são inválidos!')
       continue 
    
    if len(operador) > 1 or operador not in operadores_validos:
        print('Apenas um operador por vez e apenas os permitidos (+,-,/,*)')
    else:
        if operador == '+':
            soma = numero_um_float + numero_dois_float
            print('%.3f' %soma)
        elif operador == '-':
            subtracao = numero_um_float - numero_dois_float
            print('%.3f' %subtracao)
        elif operador == '*' :
            multiplicacao = numero_um_float * numero_dois_float
            print('%.3f' %multiplicacao)
        elif operador == '/': 
            if numero_dois == 0:
             print('Não é possível dividir por zero!') 
            else:
             divisao = numero_um_float / numero_dois_float
             print('%.3f' %divisao)

    sair = input('Quer sair? [S]: ').lower().startswith('s')
    if sair is True: 
        break 