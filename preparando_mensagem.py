def coletar_dados_fixos():
    print("Bem-vindo ao sistema de envio de mensagens!")
    print("Insira os dados fixos para o envio das mensagens.")

    # Máscara automática para data
    while True:
        data = input("Digite a data do exame (ex.: 120525 para 12/05/25): ").strip()
        if len(data) == 6 and data.isdigit():
            data_formatada = f"{data[:2]}/{data[2:4]}/{data[4:]}"
            break
        else:
            print("Formato inválido! Digite apenas números, ex: 120525 para 12/05/25.")

    # Máscara automática para dia da semana

        dias_semana = input("Digite o dia da semana do exame: ").strip().capitalize()
        dia_semana = dias_semana + "-feira" 

    while True:
        print("Escolha o tipo do exame:")
        print("1 - Ecocardiograma")
        print("2 - Teste Ergométrico")
        tipo_exame_opcao = input("Digite o número correspondente ao tipo do exame: ").strip()

        if tipo_exame_opcao == "1":
            tipo_exame = "Ecocardiograma"
            break
        elif tipo_exame_opcao == "2":
            tipo_exame = "Teste Ergométrico"
            break
        elif tipo_exame_opcao == "0":
            print("Dados coletados.")
            break
        else:
            print("Opção inválida. Escolha '1' para Ecocardiograma ou '2' para Teste Ergométrico.")

    return data_formatada, dia_semana, tipo_exame

# Chame a função assim:
if __name__ == "__main__":
    data, dia_semana, tipo_exame = coletar_dados_fixos()
    print(data, dia_semana, tipo_exame)