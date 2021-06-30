# 1.    Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. 
# Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
cadastro = dict()
cadastro['nome'] = input("Nome: ")
cadastro['ctps'] = int(input("Ctps: com 5 Dígitos: "))

#Laço para recebr as informações necessárias e impressão na tela dos dados digitados
if cadastro['tps'] !=0:
    cadastro['serie'] = int(input("Série com 03 Dígitos: "))
    cadastro['idade'] = (2021 - int(input("Ano de nascimento: ")))
    cadastro['anos_trabalhados'] = int((2021-int(input("Ano de contratação: "))))
    cadastro['salário'] = float(input("Último Salário: "))
    tempo = 35 - cadastro["anos_trabalhados"]
    print(f"""
   - Nome: {cadastro['nome']}, 
   - Idade {cadastro['idade']} anos, 
   - Ctps: {cadastro['ctps']}
   - Série: {cadastro['serie']}
   - Ultimo Salário: {cadastro['salário']}
   - Anos de Trabalho: {cadastro['anos_trabalhados']} """)

    # CALCULO DO TEMPO DE APOSENTADORIA DE ACORDO COM AS NOVAS REGRAS
    print('De acordo com as Novas Regras de Aposentadoria')
    print()

    if cadastro['anos_trabalhados'] >= 35:
        print("Você já está apto a se aposentar")
    elif 35 > cadastro['anos_trabalhados'] >= 33:
        print(f""" Você não está sujeito a regras de transição poderá se aposentar em: {35-cadastro['anos_trabalhados']} ano(s)""")
    elif  20 <= cadastro['anos_trabalhados'] < 33:
        print("Você está sujeito as novas regras de transições consulte o site do INSS ou entre em contato com 135")
    elif  cadastro['anos_trabalhados'] < 20:
        dt_futura = 65-cadastro['idade']
        print(f"""você se aposentará por idade daqui há : {65-cadastro['idade']} anos,  em {dt_futura + 2021}. """)