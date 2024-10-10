#Chamados de set.
#Ele é uma coleção desordenada de elementos. Não tem indice
#Não possui elementos repetidos

listaB=[10,20,30,10,10,30,60]
conjunto = set(listaB)
print(conjunto)

dicionario={1:20,2:30,3:40}
conjunto = set(dicionario)
print(conjunto)
conjunto2 = set(dicionario.values())
print(conjunto)
conjunto3 = set(dicionario.items())
print(conjunto)

a = set('abracadabra')
b = set('alacazam')

print(a & b)
print(a - b)
print(b - a)
print(a | b)
print(a ^ b)
k = {x for x in 'abacadabra' if x not in 'abc'}
