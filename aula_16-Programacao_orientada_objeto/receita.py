from time import sleep
class Receita:
    def __init__(self,ovo,leite,farinha,manteiga):
        self.ovo = ovo
        self.leite = leite
        self.farinha = farinha
        self.manteiga = manteiga

    def mistura(self):
        if self.ovo==2:
            return "Bolo Misturando..."
        else:
            return "você precisa de no minimo 2 ovos, para misturar o bolo"

    def assar():
        print('bolo sendo assado...')
        sleep(2)
        print('seu bolo está pronto')
