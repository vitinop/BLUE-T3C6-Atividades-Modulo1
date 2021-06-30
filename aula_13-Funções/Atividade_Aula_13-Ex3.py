# Faça um programa em Python com uma função que necessite de três parametros, e que forneça:
# A soma desses três parametros através de uma função.
# Seu script também deve fornecer a média dos três números,  através de uma segunda função que chama a primeira.
number = list()
def getValues():
    for i in range(3):
        number.extend([float(input("digite um valor: "))])
    show = performMedia(makeSum(number[0],number[1],number[2]))
    print("A média é:",show)
#realiza soma
def makeSum(firstnumber=0,secondnumber=0,thirdnumber=0):
    sumnumbers= firstnumber+secondnumber+thirdnumber
    return sumnumbers
#realiza calculo de média
def performMedia(sumnumbers=0):
    return (sumnumbers/3)

getValues()