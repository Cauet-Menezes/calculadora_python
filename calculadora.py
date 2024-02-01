""" Calculadora com while """

while True: 
    numero_um   = float(input('Digite o primeiro numero: '))
    numero_dois = float(input('Digite o segundo numero: '))
    operador    = input('Digite o operador: ')

    if operador == '+':
        soma = numero_um + numero_dois
        print('%.3f' %soma)
    elif operador == '-':
        subtracao = numero_um - numero_dois
        print('%.3f' %subtracao)
    elif operador == '*' :
        multiplicacao = numero_um * numero_dois
        print('%.3f' %multiplicacao)
    elif operador == '/': 
        if numero_dois == 0:
         print('Não é possível dividir por zero!') 
        else:
         divisao = numero_um / numero_dois
         print('%.3f' %divisao)

    sair = input('Quer sair? [S]: ').lower().startswith('s')
    if sair is True: 
        break 