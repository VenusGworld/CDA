from .Funcionario import Funcionario

"""
Classe Movimento Gerente
@author - Fabio
@version - 1.0
@since - 11/08/2023
"""

class MovimentoGerente:
    id: int
    dataEnt: str
    horaEnt: str
    gerente: Funcionario
    dataSai: str
    horaSai: str
    delete: bool

    def __init__(self) -> None:
        self._id = None
        self._dataEnt = None
        self._horaEnt = None
        self._gerente = None
        self._dataSai = None
        self._horaSai = None
        self._delete = None

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def dataEnt(self) -> str:
        return self._dataEnt
    
    @dataEnt.setter
    def dataEnt(self, dataEnt: str) -> None:
        self._dataEnt = dataEnt

    @property
    def horaEnt(self) -> str:
        return self._horaEnt
    
    @horaEnt.setter
    def horaEnt(self, horaEnt: str) -> None:
        self._horaEnt = horaEnt

    @property
    def gerente(self) -> Funcionario:
        return self._gerente
    
    @gerente.setter
    def gerente(self, gerente: Funcionario) -> None:
        self._gerente = gerente

    @property
    def dataSai(self) -> str:
        return self._dataSai
    
    @dataSai.setter
    def dataSai(self, dataSai: str) -> None:
        self._dataSai = dataSai

    @property
    def horaSai(self) -> str:
        return self._horaSai
    
    @horaSai.setter
    def horaSai(self, horaSai: str) -> None:
        self._horaSai = horaSai

    @property
    def delete(self) -> bool:
        return self._delete
    
    @delete.setter
    def delete(self, delete: bool) -> None:
        self._delete = delete

    def toJson(self) -> dict:
        json = {
            "id": self._id,
            "dataEnt": self._dataEnt,
            "horaEnt": self._horaEnt,
            "gerente": self._gerente.toJson(),
            "dataSai":  self._dataSai,
            "horaSai": self._horaSai,
            "delete": self._delete
        }

        return json