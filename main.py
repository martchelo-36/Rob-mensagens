from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import os

# Caminho para o Edge WebDriver (certifique-se de que o msedgedriver.exe está na pasta correta)
edgedriver_path = os.path.join(os.getcwd(), 'msedgedriver.exe')  # Substitua pelo nome correto do executável
service = Service(edgedriver_path)
navegador = webdriver.Edge(service=service)

# Lendo o arquivo Excel da mesma pasta do código
excel_path = os.path.join(os.getcwd(), 'Contatos.xlsx')
contatos = pd.read_excel(excel_path)

# Acessando o WhatsApp Web
navegador.get('https://web.whatsapp.com/')
input("Escaneie o QR Code no WhatsApp Web e pressione Enter para continuar...")

# Enviando mensagens para cada contato
for i, contato in contatos.iterrows():
    nome = contato['Nome']  # Coluna "Nome" no Excel
    numero = contato['Número']  # Coluna "Número" no Excel
    mensagem = contato['Mensagem']  # Coluna "Mensagem" no Excel

    # Acessando o chat do contato pelo link do WhatsApp
    link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
    navegador.get(link)
    time.sleep(10)  # Aguarde o carregamento do chat

    # Enviar a mensagem
    try:
        enviar = navegador.find_element("xpath", '//div[@title="Enviar"]')
        enviar.click()
        time.sleep(5)  # Aguarde o envio da mensagem
    except Exception as e:
        print(f"Erro ao enviar mensagem para {nome}: {e}")

print("Mensagens enviadas com sucesso!")
navegador.quit()