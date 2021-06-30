# 3. Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela. A média para aprovação é 7. 
# Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado.
import os
alunos = dict()
lista_alunos=list()
continuar=""
nome=""
nota=0
while True:
    
    nome= input("Insira o nome do aluno: ")
    nota= float(input("Insira a nota do aluno: "))
    if nota>=5 and nota<=6.9:
        alunos['Nome']= nome
        alunos['Nota'] = nota
        alunos['Situação']= "Recuperação"
        print ("O aluno está em recuperação")
    elif nota<5:
        alunos['Nome']= nome
        alunos['Nota'] = nota
        alunos['Situação']= "Reprovado"
        print ("O aluno foi  Reprovado")    
    elif nota >7:
        alunos['Nome']= nome
        alunos['Nota'] = nota
        alunos['Situação']= "Aprovado"
        print ("O aluno foi Aprovado")
      
    lista_alunos.append(alunos.copy())
    print(f"A situação atual do aluno é: {alunos}")
    print("A lista da situação de todos alunos é :")   
    for i in lista_alunos:
        print(f'{i}')
    continuar = str(input("Gostaria de encerrar o programa? [S/N]: ")).upper().strip()[0]
    if continuar == 'S':
        break
    elif continuar =='N':
        os.system('cls' if os.name == 'nt' else 'clear')