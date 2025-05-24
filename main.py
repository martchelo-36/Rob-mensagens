import modelos

# Coleta dos dados fixos
while True:
    data = input("Digite a data do exame (ex.: 120525 para 12/05/25): ").strip()
    if len(data) == 6 and data.isdigit():
        data_formatada = f"{data[:2]}/{data[2:4]}/{data[4:]}"
        break
    else:
        print("Formato inválido! Digite apenas números, ex: 120525 para 12/05/25.")

while True:
    dia_semana = input("Digite o dia da semana do exame (ex.: Segunda, Terca, Sabado, Domingo): ").strip().capitalize()
    if dia_semana in ["Sabado", "Sábado"]:
        dia_semana_formatado = "Sábado"
        break
    elif dia_semana == "Domingo":
        dia_semana_formatado = "Domingo"
        break
    else:
        dia_semana_formatado = dia_semana + "-feira"
        break

# Menu para escolher o modelo de mensagem
print("\nEscolha o modelo de mensagem:")
print("1 - Ecocardiograma")
print("2 - Teste Ergométrico")
print("3 - Doppler")
print("4 - MAPA")
print("5 - Holter")
print("6 - ECG/Mamografia/RX")
print("7 - Confirmar Consulta")
print("8 - Cancelar Exame")
print("9 - Cancelar Consulta")
print("10 - Reagendar Exame")
print("11 - Reagendar Consulta")
print("12 - Disponibilidade Exame")
print("13 - Disponibilidade Consulta")
modelo_opcao = input("Digite o número do modelo desejado: ").strip()

# Seleção do modelo
if modelo_opcao == "1":
    modelo = modelos.modelo_ecocardiograma
elif modelo_opcao == "2":
    modelo = modelos.modelo_teste_ergometrico
elif modelo_opcao == "3":
    modelo = modelos.modelo_doppler
elif modelo_opcao == "4":
    modelo = modelos.modelo_mapa
elif modelo_opcao == "5":
    modelo = modelos.modelo_holter
elif modelo_opcao == "6":
    modelo = modelos.modelo_ecg_mamografia_rx
elif modelo_opcao == "7":
    modelo = modelos.modelo_confirmar_consulta
elif modelo_opcao == "8":
    modelo = modelos.modelo_cancelar_exame
elif modelo_opcao == "9":
    modelo = modelos.modelo_cancelar_consulta
elif modelo_opcao == "10":
    modelo = modelos.modelo_reagendar_exame
elif modelo_opcao == "11":
    modelo = modelos.modelo_reagendar_consulta
elif modelo_opcao == "12":
    modelo = modelos.modelo_disponibilidade_exame
elif modelo_opcao == "13":
    modelo = modelos.modelo_disponibilidade_consulta
else:
    print("Opção inválida! Saindo do programa.")
    exit()

# Coleta dos contatos
contatos = []
while True:
    numero = input("Digite o número do contato (apenas números, com DDD, ex.: 13999999999, ou 0 para sair): ").strip()
    if numero == '0':
        break
    if numero.startswith('+'):
        numero = numero[1:]
    if not numero.startswith('55'):
        numero = '55' + numero

    # Para modelos que precisam de hora
    if modelo_opcao in ["1", "2", "3", "4", "5", "7", "10", "11"]:
        while True:
            hora = input("Digite a hora do exame (ex.: 1430 para 14:30): ").strip()
            if len(hora) == 4 and hora.isdigit():
                hora_formatada = f"{hora[:2]}:{hora[2:]}"
                break
            else:
                print("Formato inválido! Digite apenas números, ex: 1430 para 14:30.")
    else:
        hora_formatada = ""

    contatos.append({"Numero": numero, "Hora": hora_formatada})

# Geração e exibição das mensagens
for contato in contatos:
    # Modelos simples
    if modelo_opcao in ["1", "2", "3", "4", "5"]:
        mensagem = modelo(dia_semana=dia_semana_formatado, data=data_formatada, hora=contato['Hora'])
    elif modelo_opcao == "6":
        mensagem = modelo()
    elif modelo_opcao == "7":
        medico = input("Nome do médico: ")
        especialidade = input("Especialidade: ")
        mensagem = modelo(dia_semana=dia_semana_formatado, data=data_formatada, hora=contato['Hora'], medico=medico, especialidade=especialidade)
    elif modelo_opcao == "8":
        exame = input("Nome do exame: ")
        justificativa = input("Justificativa do cancelamento: ")
        mensagem = modelo(exame=exame, justificativa=justificativa, data=data_formatada, dia_semana=dia_semana_formatado)
    elif modelo_opcao == "9":
        medico = input("Nome do médico: ")
        justificativa = input("Justificativa do cancelamento: ")
        mensagem = modelo(medico=medico, justificativa=justificativa, data=data_formatada, dia_semana=dia_semana_formatado)
    elif modelo_opcao == "10":
        exame = input("Nome do exame: ")
        justificativa = input("Justificativa do reagendamento: ")
        data_reagendada = input("Data reagendada (ex.: 120525 para 12/05/25): ")
        if len(data_reagendada) == 6 and data_reagendada.isdigit():
            data_reagendada = f"{data_reagendada[:2]}/{data_reagendada[2:4]}/{data_reagendada[4:]}"
        mensagem = modelo(exame=exame, justificativa=justificativa, data=data_formatada, data_reagendada=data_reagendada, hora=contato['Hora'])
    elif modelo_opcao == "11":
        medico = input("Nome do médico: ")
        especialidade = input("Especialidade: ")
        justificativa = input("Justificativa do reagendamento: ")
        data_reagendada = input("Data reagendada (ex.: 120525 para 12/05/25): ")
        if len(data_reagendada) == 6 and data_reagendada.isdigit():
            data_reagendada = f"{data_reagendada[:2]}/{data_reagendada[2:4]}/{data_reagendada[4:]}"
        mensagem = modelo(medico=medico, especialidade=especialidade, justificativa=justificativa, data=data_formatada, data_reagendada=data_reagendada, hora=contato['Hora'])
    elif modelo_opcao == "12":
        periodo = input("Período (MANHÃ/TARDE): ")
        exame = input("Nome do exame: ")
        mensagem = modelo(dia_semana=dia_semana_formatado, data=data_formatada, periodo=periodo, exame=exame)
    elif modelo_opcao == "13":
        periodo = input("Período (MANHÃ/TARDE): ")
        medico = input("Nome do médico: ")
        especialidade = input("Especialidade: ")
        mensagem = modelo(dia_semana=dia_semana_formatado, data=data_formatada, periodo=periodo, medico=medico, especialidade=especialidade)
    else:
        mensagem = "Modelo não implementado."

    print("\nMensagem gerada:")
    print(mensagem)
    # Aqui você pode colocar o código para enviar a mensagem pelo WhatsApp




