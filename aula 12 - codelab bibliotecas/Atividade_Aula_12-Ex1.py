# 1. Exercício Treino - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 (que podem ser armazenados em uma lista) 
# e seus valores correspondentes aos quadrados desses números.{1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}
lista=[1,4,5,6,7,9]
dicionario=dict()
for i in lista :
    dicionario[i]=i
for i, j in dicionario.items():
    valor=j**2
    dicionario[j]= valor
print(dicionario)