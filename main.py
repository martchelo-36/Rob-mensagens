from preparando_mensagem import coletar_dados_fixos
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
import time

# Coleta os dados fixos do usuário
data, dia_semana, tipo_exame = coletar_dados_fixos()

# Aqui você pode coletar os contatos e horários (exemplo simples)
contatos = []
while True:
    numero = input("Digite o número do contato (apenas números, com DDD, ex.: 13999999999, ou 0 para sair): ").strip()
    if numero == '0':
        break
    if numero.startswith('+'):
        numero = numero[1:]
    if not numero.startswith('55'):
        numero = '55' + numero
    hora = input("Digite a hora do exame (ex.: 1430 para 14:30): ").strip()
    if len(hora) == 4 and hora.isdigit():
        hora_formatada = f"{hora[:2]}:{hora[2:]}"
    else:
        hora_formatada = hora
    contatos.append({"Numero": numero, "Hora": hora_formatada})

# Abrindo o navegador
navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com/')
input("Escaneie o QR Code no WhatsApp Web e pressione Enter para continuar...")

# Enviando mensagens
for contato in contatos:
    mensagem = (
        f"Olá! Estamos entrando em contato para confirmar o seu exame de {tipo_exame}.\n"
        f"Data: {data} ({dia_semana})\n"
        f"Hora: {contato['Hora']}\n"
        "Por favor, entre em contato caso tenha dúvidas. Obrigado!"
    )
    mensagem_codificada = quote(mensagem)
    link = f"https://web.whatsapp.com/send?phone={contato['Numero']}&text={mensagem_codificada}"
    navegador.get(link)
    try:
        enviar = WebDriverWait(navegador, 40).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="compose-btn-send"]'))
        )
        enviar.click()
        time.sleep(3)
        print(f"Mensagem enviada para {contato['Numero']} com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar mensagem para {contato['Numero']}: {e}")

print("Mensagens enviadas com sucesso!")
navegador.quit()