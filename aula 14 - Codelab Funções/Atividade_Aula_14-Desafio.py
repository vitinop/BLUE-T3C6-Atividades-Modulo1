# DESAFIO - Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA 
# e devolva uma string no formato D de mesPorExtenso de AAAA. 
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida. 
# Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bissexto, sendo que nesses casos Fevereiro terá 29 dias.
# Anos divisiveis por por 4, com resto 0 , são bissextos

def data(value):#DD/MM/AAAA
    mes={"01":"janeiro" ,"02":"fevereiro", "03":"março","04":"abril","05":"maio","06":"junho",
        "07":"julho","08":"agosto","09":"setembro", "10":"outubro", "11":"novembro","12":"dezembro"}
    dia =(value[0:2])
    dia=int(dia)
    mes_chave = value[3:5]
    mes_numero =int(mes_chave)
    ano =value[6:10]
    ano=int(ano)
    if mes_numero>12 or mes_numero<1:
        return f"Mês inválido, insira um mês válido:"
    elif ano%4==0 and mes_chave=="02":
        if dia>29:
            return f"Dia invalido, fevereiro possui 29 dias em anos bissextos"
    elif mes_chave=="02" and dia>28:
            return f"Dia invalido, fevereiro possui 28 dias em anos não bissextos"
    return f'{dia} de {mes[mes_chave]} de {ano}'

#Main Program
data_informada = input('Informe uma data no formato DD/MM/AAAA: ')
data_escrita = data(data_informada)
print(data_escrita)


