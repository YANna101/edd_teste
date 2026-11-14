from aula09_fila_dupla import FilaDupla  # Remova esta linha se for recriar a classe abaixo

class Estela:
    def __init__(self, nome, cor, tamanho, constelacao):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.constelacao = constelacao
        self.proximo = None
        self.anterior = None

class FilaDupla:  # Corrigido de class (FilaDupla):
    def __init__(self):
        self.fila1 = []
        self.fila2 = []
        
    def adicionar_estela(self, estela):
        if len(self.fila1) <= len(self.fila2):
            self.fila1.append(estela)
        else:
            self.fila2.append(estela)

                
                
                

                    
                    
        
    