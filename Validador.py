while True:
    cpf = input('Digite seu cpf apenas com 11 numeros : ')

    if not cpf.isnumeric():
        print('Digite seu cpf apenas com numeros !!!!!!!! ')
        continue
    elif len(cpf) < 11 or len(cpf) > 11:
        print('Digite seu cpf apenas com 11 numeros !!!!')
        continue
    else:
        n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11 = list(cpf) #separando cada algorismo da string cpf
        n1 = int(n1)               #transform
        n2 = int(n2)
        n3 = int(n3)
        n4 = int(n4)
        n5 = int(n5)
        n6 = int(n6)
        n7 = int(n7)
        n8 = int(n8)
        n9 = int(n9)
        n10 = int(n10)
        n11 = int(n11)
        x = (n1 * 10 + n2 * 9 + n3 * 8 + n4 * 7 + n5 * 6 + n6 * 5 + n7 * 4 + n8 *3 + n9 * 2 ) #calcular o digito 1
        d1 = 11 - (x % 11)
    if d1 >= 9:                      #verificar o digito 1
        z = 0
    else:
        print('CPF INVALIDO')
        exit()
    if z == 0:                      #checa o digito 2
        d2 = (n1 * 11 + n2 * 10 + n3 * 9 + n4 * 8 + n5 * 7 + n6 * 6 + n7 * 5 + n8 * 4 + n9 * 3 + d1 * 2)
        Ultimo_digito = 11 - (d2 % 11)
        break
if Ultimo_digito == n11: #finalizando se é valido ou não
    print('CPF VALIDADO')
    exit()
elif Ultimo_digito != n11:
    print('CPF INVALIDO')
