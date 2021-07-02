class Relogio:
    def __init__(self):
        self.horas = 6
        self.minutos = 0
    
    def __str__(self): # Pesquisar significado dessa função especifica.
        return f"{self.horas:02d}:{self.minutos:02d}"
    
    def avancaTempo(self, minutos,horas):
        self.horas+= horas
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1
    