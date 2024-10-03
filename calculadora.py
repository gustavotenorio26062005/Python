opcao = int(input('******opcoes******\nOpção 1 somar\nOpção 2 subtrair\nOpção 3 média\nOpção 4 finalizar: '))
valores = []
while opcao != 4:
    if opcao == 1:
        for i in range(0,2):
            valores.append(int(input(f"Valor {i} da soma: ")))
        print(f'O resultado da soma é: {sum(valores)}')4
        valores = []
        opcao = int(input('******opcoes******\nOpção 1 somar\nOpção 2 subtrair\nOpção 3 média\nOpção 4 finalizar: '))
    if opcao == 2:
        for i in range(0,2):
            valores.append(int(input(f"Valor {i} da subtração: ")))
        print(f'O resultado da subtração é: {valores[0] - valores[1]}')
        valores = []
        opcao = int(input('******opcoes******\nOpção 1 somar\nOpção 2 subtrair\nOpção 3 média\nOpção 4 finalizar: '))
    if opcao == 3:
        num = int(input("A média de quantos números?"))
        for i in range(0,num):
            valores.append(int(input(f"Valor {i} da média: ")))
        print(f'O resultado da média é: {sum(valores)/len(valores)}')
        valores = []
        opcao = int(input('******opcoes******\nOpção 1 somar\nOpção 2 subtrair\nOpção 3 média\nOpção 4 finalizar: '))
print('Você encerrou a aplicação')
    