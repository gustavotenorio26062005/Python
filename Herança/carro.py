class Carro:

    def __init__(self,fabricante,modelo,ano):
        self.fabricante= fabricante
        self.modelo=modelo
        self.ano=ano
        self.cor="branco"
        self.hodometro = 0
        self.tanque = 10
        pass

    #Metódo para exibir dados do carro
    #Definindo uma assinatura do metódo
    def exibir_descrição(self):
        nome_extenso=str(self.ano)+" "+ self.fabricante+" "+self.modelo
        return nome_extenso
    #Metódo para a leitura do hodometro
    def ler_hodometro(self):
        print(f"O carro tem {self.hodometro} km rodados")
        pass
    def atualizar_hodometro(self,kms):
        if kms>= self.hodometro:
            self.hodometro = kms
        else:
            print("VocÊ está tentando reduzir o valor do hodômetro!")
        pass

    #Metódo para incrementar o hodometro
    def incrementar_hodometro(self,kms):
        if kms > 0:
            self.hodometro += kms
        pass

    #Método usado para retornar auma representação de string de um objeto 
    def __str__(self):
        return f"Carro {self.fabricante}\nModelo{self.modelo}\nAno{self.ano}\nHodometro{self.hodometro}\nA cor é{self.cor}"
    
    def __repr__(self):
        return f"<Carro>({self.fabricante})\n<Modelo>({self.modelo})\n<Ano>({self.ano})\n<Hodometro>({self.hodometro})\n<A cor é>({self.cor})"
    
    def set_cor(self,cornova):
        self.cor=cornova

    def abastecer_tanque(self,litros):
        self.tanque+=litros
        print(f"O tanque foi atualizado para {self.tanque} litros.")

class CarroEletrico(Carro):
    
    def __init__(self, fabricante, modelo, ano):
        super().__init__(fabricante, modelo, ano)
        self.bateria = Bateria()

    def get_descEletrico(self):
        print(f"Carro elétrico {self.fabricante}\nModelo{self.modelo}\nAno{self.ano}\nHodometro{self.hodometro}\nA cor é{self.cor}\nBateria {self.bateria.capacidade}")
    
    def abastecer_tanque(self):
        print(f"Esse modelo não tem tanque!")

class Bateria:
    def __init__(self,capacidade=70):
        self.capacidade = capacidade

    def  get_bateria(self):
        print(f"Bateria com{self.capacidade}")