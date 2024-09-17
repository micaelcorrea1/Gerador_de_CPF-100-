import random  # Módulo para gerar números aleatórios

n_cpf = 0
for cpfs in range(100):  # Gera 100 CPFs
    cpf = ''
    for _ in range(9):  # Gera os 9 primeiros dígitos aleatórios do CPF
        cpf += str(random.randint(0, 9))

    cpf_1 = cpf[0:9]  # Pega os 9 primeiros dígitos
    
    # Cálculo do primeiro dígito verificador
    contador_regressivo_1 = 10
    resultado_1 = 0
    for numero_1 in cpf_1:
        resultado_1 += int(numero_1) * contador_regressivo_1
        contador_regressivo_1 -= 1

    # Se o resto for >= 10, o dígito verificador é 0
    resultado_1_mult_por_10 = resultado_1 * 10
    resto_resultado_1 = resultado_1_mult_por_10 % 11
    primeiro_digito = 0 if resto_resultado_1 >= 10 else resto_resultado_1

    # Cálculo do segundo dígito verificador
    cpf_2 = cpf_1 + str(primeiro_digito)  # Adiciona o primeiro dígito verificador
    contador_regressivo_2 = 11
    resultado_2 = 0
    for numero_2 in cpf_2:
        resultado_2 += int(numero_2) * contador_regressivo_2
        contador_regressivo_2 -= 1

    # Se o resto for >= 10, o segundo dígito verificador é 0
    resultado_2_mult_por_10 = resultado_2 * 10
    resto_resultado_2 = resultado_2_mult_por_10 % 11
    segundo_digito = 0 if resto_resultado_2 >= 10 else resto_resultado_2

    # Formatação do CPF final no formato XXX.XXX.XXX-XX
    cpf_gerado_pelo_calculo = f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{primeiro_digito}{segundo_digito}'

    n_cpf += 1
    print(f'{n_cpf}. CPF: {cpf_gerado_pelo_calculo}')  # Exibe o CPF gerado

