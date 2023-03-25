# Calculadora em Python

# Atribuição Lógica de valores

def add(x, y):
    return x + y
def subtraction(x, y):
    return x - y
def multyply(x * y):
    return x * y
def devide(x, y):
    return x / y
    
# Apresentação ao usuario
    
print("Bem vindo ao Calculus3000! Selecione uma das opções abaixo")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Sistema para funcionamento da caculadora

while True:
    choice = input(("Selecione uma opção (1/2/3/4): )
    if choice != ("1", "2", "3", "4" ):
        print("Por favor, selecione um numero válido")
    elif choice in ("1", "2", "3", "4" ):
        try:
            num1 = int(input("Digite o primeiro algarismo da operação:") )
            num2 = int(input("Digite o segundo algarismo da operação:") )
           except ValueError:
                print("Opção invalida! Selecione um número válido" )
           if choice == '1':
                print(num1, '+', num2, '=', add(num1, num2) )
           elif choice == '2':
                print(num1, '-', num2, '=', subtraction(num1, num2) )
           elif choice == '3':
                print(num1, '*', num2, '=', multyply(num1, num2) )
           elif choice == '4':
                print(num1, '/', num2, '=', devide(num1, num2) )
    choice2 = input("Quer calcular denovo? (s/n):" )
    if choice2 == "n":
        break
    else:
        print("Função desconhecida")

# Fim do programa
