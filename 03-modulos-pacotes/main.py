#uso chamada das funcoes

import funcoes #traz o modulo todo

print(funcoes.somar(10,2))
print(funcoes.multiplicar(10,2))


from funcoes import somar, multiplicar #trazas que quiser separadamente 

print(somar(10,7))
print(multiplicar(10,4))

from funcoes import * #traz o modulo todo mas separadamente, mlhr q o primeiro

print(somar(10,7))
print(multiplicar(10,4))


from funcoes import somar, multiplicar
from funcoes2 import somar as cadeira


print(somar(10,7))
print(cadeira(10,7))
