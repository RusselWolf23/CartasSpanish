class Carta:
    def __init__(self, numero, palo):
        self.numero=numero
        self.palo=palo

    def ver(self):
        return str(f"{self.numero} {self.palo}")
    
