from aula09_fila import Fila


class Carro:
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa

    def __str__(self):
        return f"{self.modelo} - {self.placa}"


class FilaCarrosEstudo(Fila):
    def __init__(self):
        super().__init__()

    def adicionar_carro(self, carro):
        self.enfileirar(carro)

    def remover_carro(self):
        return self.desenfileirar()

    def listar_carros(self):
        print("Tamanho da fila de carros: ", self.tamanho())
        if not self.esta_vazia():
            print("Carro no início da fila:", self.consultar_inicio().dado)
        else:
            print("A fila está vazia.")
            
       
if __name__ == "__main__":
    fila_carros_exemplo = FilaCarrosEstudo()
    carro1 = Carro("Toyota", "ABC-1234")
    carro2 = Carro("Honda", "XYZ-5678")
    carro3 = Carro("Ford", "LMN-9012")
    carro4 = Carro("Chevrolet", "DEF-3456")
    carro5 = Carro("Volkswagen", "GHI-7890")
    
    fila_carros_exemplo.adicionar_carro(carro1)
    fila_carros_exemplo.adicionar_carro(carro2)
    fila_carros_exemplo.adicionar_carro(carro3)
    fila_carros_exemplo.adicionar_carro(carro4)
    fila_carros_exemplo.adicionar_carro(carro5)

    fila_carros_exemplo.listar_fila()
    
    print("Removendo carro:", fila_carros_exemplo.remover_carro().dado)
    fila_carros_exemplo.listar_carros()