
#Uma pista de kart permite 5 voltas para cada um de 3 corredores
#Escreva um programa que leia todos os tempos em segundos e os guarde 
# em um dicionário, onde a chave é o nome do corredor. A o final diga quem foia melhor volta 
# da prova e em qual, ainda a ordem do campeão com a menor média

corrida={}
voltas=corrida.fromkeys([1,2,3],0)

voltas[1]= [input("1º volta"),input("2º volta"),input("3º volta"),input("4º volta"),input("5º volta")]
voltas[2]= [input("1º volta"),input("2º volta"),input("3º volta"),input("4º volta"),input("5º volta")]
voltas[3]= [input("1º volta"),input("2º volta"),input("3º volta"),input("4º volta"),input("5º volta")]

for i  in voltas[1]:
    soma = sum(voltas.values)
    media1 = soma/len(voltas.values)
for i in voltas[2]:
    soma = sum(voltas.values)
    media2 = soma/len(voltas.values)
for i in voltas[3]:
    soma = sum(voltas.values)
    media3 = soma/len(voltas.values)
print(media1)