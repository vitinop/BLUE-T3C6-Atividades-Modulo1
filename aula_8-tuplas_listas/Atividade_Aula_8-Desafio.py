# Desafio da noite:
# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

contadordeculpa=0
lista=[1,2,3,4,5]
for lista in range(0,6):
    if lista==1:
        print("Você telefonou para a vítima?")
        resposta=str (input("Responda S para sim e N para não: "))
        resposta=resposta.capitalize().strip()
        if resposta == "S":
            contadordeculpa=contadordeculpa+1
    elif lista==2: 
        print("Você esteve no local do crime?")
        resposta=str (input("Responda S para sim e N para não: "))
        resposta=resposta.capitalize().strip()
        if resposta == "S":
            contadordeculpa=contadordeculpa+1 
    elif lista==3:
        print("Você mora perto da vítima?")
        resposta=str (input("Responda S para sim e N para não: "))
        resposta=resposta.capitalize().strip()
        if resposta == "S":
            contadordeculpa=contadordeculpa+1 
    elif lista==4:
        print("Você devia para a vítima?")
        resposta=str (input("Responda S para sim e N para não: "))
        resposta=resposta.capitalize().strip()
        if resposta == "S":
            contadordeculpa=contadordeculpa+1 
    elif lista==5:
        print("Você já trabalhou com a vítima?")
        resposta=str (input("Responda S para sim e N para não: "))
        resposta=resposta.capitalize().strip()
        if resposta == "S":
            contadordeculpa=contadordeculpa+1 
  
if contadordeculpa <= 1:
  print("O individuo é inocente")
elif contadordeculpa == 2:
  print("O individuo é suspeito")
elif contadordeculpa == 3 or contadordeculpa == 4 :
  print("O individuo é cúmplice")
elif contadordeculpa == 5:
   print("O individuo é culpado")