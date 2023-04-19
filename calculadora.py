
'''
Referencias:
https://flexiple.com/python/python-switch-case/
https://www.geeksforgeeks.org/switch-case-in-python-replacement/
https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/
https://pythonguides.com/case-statement-in-python/

'''

# Classe de métodos


class Calculadora:
    # Métodos
    def __init__(self):
        pass

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def mutiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b

print(__name__)
if __name__ == '__main__':

    # Instânciar classe Calculadora()
    calculadora = Calculadora()


    # Entradas de dados
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))

    # Conjunto de operações
    listaoperacao = {
        1: calculadora.soma(a=num1, b=num2),
        2: calculadora.subtracao(a=num1, b=num2),
        3: calculadora.mutiplicacao(a=num1, b=num2),
        4: calculadora.divisao(a=num1, b=num2)
    }


    # Escolha da função no conjunto
    def switch(num):
        return listaoperacao.get(num, "Escolha inválida")


    # Menu de opções
    operacao = int(input("Escolha uma opecação: \n"
                         "- Digite 1 para soma \n"
                         "- Digite 2 para subtração \n"
                         "- Digite 3 para multiplicação \n"
                         "- Digite 4 para divisão \n"
                         "- : "))


    # Execução da operação escolhida
    print("Usando if:")
    if operacao == 1:
        print("Soma =", switch(operacao))
    elif operacao == 2:
        print("Subtração =", switch(operacao))
    elif operacao == 3:
        print("Multiplicação =", switch(operacao))
    elif operacao == 4:
        print("Divisão =", switch(operacao))
    else:
        print("Escolha inválida!")

    print("Usando case:")
    match operacao:
         case 1:
             print("Soma =", switch(operacao))
         case 2:
             print("Subtração =", switch(operacao))
         case 3:
             print("Multiplicação =", switch(operacao))
         case 4:
             print("Divisão =", switch(operacao))
         case _:
             print("Escolha inválida!")
