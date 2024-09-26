import random
lista = ["Gustavo","Thais","Carlos","Jair","Adler","Giovanni","Kaique","Osmar","Diego","Luis"]
listab = []
num=0
tam = len(lista)
i=tam
while len(listab) < i:
    if tam != 0:
        tam-=1
    num = int(random.randint(0,tam))
    listab.append(lista[num])
    lista.remove(lista[num])
print(listab)