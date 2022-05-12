def sim_ou_nao():
    valido = False
    while not valido:
        resp = str(input()).strip()
        if resp == '1':
            valido = True
            return resp
        elif resp == '2':
            valido = True
            return resp
        else:
            print('Insira uma opção valida!')


def ler_codigo(cod):
    valido = False
    while not valido:
        entrada = str(input(cod)).strip()
        if not entrada.isnumeric() or len(entrada) < 4 or len(entrada) > 4:
            print('Valor invalido!')
        else:
            valido = True
            return str(entrada)


def ler_dinheiro(din):
    valido = False
    while not valido:
        entrada = str(input(din)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('Valor invalido!')
        else:
            valido = True
            return round(float(entrada), 2)


def ler_sexo(sex):
    valido = False
    while not valido:
        entrada = str(input(sex)).strip().upper()
        if entrada == 'M':
            valido = True
            return entrada
        elif entrada == 'F':
            valido = True
            return entrada
        elif entrada != 'M' or entrada != 'F':
            print('Insira uma opção valida!')


def ler_cpf(cpf):
    valido = False
    while not valido:
        entrada = str(input(cpf)).strip()
        if not entrada.isnumeric() or len(entrada) < 11 or len(entrada) > 11:
            print('Valor invalido!')
        else:
            valido = True
            return int(entrada)


def ler_nivel(niv):
    valido = False
    while not valido:
        resp = str(input(niv)).strip()
        if resp == '1' or resp == '2' or resp == '3' or resp == '4':
            valido = True
            return int(resp)
        else:
            print('Insira uma opção valida!')


def ler_senha(sen):
    valido = False
    while not valido:
        entrada = str(input(sen)).strip()
        if len(entrada) < 4:
            print('Valor invalido!')
        else:
            valido = True
            return entrada