# def modelo_ultrassom(nome="", dia_semana="", data="", hora=""):
#     return f"""Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG. Gostaríamos de confirmar seu atendimento de {dia_semana} {data}
# NOME: {nome}

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

# Horário: {hora}

# OBSERVAÇÕES: SE JÁ REALIZOU ESSE EXAME, POR GENTILEZA, TRAZER CONSIGO NO DIA DO EXAME; SE HOUVER MAIS EXAMES AGENDADOS NO DIA DA CONFIRMAÇÃO E NÃO ESTÃO ESCRITOS, POR GENTILEZA NOS INFORMAR.
# Podemos confirmar? 
# Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos."""

def modelo_doppler(dia_semana="", data="", hora=""):
    return f"""Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG. Gostaríamos de confirmar seu atendimento de {dia_semana} {data}
Exame: DOPPLER COLORIDO ARTERIAL DE MEMBROS INFERIORES
Exame: DOPPLER COLORIDO VENOSO DE MEMBROS INFERIORES
Exame: DOPPLER CARÓTIDAS E VERTEBRAIS
Exame: DOPPLER AORTA ILÍACA 
PREPARO: DIA ANTERIOR - DIETA LEVE E TOMAR DE 50 GOTAS DE LUFTAL DE 8 EM 8 H / DIA DO EXAME - COMER TORRADAS COM CHÁ DEPOIS JEJUM TOTAL, PODE TOMAR ÁGUA E CONTINUAR TOMANDO LUFTAL.
HORÁRIO: {hora}
OBS: SE HOUVER MAIS EXAMES AGENDADOS E NÃO ESTÃO ESCRITOS NA MENSAGEM, POR GENTILEZA NOS INFORMAR.
Podemos confirmar? 
Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos."""

def modelo_ecocardiograma(dia_semana="", data="", hora=""):
    return f"""Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG. Gostaríamos de confirmar seu atendimento de {dia_semana} {data}
EXAME: ECOCARDIOGRAMA

PREPARO:  SEM PREPARO

OBS: SE HOUVER MAIS EXAMES AGENDADOS E NÃO ESTÃO ESCRITOS, POR GENTILEZA NOS INFORMAR.
Podemos confirmar? 
Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos.
HORÁRIO: {hora}"""

def modelo_teste_ergometrico(dia_semana="", data="", hora=""):
    return f"""Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG. Gostaríamos de confirmar seu atendimento de {dia_semana} {data}

EXAME: TESTE ERGOMÉTRICO 

PREPARO:  ROUPA DE ACADEMIA; NÃO PASSAR NENHUM CREME HIDRATANTE NO CORPO; NÃO REALIZAR NENHUM ESFORÇO FÍSICO ANTES DO EXAME (HOMEM: DEPILAR PELO DO TÓRAX ; MULHER: PRENDER O CABELO)

OBS: SE HOUVER MAIS EXAMES AGENDADOS E NÃO ESTÃO ESCRITOS, POR GENTILEZA NOS INFORMAR.
Podemos confirmar? 
Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos.
HORÁRIO: {hora}"""

def modelo_mapa(dia_semana="", data="", hora=""):
    return f"""Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG. Gostaríamos de confirmar seu atendimento de {dia_semana} {data}

EXAME: MAPA 24H

PREPARO:  SEM PREPARO

OBS: SE HOUVER MAIS EXAMES AGENDADOS E NÃO ESTÃO ESCRITOS, POR GENTILEZA NOS INFORMAR.
Podemos confirmar? 
Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos.
HORÁRIO: {hora}"""

def modelo_holter(dia_semana="", data="", hora=""):
    return f"""Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG. Gostaríamos de confirmar seu atendimento de {dia_semana} {data}

EXAME: HOLTER 24H

PREPARO:  SEM PREPARO

OBS: SE HOUVER MAIS EXAMES AGENDADOS E NÃO ESTÃO ESCRITOS, POR GENTILEZA NOS INFORMAR.
Podemos confirmar? 
Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos.
HORÁRIO: {hora}"""

