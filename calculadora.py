def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def subtrair (a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por 0!"
    return a / b

def exponencial (a, b):
    return a ** b

✔️ b) Usar entrada do usuário (modo interativo no terminal)
def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def subtrair(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por 0!"
    return a / b

def exponencial(a, b):
    return a ** b

# Programa principal
print("Escolha a operação:")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print("5 - Exponencial")

op = input("Digite o número da operação: ")

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if op == "1":
    print("Resultado:", somar(a, b))
elif op == "2":
    print("Resultado:", subtrair(a, b))
elif op == "3":
    print("Resultado:", multiplicar(a, b))
elif op == "4":
    print("Resultado:", dividir(a, b))
elif op == "5":
    print("Resultado:", exponencial(a, b))
else:
    print("Operação inválida!")