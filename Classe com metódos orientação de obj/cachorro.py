class Cachorro:

    def __init__(self,apelido,idade):
        self.apelido = apelido
        self.idade = idade

        pass

    def sentar(self):
        print(f"{self.apelido.title()} senta")
    pass

    def rolar(self):
        return f"{self.apelido} rola!"