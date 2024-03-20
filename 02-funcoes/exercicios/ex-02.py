#Ex02 - Escreva um programa em Python que solicita ao usuário três números e apresenta a média aritmética dos números informados.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceira número: "))

def get_media(*numeros):
    return sum(numeros) / len(numeros)

print(f"Média aritmética: {get_media(numero1, numero2, numero3)}")