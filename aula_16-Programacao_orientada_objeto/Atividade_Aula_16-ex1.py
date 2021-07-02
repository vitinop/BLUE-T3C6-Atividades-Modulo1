class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nomePessoa = nome
        self.idadePessoa = idade
        self.pesoPessoa = peso
    def comer(self, calorias):
        if self.idadePessoa > 30:
            self.pesoPessoa += 2*calorias
        else:
            self.pesoPessoa += calorias
    def malhar(self, calorias):
        if self.idadePessoa < 30:
            self.pesoPessoa -= 2*calorias
        else:
            self.pesoPessoa -= calorias
    def mostrarDados(self):
        return f'''
            Nome: {self.nomePessoa}
            Idade: {self.idadePessoa}
            Peso: {self.pesoPessoa} kg'''

pessoa1 = Pessoa('nome', 23, 75)

print(pessoa1.mostrarDados())

pessoa1.comer(10)

pessoa1.malhar(15)

print(pessoa1.mostrarDados())