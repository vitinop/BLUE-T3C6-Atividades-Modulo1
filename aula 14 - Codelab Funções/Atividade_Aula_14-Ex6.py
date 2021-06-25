# 6. Escreva uma função que, dado um número nota representando a nota de um estudante, 
# converte o valor de nota para um conceito (A, B, C, D, E e F).
# Nota -Conceito
# >=9.0 -A
# >=8.0 - B
# >=7.0 -C
# >=6.0 -D
# <=4.0 -F
def conceito(nota=0):
    nota=float(input("Informe a nota do aluno "))
    if nota>=9:
        return f'Conceito A'
    elif nota>=8:
        return f'Conceito B'
    elif nota>=7:
        return f'Conceito C'
    elif nota>=6:
        return f'Conceito D'
    elif nota<6:
        return f'Conceito F'
conceitoFinal=conceito()
print(conceitoFinal)