def modelo_ecg_mamografia_rx():
    return """Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG.

Exame: ECG ou ELETROCARDIOGRAMA 
HORÁRIO: NÃO AGENDAMOS, O PACIENTE APENAS PRECISA DO PEDIDO MÉDICO, REALIZAMOS DE SEG - SEX, DAS 08:00 - 12:00 (MANHÃ) E DAS 14:00 - 17:00 (TARDE) 

Exame: RAIO-X / MAMOGRAFIA
HORÁRIO: NÃO AGENDAMOS, O PACIENTE APENAS PRECISA DO PEDIDO MÉDICO, REALIZAMOS DE SEG - SEX, DAS 08:00 - 12:00 (MANHÃ)

Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos."""

def modelo_confirmar_consulta(dia_semana="", data="", hora="", medico="", especialidade=""):
    return f"""Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG. Gostaríamos de confirmar seu atendimento de {dia_semana} {data}

CONSULTA: DR.(A) {medico} ({especialidade})

Podemos confirmar? 
Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos.
HORÁRIO: {hora}"""

def modelo_cancelar_exame(exame="", justificativa="", data="", dia_semana=""):
    return f"""Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG. Estamos entrando em contato para avisar que estamos cancelando seu atendimento de exame de {exame} (SOMENTE. SE HOUVER OUTROS ATENDIMENTOS, NÃO SERÃO DESMARCADOS), pois {justificativa}. Atendimento do dia {data}, {dia_semana}. Para remarcá-los, peço que ligue no número 32690020. Grato!"""

def modelo_cancelar_consulta(medico="", justificativa="", data="", dia_semana=""):
    return f"""Olá, tudo bem? Somos da Clínica Santos Medical Group - SMG. Estamos entrando em contato para avisar que estamos cancelando seu atendimento de consulta com o/a Dr.(a) {medico} (SOMENTE. SE HOUVER OUTROS ATENDIMENTOS, NÃO SERÃO DESMARCADOS), pois {justificativa}. Atendimento do dia {data}, {dia_semana}. Para remarcá-los, peço que ligue no número 32690020. Grato!"""

def modelo_reagendar_exame(exame="", justificativa="", data="", data_reagendada="", hora=""):
    return f"""Olá, tudo bem? Somos da clínica Santos Medical Group - SMG. Estamos entrando em contato para avisar que o seu exame {exame} do dia {data} reagendamos. Pois {justificativa}. Se caso não possuir disponibilidade para a data reagendada nos contatar (32690020) ou se conseguir pedimos que confirme por este canal. Grato!
DATA REAGENDADA: {data_reagendada}
HORÁRIO: {hora}
EXAME: {exame}"""

def modelo_reagendar_consulta(medico="", especialidade="", justificativa="", data="", data_reagendada="", hora=""):
    return f"""Olá, tudo bem? Somos da clínica Santos Medical Group - SMG. Estamos entrando em contato para avisar que o seu atendimento de consulta com DR.(A) {medico} do dia {data} reagendamos. Pois {justificativa}. Se caso não possuir disponibilidade para a data reagendada nos contatar (32690020) ou se conseguir pedimos que confirme por este canal. Grato!

DATA REAGENDADA: {data_reagendada}
HORÁRIO: {hora}
CONSULTA: {medico} ({especialidade})"""

def modelo_disponibilidade_exame(dia_semana="", data="", periodo="", exame=""):
    return f"""Olá, bom dia, somos a Santos Medical Group - SMG. Estamos entrando em contato para avisar que no dia {data}, {dia_semana} temos horários para o período {periodo}
Para o seguinte exame:

Exame: {exame}

Se houver interesse em antecipar, por favor nos avise por este canal ou ligue 32690020
Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos."""

def modelo_disponibilidade_consulta(dia_semana="", data="", periodo="", medico="", especialidade=""):
    return f"""Olá, bom dia, somos a Santos Medical Group - SMG. Estamos entrando em contato para avisar que no dia {data}, {dia_semana} temos horários para o período {periodo}
Para o seguinte consulta:

CONSULTA: {medico} ({especialidade})

Se houver interesse em antecipar, por favor nos avise por este canal ou ligue 32690020
Endereço: Avenida Rei Alberto I, Nº 243 - Ponta da praia, Santos."""