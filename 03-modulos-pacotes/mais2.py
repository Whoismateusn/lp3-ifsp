from matematica.constantes import pi
from matematica.funcoes import somar, multiplicar #ou "... import * "
from estatistica.funcoes import media #ou "... import * "
from matematica.geometria.funcoes import area_quadrado

print(somar(1, 3))
print(multiplicar(1, 3))
print(pi)

notas = [10.0, 4.6, 5.4]
print(media(notas))

print(area_quadrado(3))

