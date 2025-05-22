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










# MODELOS DE MENSAGENS





# MODELO DE MENSAGENS 

# ------------------------------------------------------
# ULTRASSOM 

# Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG. Gostaríamos de confirmar seu atendimento de -feira  //20
# NOME: 

# Exame: US ABDOME TOTAL
# PREPARO: 6 HORAS DE JEJUM; TOMAR DE 60 A 80 GOTAS DE LUFTAL 1 HORA ANTES DO EXAME; BEBER DE 4/5 COPOS DE ÁGUA, ESTAR COM A BEXIGA CHEIA.

# Exame: US APARELHO URINÁRIO / US PRÓSTATA / US PELVICO 
# PREPARO: BEBER DE 4/5 COPOS DE ÁGUA, ESTAR COM A BEXIGA CHEIA.

# Exame: US TIREÓIDE COM DOPPLER / US MAMAS (SE FEITO MAMOGRAFIA TRAZER, POR GENTILEZA) / US AXILAS / US TRANSVAGINAL / US ARTICULAR (QUADRIL, JOELHO, OMBRO, ETC) / US MÚSCULO ESQUELÉTICO / US PAREDE ABDOMINAL / US OBSTÉTRICO / US OBSTÉTRICO MORFOLÓGICO ( SOMENTE NO PARTICULAR 
# PREPARO:  SEM PREPARO

# Exame: US ABDOME SUPERIOR
# PREPARO: 8 HORAS DE JEJUM

# Exame: US PARTES MOLES
# PREPARO: ALIMENTAÇÃO LEVE E HIDRATAÇÃO

# Horário:

# OBSERVAÇÕES: SE JÁ REALIZOU ESSE EXAME, POR GENTILEZA, TRAZER CONSIGO NO DIA DO EXAME; SE HOUVER MAIS EXAMES AGENDADOS NO DIA DA CONFIRMAÇÃO E NÃO ESTÃO ESCRITOS, POR GENTILEZA NOS INFORMAR.
# Podemos confirmar? 
# Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos.

# ------------------------------------------------------
# DOPPLER 

# Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG. Gostaríamos de confirmar seu atendimento de -feira //2025
# Exame: DOPPLER COLORIDO ARTERIAL DE MEMBROS INFERIORES
# Exame: DOPPLER COLORIDO VENOSO DE MEMBROS INFERIORES
# Exame: DOPPLER CARÓTIDAS E VERTEBRAIS
# Exame: DOPPLER AORTA ILÍACA 
# PREPARO: DIA ANTERIOR - DIETA LEVE E TOMAR DE 50 GOTAS DE LUFTAL DE 8 EM 8 H / DIA DO EXAME - COMER TORRADAS COM CHÁ DEPOIS JEJUM TOTAL, PODE TOMAR ÁGUA E CONTINUAR TOMANDO LUFTAL.
# HORÁRIO: 
# OBS: SE HOUVER MAIS EXAMES AGENDADOS E NÃO ESTÃO ESCRITOS NA MENSAGEM, POR GENTILEZA NOS INFORMAR.
# Podemos confirmar? 
# Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos.

# ------------------------------------------------------
# ECOCARDIOGRAMA 

# Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG. Gostaríamos de confirmar seu atendimento de -feira //20
# EXAME: ECOCARDIOGRAMA

# PREPARO:  SEM PREPARO

# OBS: SE HOUVER MAIS EXAMES AGENDADOS E NÃO ESTÃO ESCRITOS, POR GENTILEZA NOS INFORMAR.
# Podemos confirmar? 
# Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos.
# HORÁRIO: 
# ------------------------------------------------------
# TESTE ERGOMÉTRICO

# Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG. Gostaríamos de confirmar seu atendimento de -feira  //20

# EXAME: TESTE ERGOMÉTRICO 

# PREPARO:  ROUPA DE ACADEMIA; NÃO PASSAR NENHUM CREME HIDRATANTE NO CORPO; NÃO REALIZAR NENHUM ESFORÇO FÍSICO ANTES DO EXAME (HOMEM: DEPILAR PELO DO TÓRAX ; MULHER: PRENDER O CABELO)

# OBS: SE HOUVER MAIS EXAMES AGENDADOS E NÃO ESTÃO ESCRITOS, POR GENTILEZA NOS INFORMAR.
# Podemos confirmar? 
# Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos.
# HORÁRIO: 
# ------------------------------------------------------
# MAPA 

# Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG. Gostaríamos de confirmar seu atendimento de -feira //20

# EXAME: MAPA 24H

# PREPARO:  SEM PREPARO


