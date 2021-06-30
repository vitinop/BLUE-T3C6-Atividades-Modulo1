#02 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
entrada = tuple()
quantidade = 0
primeiro = 0


for i in range(4):
    valor = int(input(f"Digite o {i+1}º valor: "))
    entrada = entrada + tuple([valor])

print(entrada)
quantidade = entrada.count(9)
primeiro = entrada.index(3)
print(f"""o 9 apareceu {quantidade} 
vezes, e o primeiro 3 digitado encontra-se na posição {primeiro}
""")
