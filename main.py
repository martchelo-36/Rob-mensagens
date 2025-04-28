from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import pandas as pd
import time
import os

# Abrindo zapzap
navegador = webdriver.Chrome()

# Lendo o arquivo Excel (já já essa porra vai ter q virar pdf)
excel_path = os.path.join(os.getcwd(), 'Contatos.xlsx')
contatos = pd.read_excel(excel_path)


navegador.get('https://web.whatsapp.com/')
input("Escaneie o QR Code no WhatsApp Web e pressione Enter para continuar...")

# Enviando mensagens
for i, contato in contatos.iterrows():
    nome = contato['Nome']  
    numero = str(contato['Número']).strip()  
    mensagem = contato['Mensagem']  

    # Codificar a mensagem para a URL
    mensagem_codificada = quote(mensagem)
    link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem_codificada}"
    navegador.get(link)
    time.sleep(10)  

    try:
        enviar = navegador.find_element("xpath", '//div[@title="Enviar"]')
        enviar.click()
        time.sleep(5)  
    except Exception as e:
        print(f"Erro ao enviar mensagem para {nome}: {e}")

print("Mensagens enviadas com sucesso!")
navegador.quit()