import random
max = int(input('limite superior: '))
min = int(input('limite inferior: '))
i = 1
num = random.randint(min,max)
lista = []
valor = int(input("Faça sua 1º tentativa: "))

while valor != num:
    lista.append(valor)
    if valor > num:
        print("Você errou, o número sorteado foi menor, escolha um número menor: ")
    elif valor < num:
        print("Você errou, o número sorteado foi maior, escolha um número maior: ")
    i+=1
    valor = int(input(f"Faça sua {i}º tentativa: "))
lista.append(valor)
print(f"Você acertou!!, o número sorteado foi esse mesmo, parabéns, demorou {i} tentativas")
print(f"Os números digitados foram {lista}")

