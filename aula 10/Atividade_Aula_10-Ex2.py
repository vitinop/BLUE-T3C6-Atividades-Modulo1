# #02 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com essa formatação:

# [  1  ][  2  ][  3  ]
# [  4  ][  5  ][  6  ]
# [  7  ][  8  ][  9  ] 

# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# #03 - Aprimore o desafio anterior, mostrando no final:
#    A) A soma de todos os valores pares digitados.
#    B) A soma dos valores da terceira coluna. 
#    C) O maior valor da segunda linha.

matrizPrincipal=list()
somapar=0
soma3coluna=0
maior2linha=0
for i in range (1,4):
    matrizaux=list()
    valor=int(input(f"Insira o primeiro valor da {i}ª matriz: "))
    matrizaux.append(valor)
    if valor%2==0:
        somapar=somapar+valor
        if i==2:
            maior2linha=valor
    valor=int(input(f"Insira o segundo valor da {i}ª matriz: "))
    matrizaux.append(valor)
    if valor%2==0:
        somapar=somapar+valor
        if i==2 and valor>maior2linha:
            maior2linha=valor
    valor=int(input(f"Insira o terceiro valor da {i}ª matriz: "))
    soma3coluna=soma3coluna+valor
    matrizaux.append(valor)    
    if valor%2==0:
        somapar=somapar+valor
        if i==2 and valor>maior2linha:
            maior2linha=valor
    matrizPrincipal.append(matrizaux[:])
    
for l in range (0,3):
    for c in range(0,3):
        print(f'[{matrizPrincipal[l][c]:^5}]', end='')   
    print()

print(f"""O valor da soma dos numeros pares da matriz é : {somapar}
O valor da soma dos numeros da terceira coluna é:{soma3coluna}
O maior valor da segunda linha é segunda linha é :{maior2linha}""")
    