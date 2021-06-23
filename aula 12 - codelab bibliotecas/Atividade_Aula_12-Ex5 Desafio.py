# 5. DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, 
# e que quando perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.
import os
dicionario= dict()
media_idade=0
lista_todos=list()
lista_todas_mulheres=list()
nota=0
lista_idade_todos= list()
while True:
    dicionario['Nome']= (input("Insira o nome: "))
    dicionario['Idade'] =int(input("Informe a idade: "))
    lista_idade_todos.append(dicionario['Idade'])
    sexBio=(input("Olá, informe o sexo biologico da pessoa, digite F para feminino e M para masculino: ")).upper().strip()[0]
    while sexBio not in ["F","M"]:
        sexBio=(input("""
        Sexo biológico inválido! Tente novamente. 
        Digite F para feminino e M para masculino: """)).upper().strip()[0]
    if sexBio =="F":
        lista_todas_mulheres.append(dicionario)
        dicionario['Sexo Biológico']="Feminino"
    elif sexBio =="M":
        dicionario['Sexo Biológico']="Masculino"
    lista_todos.append(dicionario.copy())
    media_idade=(sum(lista_idade_todos)/len(lista_todos))
    print(f"""
    O número de usuários cadastrados é                          : {len(lista_todos)}
    
    A média de idade Geral é                                    : {media_idade:.2f}

    A lista de todos usuários cadastrados do sexo feminino é    :{(lista_todas_mulheres)}

    A lista de todos usuários cadastrados é                     :{(lista_todos)}""")
    print(dicionario)
    
    
    
    continuar = str(input("Gostaria de encerrar o programa? [S/N]: ")).upper().strip()[0]
    if continuar == 'S':
        break
    elif continuar =='N':
        os.system('cls' if os.name == 'nt' else 'clear')