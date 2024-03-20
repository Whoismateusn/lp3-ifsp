''' Ex03 - Crie um programa em Python que recebe como entrada o valor de uma compra e apresenta como saída o valor final com desconto e o desconto aplicado com base nas seguintes regras:

    Compras entre R$ 0,01 e R$ 9,99 - 0% de desconto
    Compras entre R$ 10,00 e R$ 99,99 - 5% de desconto
    Compras entre R$ 100,00 e R$ 499,99 - 10% de desconto
    Compras iguais ou superiores a R$ 500,00 - 15% de desconto'''
    
    
valor_compra = 0.00
while valor_compra <= 0.00:
    valor_compra = float(input("Digite o valor da compra: "))

def get_desconto(valor):

    if valor >= 500.0:
        return 0.15
    if valor <= 499.99 and valor >= 100.0:
        return 0.1
    if valor <= 99.99 and valor >= 10.0:
        return 0.05
    
    return 0.0

print(f"Valor final: R$ {valor_compra - (valor_compra * get_desconto(valor_compra))}")
print(f"Desconto aplicado: {int(get_desconto(valor_compra) * 100)}%")