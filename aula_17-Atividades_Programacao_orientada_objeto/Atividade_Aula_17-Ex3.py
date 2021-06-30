# Crie uma classe que modele uma pessoa
# a)Atributos nome, idade, peso e altura
# b)Métodos envelhecer, engordar, emagrecer, crescer
# Por padrão, a cada ano que a pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self, anos):
        return self.crescer(anos)
    def engordar(self, calorias):
        self.peso += calorias * 0.000125
    def emagrecer(self, horasExercicio):
        self.peso -= horasExercicio * 0.1
    def crescer(self, anos):
        if self.idade < 21:
            if self.idade + anos < 21:
                self.altura += anos * (0.5)
            else:
                self.altura += (21 - self.idade) * 0.5
        self.idade += anos
    

pessoa1 = Pessoa('Felipe', 20, 73, 178)

print(f'''RELATÓRIO INICIAL:
Nome: {pessoa1.nome}
Idade: {pessoa1.idade} anos
Peso: {pessoa1.peso:.2f} kg
ALtura: {pessoa1.altura:.2f} cm''')

pessoa1.envelhecer(50)
print(f'''\nIdade após 50 anos: {pessoa1.idade} anos.
Altura após 50 anos: {pessoa1.altura:.2f} cm.''')

pessoa1.crescer(2)
print(f'''\nIdade após +2 anos: {pessoa1.idade} anos.
Altura após +2 anos: {pessoa1.altura:.2f} cm.''')

pessoa1.engordar(8000)
print(f'\nPeso após ingerir 8000 calorias: {pessoa1.peso:.2f} kg.')

pessoa1.emagrecer(18)
print(f'\nPeso após fazer 18h de caminhada: {pessoa1.peso:.2f} kg.')

print(f'''\nRELATÓRIO FINAL:
Nome: {pessoa1.nome}
Idade: {pessoa1.idade} anos
Peso: {pessoa1.peso:.2f} kg
ALtura: {pessoa1.altura:.2f} cm''')