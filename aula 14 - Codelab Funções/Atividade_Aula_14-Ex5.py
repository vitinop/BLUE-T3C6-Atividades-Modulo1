# 5. Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.
def calculo_imc(peso=0,altura=0):
    imc=peso/(altura*altura)
    return imc

imc=calculo_imc(75, 1.68)
print(f"{imc:.1f}")