#Considerando 3 alunos com as respectivas nomes e notas
#Pedro, nota 1 = 10,nota 2 = 6
#Maria, nota 1 = 4,5,nota 2 = 8,5
#Bob, nota 1 = 5,5,nota 2 = 7,5
alunos={}
alunos['nome']=['Maria','Bob','Pedro']
alunos['nota']=[10,6,4.5,8.5,5.5,7.5]

x=0
y=x+1
print(alunos)
media=[]
for z in alunos['nome']:
    print(f"Nota 1 : {alunos['nota'][x]} + Nota 2 :{alunos['nota'][y]}")

    soma = alunos['nota'][x]+alunos['nota'][y]
    media.append(soma/2)
    x+=2
    y+=2
print(f"A média de Pedro foi : {media[0]}\nA média de Maria foi : {media[1]}\nA média de Bob foi : {media[2]}")
