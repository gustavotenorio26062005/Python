numeros = [1,2,3,4,5]
num = [6,7,8,9]
numeros.append(1)
print(f"Lista: {numeros}")#Adiciona o elemento ao final da lista, caso eu colocasse uma lista iria acrescentar a lista toda
numeros.extend(num)
print(f"Lista: {numeros}")#Adiciona os valores da variável a lista
numeros.remove(2)
print(f"Lista: {numeros}")#Remove o número passado por parâmetro do indice
numeros.pop(0)
print(f"Lista: {numeros}")

listaA = ['Ramon','Gu','Teste','Jair',"Danilo"]
listaA.sort()
print(f"Lista: {listaA}")
listaA.sort(reverse=True)
print(f"Lista: {listaA}")
listaA.sort(reverse=False)
print(f"Lista: {listaA}")
listaA.reverse()
print(f"Lista: {listaA}")
