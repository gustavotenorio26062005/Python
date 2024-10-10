    ### Dicionário
    #Não existe indices, pois não é ordenada
    #Acesso por meio de chaves
    #São criados pela combinação de chave e valor
    #São mutáveis
    #Adicionar e remover itens (elementos).
    #Utilizar as chaves {...} para criar um dicionário
    #Os elementos são separados por ,vírgulas
#Criar dicionários por meio do construtor dict()
#Passando dois tipos de parâmetros:
    #Lista de tuplas(Cada tupla contém uma chave e um contéudo)
    #Sequência de itens (No formato chave = valor).
nomes={1: "Gu",2:"Tenório",3:"Barros"}#Chaves como números inteiros
type(nomes)
nomesA={"A": "Gu","B":"Tenório","C":"Barros"}
#Chaves como string delimitadas por aspas simples ou duplas
# In verifica a chave e não o valor
1 in nomes #Verifica se chave existe caso sim = true, else false

#Dicionário a partir de lista de tuplas
t1=(1,"gu")
t2=(2,5)
t3=(3,["teste","esse"])
lista = [t1,t2,t3]
dicio = dict(lista)

#Dicionário a partir de sequecia de pares chave = valor
#Ser strings, porem não escritas entre aspas, nem simples nem duplas

dict(a= 10, b=11, c= 12)
tupla =(2,3,4,5,6)
lista=[]
for y in tupla:
    print(f"x2 = {y**2}")
    lista.append({y,y**2})
    
dic=dict(lista)
print(dic)

nomes.fromkeys([4,2],[2,4])
nomesA.get('A',2)

nomesA.items()

nomesA.keys()
nomes.values()

nomesA.pop("B")

nomesA.popitem

nomesA['B'] = 1
nomesA['C'] = 2

nomesB = {10:"Cidade A",20:"Cidade A"}
nomesA.update(nomesB)
