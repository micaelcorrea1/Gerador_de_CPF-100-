import random

n_cpf = 0
for cpfs in range(100):
    cpf = ''
    for _ in range(9):
        cpf += str(random.randint(0, 9))

    cpf_1 = cpf[0:9]
    contador_regressivo_1 = 10
    resultado_1 = 0
    for numero_1 in cpf_1:
        resultado_1 += int(numero_1) * contador_regressivo_1
        contador_regressivo_1 -= 1

    resultado_1_mult_por_10 = resultado_1 * 10
    resto_resultado_1 = resultado_1_mult_por_10 % 11
    primeiro_digito = 0 if resto_resultado_1 >= 10 else resto_resultado_1


    cpf_2 = cpf_1 + str(primeiro_digito)
    contador_regressivo_2 = 11
    resultado_2 = 0
    for numero_2 in cpf_2:
        resultado_2 += int(numero_2) * contador_regressivo_2
        contador_regressivo_2 -= 1

    resultado_2_mult_por_10 = resultado_2 * 10
    resto_resultado_2 = resultado_2_mult_por_10 % 11
    segundo_digito = 0 if resto_resultado_2 >= 10 else resto_resultado_2

    cpf_gerado_pelo_calculo = f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{primeiro_digito}{segundo_digito}'

    n_cpf += 1
    print(f'{n_cpf}. CPF: {cpf_gerado_pelo_calculo}')
