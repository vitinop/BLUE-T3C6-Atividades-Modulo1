# Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if, 
# verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela a seguinte frase para cada um deles: 
# 'Fulano é maior de idade' ou 'Fulana é menor de idade' e  também quantos são maiores e quantos são menores de idade.
listaMaior=list()
listaMenor=list()
for i in range(0,5):
    listaAux=["",0]
    nome=str(input("Insira o nome: "))
    idade=int(input("Insira a idade: "))
    listaAux[0]= nome
    listaAux[1]= idade 
    if listaAux[1]<18:
        listaMenor.append(listaAux[:])
        print(f"{listaAux[0].capitalize()} é menor de idade. ")
    else:
        listaMaior.append(listaAux[:])
        print(f"{listaAux[0].capitalize()} é maior de idade")
print(f"""
No total {len(listaMaior)} são maiores de idade
No total {len(listaMenor)} são menores de idade
""")