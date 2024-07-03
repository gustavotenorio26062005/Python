import pyautogui
from playwright.sync_api import sync_playwright
import time
import pyperclip

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(3)  # Aguarde alguns segundos para o Chrome abrir

pyautogui.moveTo(x=649, y=76)
pyautogui.click()

link = "https://capricornio.systextil.com.br/systextil/forms.systextil.senha"

# Copia o link para a área de transferência
pyperclip.copy(link)

# Cole o conteúdo da área de transferência
pyautogui.hotkey("ctrl", "v")

pyautogui.press("enter")

#Login
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

#importar tabela
import pandas

tabela_origem = pandas.read_csv("C:/Users/gusta/Desktop/Vs studio code/Teste - Copia.csv")
print(tabela_origem)

for linha in tabela_origem.index:
    pyautogui.press("tab")
    codigo = tabela_origem.loc[linha, "op"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write("45")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.write("360")
    pyautogui.press("tab")
    Turno = tabela_origem.loc[linha,"Turno"]
    pyautogui.write(Turno)
    pyautogui.press("tab")
    Turno = tabela_origem.loc[linha,"Data"]
    pyautogui.write("26/06/2023")
    pyautogui.press("enter")
    pyautogui.write("2")
    pyautogui.press("tab")
    pyautogui.write("apa01")
    pyautogui.press("tab")
    pyautogui.write("999")
    pyautogui.press("tab")
    pyautogui.write("000001")
    pyautogui.press("tab")
    pyautogui.write("0")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.write("enter")
    #defeitos
    pyautogui.press("tab")
    pyautogui.write("855")
    pyautogui.press("tab")
    pyautogui.write(str("0,0"))
    pyautogui.press("F9")
    pyautogui.moveTo(x=1284, y=106)
    pyautogui.click()

    pyautogui.write(aba)
    pyautogui.press("enter")
    