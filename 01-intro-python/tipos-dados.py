#tipos de dados

#Numérico

#Int
idade = 10


#Float
altura = 1.65

#boolean
# True, False (maiusculo)
verdade = True
mentira = False
Ligado = True
Desligado = False
frete_gratis = True

#string - str
# sequencia de caracteres
#literal de str
# " " e ' 'funsiconam... mas usar padronizado
nome = 'José'
nome = "José"

#char q nvdd n tem... e é usado str

letra = "a"


#ele respeita a quebra de linhas com as aspas 
frase = """Olá
teste
teste"""

#inerpolação de string
nome = 'Sonia'
idade = 23

# f-string
mensagem = f"bom dia{nome}, você tem {idade} anos! "

nome = 'Silvio santos'

print(nome[1])
print(nome[2])
print(nome[0:3])

#str são objetos 
#métodos
print (nome.upper())
print (nome)

#list
#lista de valores
#pode conter valoreas de tipos diferentes
#pode ser alterada (add, remover)
habilidades = [ 'java', 'html', 'css' ]
print(habilidades)[0] = 'javascript'
print(habilidades)

#adc nfinal da lista
habilidades.append('python')
print(habilidades)

#adc em uma posiçao
habilidades.isert(0, 'koto')
print(habilidades)


# revove, sort, clear, copy

for habilidades in habilidades:
    print(habilidades)

#tuples
#lista de valores 
#não pode alterar os valores
#só muda os "[]" pelos '()'
opções = ('sim', 'nao', 'talvez')
racas_rpg ('anao', 'humano', ' sla')

print(opções[1])

#funçao q retorna estatisticas
#sobre as notas e um aluno
#media, menor nota, maior nota
#entrada n1, n2, n3 ou notas (list)
#saida media, menor nota, maior nota
def estatistica_nota(notas):
    media = sum(notas) / len (notas)
    menor = min(notas)
    maior = max(notas)
    return media, maior, menor 

notas = [10.0, 5.5, 3.2, 1.8]
estatistica = estatistica_nota
print(estatistica)
print(type(estatistica)) #tipo é p especiicar aformatação que vai devolver e pds c da o parametro

#descompactador de tupla
media, menor, maior  = estatistica_nota(notas)
print (media, menor, maior)

#set
#conjunto de valores
#nao permite valores duplicados
#não é indexado

habilidades = ('Java', 'python', 'css')
habilidades.add('Java')
print(habilidades)

#dict
#dicionário
#palavras 
#palavras => definições
# key => value

nome = 'Silvio Santos'
idade = 120
casado = True

pessoa = {
    "nome": ' silvio'
    "idade": 120
    "casado": True
}

print(possoa['nome'])


#none
#null

none = null