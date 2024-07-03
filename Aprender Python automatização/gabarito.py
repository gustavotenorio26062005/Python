# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time
import pyperclip
from datetime import datetime

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(3)  # Aguarde alguns segundos para o Chrome abrir
pyautogui.moveTo(x=649, y=76)
pyautogui.click()
# entrar no link 
# Copia o link para a área de transferência
link = "https://capricornio.systextil.com.br/systextil/forms.systextil.senha"
pyperclip.copy(link)

# Cole o conteúdo da área de transferência
pyautogui.hotkey("ctrl", "v")

pyautogui.press("enter")

time.sleep(3)


# Passo 2: Fazer login
pyautogui.moveTo(x=855, y=308)
pyautogui.click()

pyautogui.press("0")
pyautogui.press("enter")
pyautogui.press("Tab")
usuario = "gustavo.bt"
senha = "Capri123"
pyautogui.write(usuario)
pyautogui.press("enter")
pyautogui.write(senha)
pyautogui.press("enter")

pyautogui.moveTo(x=1284, y=106)
pyautogui.click()

aba = "PCPB_F049"
pyautogui.write(aba)
pyautogui.press("enter")
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_excel("produtos.xlsx")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.press("tab")
    # pegar da tabela o valor do campo que a gente quer preencher
    time.sleep(1)
    codigo = tabela.loc[linha, "Op"]
        # preencher o campo
    pyautogui.write(str(codigo))
    time.sleep(1)
    pyautogui.press("tab")
    #estágio
    pyautogui.write("45")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("enter")
    #depósito
    pyautogui.write("360")
    time.sleep(1)
    pyautogui.press("enter")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "Turno"]))
    time.sleep(1)
    pyautogui.press("tab")
    data = tabela.loc[linha, "Data"]
    formatted_data = datetime.strftime(data, "%d/%m/%Y")

    pyautogui.write(formatted_data)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.write("2")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.write("APA01")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.write("999")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.write("000001")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.write(str(tabela.loc[linha, "Apara"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "Motivo"]))
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "Kgmotivo"]))
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.moveTo(x=112, y=106)
    time.sleep(1)
    pyautogui.click
    time.sleep(1)
    pyautogui.moveTo(x=1284, y=106)
    time.sleep(1)
    pyautogui.doubleClick
    pyautogui.write(aba)
    pyautogui.press("enter")
    time.sleep(3)
    # Passo 5: Repetir o processo de cadastro até o fim
pyautogui.hotkey("alt","f4")