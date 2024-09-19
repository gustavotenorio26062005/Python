'''Elaborar um program que informe qual é o mês por extenso, de acordo com a sequencia de 1 a 12, sendo 1, o mês de janeiro e 12, o mÊs de dezembro. Solicitar a entrada da sequência'''
'''Exibir quantos dias tem o mês informado'''
'''E indicar se o ano é bissexto. Solicitar entrada do ano'''
'''Se o resto da divisão do ano por 400 for 0 ou se o resto da divisão por 4 for 0 e se o resto da divisão por 100 != de 0'''
'''Exibir que feveireiro tem 29 dias'''
'''Se não exibir que fevereiro tem 28 dias'''

mes = int(input("Informe o número do mês: "))

while mes > 12 or mes < 1:
    mes = int(input("Informe um número correto de um mês: "))

if mes == 1: 
    print("Janeiro\nTem 31 dias")
elif mes == 2:
    print("Feveireiro")
    ano = int(input("Digite o ano: "))
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        print("O ano é bissexto então o mês de feveireiro tem 29 dias")
    else:
        print("O ano não é bissexto então o mês de feveireiro tem 28 dias")

elif mes == 3:
    print("Março\nTem 31 dias")
elif mes == 4:
    print("Abril\nTem 30 dias")
elif mes == 5:
    print("Maio\nTem 31 dias")
elif mes == 6:
    print("Junho\nTem 30 dias")
elif mes == 7:
    print("Julho\nTem 31 dias")
elif mes == 8:
    print("Agosto\nTem 31 dias")
elif mes == 9:
    print("Setembro\nTem 30 dias")
elif mes == 10:
    print("Outubro\nTem 31 dias")
elif mes == 11:
    print("Novembro\nTem 30 dias")
elif mes == 12:
    print("Dezembro\nTem 31 dias")