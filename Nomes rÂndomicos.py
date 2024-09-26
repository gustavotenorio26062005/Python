import random
lista = ["Gustavo","Thais","Carlos","Jair","Adler","Giovanni","Kaique","Osmar","Diego","Luis"]
listab = []
num=0
tam = int(len(lista)-1)
while len(listab) < tam:
    num = random.randint(0,tam)
    listab.append(lista[num])
    lista.remove(lista[num])
print(listab)