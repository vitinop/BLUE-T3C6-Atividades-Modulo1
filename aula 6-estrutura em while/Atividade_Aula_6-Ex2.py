sex=str(input("Digite F para feminino e M para masculino: "))
sex=sex.upper()
while sex not in ("MF"):
    sex=(input("Sexo Biológico Inválido. Digite F para feminino e M para masculino: ")).upper()  
if sex=="M":
  print("O sexo biológico é Masculino")
elif sex=="F":
  print("O sexo biológico é feminino.")
