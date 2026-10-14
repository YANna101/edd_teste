class Ponto:
    def __init__(self, x, y, raio=0, alpha=0):
        self.x = x
        self.y = y
        self.raio = raio
        self.alpha = alpha
        
    # somar
    # def somar(self):
    #     return self.x + self.y

    # # subtrair
    # def subtrair(self):
    #     return self.x - self.y


    def __add__(self, other):
        return Ponto(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Ponto(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Ponto({self.x}, {self.y})"
    
    
p1 = Ponto(3, 4)
p2 = Ponto(1, 2)
p3 = p1 + p2
p4 = p1 - p2
print(p3)
print(p4)