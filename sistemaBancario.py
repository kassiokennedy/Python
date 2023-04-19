'''
https://academiapme-my.sharepoint.com/:p:/g/personal/kawan_dio_me/Ef-dMEJYq9BPotZQso7LUCwBJd7gDqCC2SYlUYx0ayrGNQ?rtime=6BGAHCWu2kg
https://github.com/digitalinnovationone/trilha-python-dio/blob/02_programacao_orientada_objetos/02%20-%20Programa%C3%A7%C3%A3o%20Orientada%20a%20Objetos/10%20-%20desafio/desafio_v2.py
https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/15120778#overview
https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/15099776#overview
inserção de texte para commit
'''
import random

# Variavel global
saldo = 1000
i = 0
a = 0
extrato = ''

# --------------------------------------------------------


class Pessoa:
    def __init__(self):
        pass

    def novoUsuario(self):
        nome = input("Informe seu nome: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        cpf = int(input("informe somente os numeros do seu CPF: "))
        # endereço (rua, numero- bairro - cidade/estado
        endereco = input("Informe o endereço (logradouro, num - bairro - cidade/sigla estado): ")

# --------------------------------------------------------


class Cliente:
    '''
    https://github.com/kassiokennedy/cursoPython/blob/7e2536b6f0d06b4133f12adf4bc7c7b9eda16a2d/cursoudemy/Secao04/encapsulamento.py
    '''
    def __init__(self):
        self.dados = {}
        self.clientes = {}

    def novaConta(self, nome, username, agencia, conta):
        global a
        # clientes = {nome: '', agencia: '', conta: ''}
        print("Informe os dados da conta.")
        nome = input("Nome de usuário: ")
        agencia = 1
        conta = random.randint(0000,9999)

        if a not in self.clientes:
            self.clientes[a] = {'Nome':nome,'Ag': agencia ,'CC': conta}
            a += 1
        else:
            self.clientes[a].update({'Nome':nome,'Ag': agencia ,'CC': conta})

        return print(f'''
        Usuário: {nome}
        Agência: {agencia}
        Conta:   {conta}
        ''')

    def listaContas(self):

        print('\nLista de contas:')
        '''
        x = self.clientes.items()
        print(x)
        '''
        a = 0
        for chave, valor in self.clientes.items():
            '''
            for k, v in self.clientes.items():
                print(k, v)2
                a += 1
            '''
            print(f'Cliente: {chave}')
            for dados1, dados2 in valor.items():
                print(f'''      {dados1}:{dados2}''')
            a += 1

    def inserirCliente(self, nome, username):
        nome = input("Nome o nome completo: ")
        username = input("Digite o nome de usuario: ")

        if 'clientes' not in self.dados:
            self.dados['clientes'] = {nome: username}
        else:
            self.dados['clientes'].update({nome: username})

    def listaClientes(self):
        print('\nLista de clientes:')
        for nome, username in self.dados['clientes'].items():
            print(f'    Nome: {nome}; Usuário: {username}')

# --------------------------------------------------------


class Banco:

    def __init__(self):
        pass

    def lista(self):
        if not Cliente.novaConta:
            print("Nada aqui.")
        else:
            print("erro")

    def depositar(self):
        global saldo
        global extrato
        deposito = float(input("\nDeposite seu dinheiro: "))
        if deposito <= 0:
            print("\nNao é permitido deposito negativo ou valor zero.")
        else:
            saldo += deposito
        extrato += f'\nDepósito: {deposito:.2f} R$'
        return print(f'Seu saldo é de {saldo:.2f} R$\n')

    def sacar(self):
        global saldo # chamada da variavel global
        global i
        global extrato
        if saldo > 0 and i <=4: # Verifica se ha saldo para a operacao
            saque = float(input(
                f'\nSeu saldo é de {saldo:.2f} R$\n'
                f'Informe o valor do saque: '))
            if saque <= 0 or saque > 500:
                return print("Limite de 500,00 R$ por saque!.")
            else:
                saldo -= saque
            extrato += f'\nSaque: {saque:.2f} R$'
            i += 1
        else:
            if saldo <= 0:
                print("\nSaldo insuficiente.")
            else:
                print("\nSeulimite é de ate 3 saques diários.")

        return print(f'\nSeu saldo é de {saldo:.2f} R$\n')

    def extrato(self):
        if not extrato:
            print(f'''
-------------------- Extrato --------------------------- 
            Não ha movimentações.
--------------------------------------------------------
                        ''')
        else:
            print(f'''
-------------------- Extrato --------------------------- 
{extrato}
\nSeu saldo é de {saldo:.2f} R$\n
--------------------------------------------------------
            ''')

#################################################################
#################################################################
#################################################################

# print(__name__)
if __name__ == '__main__':
    # instanciando as classes
    banco = Banco()
    pessoa = Pessoa()
    cliente = Cliente()

    while True:
        # Menu de opções
        operacao = int(input(
            f'''
-------------------- Menu ------------------------------ 
        1 - Nov@ usuári@
        2 - Nova conta
        3 - Saque
        4 - Depósito
        5 - Extrato
        6 - Lista de contas
        7 - Lista de clientes
        8 - Sair 
--------------------------------------------------------
Escolha uma operação:'''))
        if operacao == 1:
            print(cliente.inserirCliente(any, any))

        elif operacao == 2:
            print(cliente.novaConta(any, any, any, any))

        elif operacao == 3:
            print(banco.sacar())

        elif operacao == 4:
            print(banco.depositar())

        elif operacao == 5:
            print(banco.extrato())

        elif operacao == 6:
            print(cliente.listaContas())

        elif operacao == 7:
            print(cliente.listaClientes())

        elif operacao == 8:
            print("\nFechando o programa.")
            break
        i += 1
