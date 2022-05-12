"""
Os modulos usados no código foram importados das bibliotecas.
As funções mais recorrentes no código foram escritas no arquivo funcoes.py e importadas no código

Classe Usuario para funcionarios e clientes.
Classe Produto para todos os produtos da loja.

Usuario 'administrador' para o primeiro usuário do sistema. Nivel 4, que possui todas permissões de terefas.
ID = admin; SENHA = 1234.

Produto 'teste' para realização de testes das tarefas do sistema.
CODIGO = code1111 (1111).

- Para uso não oficial e de facilitação de testes e exemplos foi determinado um código de barras ficticio de apenas 4 digitos que deverá ser reconfigurado para ser posto em usu oficial com auxilio de uma maquina de leitura de código de barras.

- O programa é executado somente nas ultimas linhas do código, tendo como seu principal corpo as funções referentes as tarefas possiveis.

Função login() para se conectar como Usuario.

Função menu() central de tarefas do programa.

[Nivel 1] Função consultar_produto() para ter acesso as informações detalhadas de um certo produto.

[Nivel 2] Função contabilizar_venda() para contabilizar uma venda e registra-la no banco de dados.

[Nivel 3] Função cadastrar_produto() para cadastrar um novo produto ou editar um já cadastrado, os armazenando no banco de dados.

[Nivel 4] Função consultar_usuario() para ter acesso as informações detalhadas de um funcionário ou cliente.

[Nivel 4] Função cadastrar_usuario() para cadastrar um novo usuario ou editar um já cadastrado, os armazenando no banco de dados.
"""


from funcoes import ler_codigo, ler_cpf, ler_dinheiro, ler_nivel, ler_senha, ler_sexo, sim_ou_nao


