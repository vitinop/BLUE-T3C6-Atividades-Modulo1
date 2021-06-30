# 2. Exercício Treino - Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] 
# e cada valor associado é o número ao quadrado.
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
lista=[1,2,3,4,5,6,7,8,9,10]
dicionario=dict()
for i in lista :
    dicionario[i]=i
for i, j in dicionario.items():
    valor=j**2
    dicionario[j]= valor
print(dicionario)