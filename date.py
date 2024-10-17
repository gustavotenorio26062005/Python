def opcao(op):
    def soma():
        x = int(input("Inclua o 1º número da soma: "))
        y = int(input("Inclua o 2º número da soma: "))
        return x + y

    def subtracao():
        x = int(input("Inclua o 1º número da subtração: "))
        y = int(input("Inclua o 2º número da subtração: "))
        return x - y

    def multiplicacao():
        x = int(input("Inclua o 1º número da multiplicação: "))
        y = int(input("Inclua o 2º número da multiplicação: "))
        return x * y

    def divisao():
        x = int(input("Inclua o 1º número da divisão: "))
        y = int(input("Inclua o 2º número da divisão: "))
        return x / y

    match op:
        case 1:
            return soma()
        case 2:
            return subtracao()
        case 3:
            return multiplicacao()
        case 4:
            return divisao()
        case _:
            return f"Valor {op} inválido"


