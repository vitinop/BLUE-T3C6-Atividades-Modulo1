# 4. Faça um programa que calcule o salário de um colaborador na empresa XYZ. 
# O salário é pago conforme a quantidade de horas trabalhadas.
# Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas. 
# SUposição de valor hora  R$ 8,33
def salarioColaborador(horas=0,horasextras=0):
    horas = int (input("Informe o numero de horas trabalhadas " ))
    if horas> 40:
        horasextras=horas-40
        horas=horas-horasextras
    salario=(horas*8.33)+(horasextras*8.33*1.5)
    return salario
salario=salarioColaborador()
print(f"{salario:.2f}")