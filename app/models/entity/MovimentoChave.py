from .Chave import Chave

"""
Classe Movimento Chave
@author - Fabio
@version - 1.0
@since - 19/06/2023
"""

class MovimentoChave:
    id: int
    dataRet: str
    horaRet: str
    dataDev: str
    horaDev: str
    chave: Chave
    delete: bool

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def dataRet(self) -> str:
        return self._dataRet
    
    @dataRet.setter
    def dataRet(self, dataRet: str) -> None:
        self._dataRet = dataRet

    @property
    def horaRet(self) -> str:
        return self._horaRet
    
    @horaRet.setter
    def horaRet(self, horaRet: str) -> None:
        self._horaRet = horaRet

    @property
    def dataDev(self) -> str:
        return self._dataDev
    
    @dataDev.setter
    def dataDev(self, dataDev: str) -> None:
        self._dataDev = dataDev
    
    @property
    def horaDev(self) -> str:
        return self._horaDev
    
    @horaDev.setter
    def horaDev(self, horaDev: str) -> None:
        self._horaDev = horaDev
    
    @property
    def chave(self) -> Chave:
        return self._chave
    
    @chave.setter
    def chave(self, chave: Chave) -> None:
        self._chave = chave
    
    @property
    def delete(self) -> bool:
        return self._delete
    
    @delete.setter
    def delete(self, delete: bool) -> None:
        self._delete = delete

    def calcularTempo(self) -> str:
        pass

    def verificaRetirada(self) -> bool:
        if self.dataDev != "" and self.horaDev != "":
            return True
        else:
            return False