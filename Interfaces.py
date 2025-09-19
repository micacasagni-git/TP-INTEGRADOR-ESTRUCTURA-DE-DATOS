from abc import ABC, abstractmethod
from typing import List

class IEnviar(ABC):
    @abstractmethod
    def enviar_mensaje(self, mensaje) -> None:
        pass

class IRecibir(ABC):
    @abstractmethod
    def recibir_mensaje(self, mensaje) -> None:
        pass

class IListarMensajes(ABC):
    @abstractmethod
    def listar_mensajes(self) -> List:
        pass
