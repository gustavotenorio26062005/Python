nomes = ['Gustavo',"Ana",'Tenório']
lista=[]
for condicao in nomes:
    if len(condicao)>4:
        nomes.insert(0,condicao)
        print(f'Nome : {condicao} e tamanho {len(condicao)}')
        