# OBS: SE HOUVER MAIS EXAMES AGENDADOS E NÃO ESTÃO ESCRITOS, POR GENTILEZA NOS INFORMAR.
# Podemos confirmar? 
# Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos.
# HORÁRIO: 
# ------------------------------------------------------
# HOLTER 

# Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG. Gostaríamos de confirmar seu atendimento de -feira //20

# EXAME: HOLTER 24H

# PREPARO:  SEM PREPARO

# OBS: SE HOUVER MAIS EXAMES AGENDADOS E NÃO ESTÃO ESCRITOS, POR GENTILEZA NOS INFORMAR.
# Podemos confirmar? 
# Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos.
# HORÁRIO: 
# ------------------------------------------------------
# ECG, MAMOGRAFIA E RX

# Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG.

# Exame: ECG ou ELETROCARDIOGRAMA 
# HORÁRIO: NÃO AGENDAMOS, O PACIENTE APENAS PRECISA DO PEDIDO MÉDICO, REALIZAMOS DE SEG - SEX, DAS 08:00 - 12:00 (MANHÃ) E DAS 14:00 - 17:00 (TARDE) 

# Exame: RAIO-X / MAMOGRAFIA
# HORÁRIO: NÃO AGENDAMOS, O PACIENTE APENAS PRECISA DO PEDIDO MÉDICO, REALIZAMOS DE SEG - SEX, DAS 08:00 - 12:00 (MANHÃ)

# Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos.

# ------------------------------------------------------
# CONFIRMAR CONSULTA
# Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG. Gostaríamos de confirmar seu atendimento de -feira  //20

# CONSULTA: DR.(A) NOME (ESPECIALIDADE)

# Podemos confirmar? 
# Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos.
# HORÁRIO: 
# ------------------------------------------------------
# CANCELAR EXAME

# Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG. Estamos entrando em contato para avisar que estamos cancelando seu atendimento de exame de EXAME (SOMENTE. SE HOUVER OUTROS ATENDIMENTOS, NÃO SERÃO DESMARCADOS), pois (JUSTIFICATIVA) . Atendimento do dia //20, -feira. Para remarcá-los, peço que ligue no número 32690020. Grato!

# ------------------------------------------------------
# CANCELAR CONSULTA

# Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG. Estamos entrando em contato para avisar que estamos cancelando seu atendimento de consulta com o/a (Dr.(a) NOME DO MÉDICO)  (SOMENTE. SE HOUVER OUTROS ATENDIMENTOS, NÃO SERÃO DESMARCADOS), pois (JUSTIFICATIVA) . Atendimento do dia //20, -feira. Para remarcá-los, peço que ligue no número 32690020. Grato!

# ------------------------------------------------------
# REAGENDAR EXAME

# Olá, tudo bem? Somos da clínica Santos Medical Group - SMG. Estamos entrando em contato para avisar que o seu exame EXAME do dia //20 reagendamos. Pois (JUSTIFICATIVA) . Se caso não possuir disponibilidade para a data reagendada nos contatar (32690020) ou se conseguir pedimos que confirme por este canal. Grato!
# DATA REAGENDADA:
# HORÁRIO:
# EXAME:

# ------------------------------------------------------
# REAGENDAR CONSULTA

# Olá, tudo bem? Somos da clínica Santos Medical Group - SMG. Estamos entrando em contato para avisar que o seu atendimento de consulta com (DR.(A). NOME DO MÉDICO) do dia //20 reagendamos. Pois (JUSTIFICATIVA) . Se caso não possuir disponibilidade para a data reagendada nos contatar (32690020) ou se conseguir pedimos que confirme por este canal. Grato!

# DATA REAGENDADA:

# HORÁRIO:

# CONSULTA: (NOME DO MÉDICO) (ESPECIALIDADE)

# ------------------------------------------------------
# DISPONIBILIDADE EXAME

# Olá, bom dia, somos a Santos Medical Group - SMG. Estamos entrando em contato para avisar que no dia //, -feira temos horários para o período (MANHÃ / TARDE)
# Para o seguinte exame:

# Exame: 

# Se houver interesse em antecipar, por favor nos avise por este canal ou ligue 32690020
# Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos.

# ------------------------------------------------------
# DISPONIBILIDADE CONSULTA

# Olá, bom dia, somos a Santos Medical Group - SMG. Estamos entrando em contato para avisar que no dia //, -feira temos horários para o período (MANHÃ / TARDE)
# Para o seguinte consulta:

# CONSULTA: (NOME DO MÉDICO) (ESPECIALIDADE)

# Se houver interesse em antecipar, por favor nos avise por este canal ou ligue 32690020
# Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos.





