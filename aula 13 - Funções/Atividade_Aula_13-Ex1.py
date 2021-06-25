# Faça um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições:
def voto():
    import datetime
    now=datetime.datetime.now()
    ano_atual = now.year
    ano_nasc=int(input("Informe seu ano de nascimento: "))
    idade=ano_atual-ano_nasc
    if 18 <= idade <70:
        return f"O voto do indiviuo é OBRIGATÓRIO"
    elif idade>=16  or idade>=70:
        return f"O voto do indiviuo é OPCIONAL"
    elif idade<16:
        return f"O voto do indiviuo é NEGADO"
   
situacaoEleitoral=voto()
print(situacaoEleitoral)