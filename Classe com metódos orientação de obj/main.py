import aluno
import cachorro
#prontuario = input("Informe seu protuário").upper()
#nome = input("Informe seu nome").capitalize()

#novoaluno = aluno.Aluno(prontuario,nome)

#print(novoaluno.nome)

#novoaluno.exibir()

dog,idade = input("Qual o apelido do cachorro? "), int(input("Qual a idade do cachorro? "))
novocachorro = cachorro.Cachorro(dog,idade=5)

print(novocachorro.apelido)
print(novocachorro.idade)

novocachorro.sentar()
print(novocachorro.rolar())