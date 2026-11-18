from __future__ import annotations

class No:
    def __init__(self, dado: object, prox: No = None):
        self.dado = dado
        self.prox = prox
        
    
    def __gt__(self, other: No) -> bool:
        return self.dado > other.dado
    
    
    def __str__(self) -> str:
        return str(self.dado)
    