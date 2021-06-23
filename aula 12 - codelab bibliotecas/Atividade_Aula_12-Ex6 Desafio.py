# 6. Desafio: Continuando o exercício 3 crie agora um boletim escolar, seu programa deve
# receber 5 notas de 15 alunos, assim como o nome desses alunos, 
# o programa tem que calcular a média desse aluno e mostrar a situação dele, 
# seguindo os mesmos critérios apresentados no exercício 3. No final apresente todos nomes, 
# as 5 notas, as médias e as situações dos 15 alunos de uma vez só.
import os
alunos = dict()
lista_alunos=list()
continuar=""
nome=""
media_total=0
notas=list()
for i in range(0,15):
    nome= input("Insira o nome do aluno: ")
    for j in range (1,6):
        nota= float(input(f"""Insira a nota do aluno no {j}º bimestre: """)) #considerando o valor bimestral valendo 100 pontos
        notas.append(nota)
        media_total=(media_total+nota)  
    media_total=(media_total)/5
    alunos['Nome']= nome
    alunos['Nota']= notas
    alunos['Média'] = media_total
    if media_total>=50 and media_total<=69.5:
        alunos['Situação']= "Recuperação"
        print ("O aluno está em recuperação")
    elif media_total<50:
        alunos['Situação']= "Reprovado"
        print ("O aluno foi  Reprovado")    
    elif media_total>69.5:     
        alunos['Situação']= "Aprovado"
        print ("O aluno foi Aprovado")
      
    lista_alunos.append(alunos.copy())
    print(f"A situação atual do aluno é: {alunos}")
    print("A lista da situação de todos alunos é :")   
    
    continuar = str(input("Gostaria de encerrar o programa? [S/N]: ")).upper().strip()[0]
    if continuar == 'S':
        break
    elif continuar =='N':
        os.system('cls' if os.name == 'nt' else 'clear')