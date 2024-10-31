import carro

fabricante=input("Insira o fabricante: ")
modelo=input("Insira o modelo: ")
ano=int(input("Ano: "))

ncarro = carro.Carro(fabricante,modelo,ano)

#print(ncarro)
#print(ncarro.exibir_descrição())

# ncarro.ler_hodometro()
# #ncarro.atualizar_hodometro(-10000)
# ncarro.incrementar_hodometro(100000)
# ncarro.ler_hodometro()
# ncarro.incrementar_hodometro(100000)
# ncarro.ler_hodometro()
# ncarro.incrementar_hodometro(-100000)
# ncarro.ler_hodometro()

carroE= carro.CarroEletrico(fabricante,modelo,ano)

carroE.get_descEletrico()
# carroE.abastecer_tanque()