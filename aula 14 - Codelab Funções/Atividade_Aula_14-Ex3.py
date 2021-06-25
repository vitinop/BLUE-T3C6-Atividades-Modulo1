# 3. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: 
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
#  A função “altera” o valor de custo para incluir o imposto sobre vendas.
def somaImposto(taxaImposto=0,custo=0):
    valorfinal =0
    while True:
        taxaImposto =float(input("Informe a taxa de imposto: " ))
        if taxaImposto<0: 
            print("Informe uma taxa entre maior que 0%")
        else:
            break 
    custo=float(input("Informe o valor de custo "))
    valorfinal=custo+(custo*(taxaImposto/100))
    return(valorfinal)

valorfinal=somaImposto()
print(f"O valor final do produto acrecido o imposto é R${valorfinal}")