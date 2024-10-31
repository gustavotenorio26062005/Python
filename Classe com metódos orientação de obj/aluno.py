class Aluno:

    def __init__(self,prontuario,nomeCompleto):
        self.pront = prontuario
        self.nome = nomeCompleto
    
    def exibir(self):
        print(f"Seu nome é {self.pront} e seu prontuário é {self.pront}")