class Usuario:

    def __init__(self, nome, sobrenome, id, senha, nivel, cpf, sexo, nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.id = id
        self.senha = senha
        self.nivel = nivel
        self.cpf = cpf
        self.sexo = sexo
        self.nascimento = nascimento


class Produto:

    def __init__(self, codigo, nome, descricao, preco, ajuste):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.ajuste = ajuste


admin = Usuario('Administrador', 'do Sistema', 'admin', '1234', 4, 11122233344, 'm', None)
code1111 = Produto('1111', 'teste', 'apenas teste', 19.99, None)
usuarios = {'admin': admin}
produtos = {'code1111': code1111}
valido = False
usuario = None


def login():
    global valido
    global usuario
    print("""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-= BANCO DE DADOS  COMERCIAL =-=-=-=-=-=
=-=-=-=-=-= Faca login para  comecar! =-=-=-=-=-=""")
    repeticao = False
    while not repeticao:
        id = str(input("ID: "))
        if id not in usuarios:
            print('Usuário nao encontrado.')
        elif id in usuarios:
            senha = str(input('SENHA: '))
            if senha != usuarios[id].senha:
                print('Senha incorreta.')
            elif senha == usuarios[id].senha:
                repeticao = True
                valido = True
                usuario = id


def menu():
    global valido
    global usuario
    print(f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
          f"Conectado como: {usuario}\n"
          f"=-=-=-=-=-=-=- O que deseja fazer? -=-=-=-=-=-=-=")
    if usuarios[usuario].nivel == 4:
        print("""Consultar um produto........................[ 1 ]
Contabilizar uma venda......................[ 2 ]
Cadastrar um novo produto...................[ 3 ]
Consultar um usuário........................[ 4 ]
Cadastrar um novo usuário...................[ 5 ]
Sair........................................[ 0 ]""")
        opcao = str(input())
        if opcao == '1':
            consultar_produto()
        elif opcao == '2':
            contabilizar_venda()
        elif opcao == '3':
            cadastrar_produto()
        elif opcao == '4':
            consultar_usuario()
        elif opcao == '5':
            cadastrar_usuario()
        elif opcao == '0':
            valido = False
            principal()
        else:
            print('Opção não encontrada!')
            menu()
    

def consultar_produto():
    print('=-=-=-=-=-=-= CONSULTA DE  PRODUTOS =-=-=-=-=-=-=')
    repeticao = False
    while not repeticao:
        pesquisa = "code" + str(input('CÓDIGO: '))
        if pesquisa not in produtos:
            print('Produto não encontrado.')
        elif pesquisa in produtos:
            print(f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
                  f"PRODUTO: {pesquisa}\n"
                  f"{produtos[pesquisa].nome}\n"
                  f"{produtos[pesquisa].descricao}\n"
                  f"R$ {produtos[pesquisa].preco}\n"
                  f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        repeticao = True
        input()
        menu()


def contabilizar_venda():
    print('=-=-=-=-=-= CONTABILIZAÇÃO  DE VENDAS =-=-=-=-=-=')
    global valor_inicial
    valor_inicial = 0.0

    def continuar_venda():
        global valor_final
        print(f"Contabilizar outro produto..................[ 1 ]\n"
              f"Finalizar a venda...........................[ 2 ]")
        resposta = sim_ou_nao()
        if resposta == '1':
            adicionar_produto()
        elif resposta == '2':
            print(f"VALOR FINAL: {valor_final}\n"
                  f"Confirmar...................................[ 1 ]\n"
                  f"Cancelar....................................[ 2 ]")
            resposta = sim_ou_nao()
            if resposta == '1':
                valor_pago = round(ler_dinheiro('VALOR PAGO PELO CLIENTE: '))
                valor_troco = valor_pago - valor_final
                print(f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
                      f"VALOR FINAl: {valor_final}\n"
                      f"VALOR PAGO: {valor_pago}\n"
                      f"TROCO: {valor_troco}\n"
                      f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                input()
                menu()
            elif resposta == '2':
                input()
                menu()

    def adicionar_produto():
        global valor_inicial
        global valor_final
        pesquisa = ler_codigo('CÓDIGO: ')
        if "code" + pesquisa in produtos:
            codigo = "code" + pesquisa
            valor_final = valor_inicial + produtos[codigo].preco
            valor_inicial = valor_final
            print(f"PRODUTO: {produtos[codigo].nome} | R$ {produtos[codigo].preco}\n"
                  f"VALOR TOTAL: R$ {valor_final}")
            continuar_venda()

        elif "code" + pesquisa not in produtos:
            print(f"Produto não encontrado!"
                  f"VALOR TOTAL: R$ {valor_final}")
            continuar_venda()

    adicionar_produto()


def cadastrar_produto():

    def novo_produto():
        codigo = "code" + pesquisa
        nome = str(input('NOME: '))
        descricao = str(input('DESCRIÇÃO: '))
        preco = ler_dinheiro('PREÇO: ')
        produto_adicionado = Produto(codigo, nome, descricao, preco, None)
        produtos[codigo] = produto_adicionado

    print('=-=-=-=-=-=-= CADASTRO DE  PRODUTOS =-=-=-=-=-=-=')
    pesquisa = ler_codigo('CÓDIGO: ')
    if "code" + pesquisa in produtos:
        print('Produto já cadastrado! Deseja edita-lo?\n'
              'Sim.........................................[ 1 ]\n'
              'Não.........................................[ 2 ]')
        resposta = sim_ou_nao()
        if resposta == '1':
            del produtos["code" + pesquisa]
            novo_produto()
        elif resposta == '2':
            pass     
    elif "code" + pesquisa not in produtos:
        novo_produto()
           
    input()
    menu()


def consultar_usuario():
    print('=-=-=-=-=-=-= CONSULTA DE  USUÁRIOS =-=-=-=-=-=-=')
    repeticao = False
    while not repeticao:
        pesquisa = str(input('ID: '))
        if pesquisa not in usuarios:
            print('Usuário não encontrado.')
        elif pesquisa in usuarios:
            print(f"USUÁRIO: {pesquisa}\n"
                  f"NOME: {usuarios[pesquisa].nome} {usuarios[pesquisa].sobrenome}\n"
                  f"CPF: {usuarios[pesquisa].cpf}"
                  f"SEXO: {usuarios[pesquisa].sexo}"
                  f"NIVEL: {usuarios[pesquisa].nivel}\n"
                  f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        repeticao = True
        input()
        menu()


def cadastrar_usuario():

    def novo_usuario():
        id = pesquisa
        nome = str(input('NOME: '))
        sobrenome = str(input('SOBRENOME: '))
        cpf = ler_cpf('CPF: ')
        sexo = ler_sexo('SEXO: ')
        nivel = ler_nivel('NIVEL: ')
        senha = ler_senha('SENHA: ')
        usuario_adicionado = Usuario(nome, sobrenome, id, senha, nivel, cpf, sexo, None)
        usuarios[pesquisa] = usuario_adicionado

    print('=-=-=-=-=-=-= CADASTRO DE  USUÁRIOS =-=-=-=-=-=-=')
    pesquisa = str(input('ID: '))
    if pesquisa in usuarios:
        print('Usuário já cadastrado! Deseja edita-lo?\n'
              'Sim.........................................[ 1 ]\n'
              'Não.........................................[ 2 ]')
        resposta = sim_ou_nao()
        if resposta == '1':
            del usuarios[pesquisa]
            novo_usuario()
        elif resposta == '2':
            pass
    elif pesquisa not in usuarios:
        novo_usuario()

    input()
    menu()


# Código Principal do programa
def principal():
    login()
    if valido == True:
        menu()

principal()
