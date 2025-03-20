from abc import ABC, abstractmethod

class elementoInterface(ABC):

    @abstractmethod
    def executar(self) -> None: pass
        
