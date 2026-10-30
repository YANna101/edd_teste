from aula09_fila import fila
from aula09_fila import no
class FilaDupla(fila.Fila):
    def __init__(self):
        super().__init__()
        self._inicio = None
        self._fim = None

    def inserir_inicio(self, valor):
        novo_no = no.No(valor)
        if self.esta_vazia():
            self._inicio = novo_no
            self._fim = novo_no
        else:
            novo_no.proximo = self._inicio
            self._inicio.anterior = novo_no
            self._inicio = novo_no
        self._tamanho += 1

    def inserir_fim(self, valor):
        novo_no = no.No(valor)
        if self.esta_vazia():
            self._inicio = novo_no
            self._fim = novo_no
        else:
            novo_no.anterior = self._fim
            self._fim.proximo = novo_no
            self._fim = novo_no
        self._tamanho += 1

    def remover_inicio(self):
        if self.esta_vazia():
            raise Exception("Fila vazia")
        valor_removido = self._inicio.valor
        if self._inicio == self._fim:
            self._inicio = None
            self._fim = None
        else:
            self._inicio = self._inicio.proximo
            self._inicio.anterior = None
        self._tamanho -= 1
        return valor_removido

    def remover_fim(self):
        if self.esta_vazia():
            raise Exception("Fila vazia")
        valor_removido = self._fim.valor
        if self._inicio == self._fim:
            self._inicio = None
            self._fim = None
        else:
            self._fim = self._fim.anterior
            self._fim.proximo = None
        self._tamanho -= 1
        return valor_removido

    def imprimir(self):
        atual = self._inicio
        while atual is not None:
            print(atual.valor, end=" ")
            atual = atual.proximo
        print()
        
        if self._fim is not None:
            atual = self._fim
            while atual is not None:
                print(atual.valor, end=" ")
                atual = atual.anterior
            print()
            
            class FilaDuplaCircular(FilaDupla):
                def __init__(self):
                    super().__init__()
                    self._fim.proximo = self._inicio
                    self._inicio.anterior = self._fim

                def inserir_inicio(self, valor):
                    super().inserir_inicio(valor)
                    self._fim.proximo = self._inicio
                    self._inicio.anterior = self._fim

                def inserir_fim(self, valor):
                    super().inserir_fim(valor)
                    self._fim.proximo = self._inicio
                    self._inicio.anterior = self._fim

                def remover_inicio(self):
                    valor_removido = super().remover_inicio()
                    if not self.esta_vazia():
                        self._fim.proximo = self._inicio
                        self._inicio.anterior = self._fim
                    return valor_removido

                def remover_fim(self):
                    valor_removido = super().remover_fim()
                    if not self.esta_vazia():
                        self._fim.proximo = self._inicio
                        self._inicio.anterior = self._fim
                    return valor_removido                 
