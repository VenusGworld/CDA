from typing import Optional

"""
Classe funcionário
@author - Fabio
@version - 1.0
@since - 20/05/2023
"""

class Funcionario:
    id: int
    nome: str
    cracha: str
    maquina: str
    gerente: bool
    ativo: bool
    delete: bool

    def __init__(self, id: Optional[int]=None, nome: Optional[str]=None, cracha: Optional[str]=None, 
                 maquina: Optional[str]=None, gerente: Optional[bool]=None, ativo: Optional[bool]=None, 
                 delete: Optional[bool]=None) -> None:
        self._id = id
        self._nome = nome
        self._cracha = cracha
        self._maquina = maquina
        self._gerente = gerente
        self._ativo = ativo
        self._delete = delete

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cracha(self) -> str:
        return self._cracha
    
    @cracha.setter
    def cracha(self, cracha):
        self._cracha = cracha
    
    @property
    def maquina(self) -> str:
        return self._maquina
    
    @maquina.setter
    def maquina(self, maquina):
        self._maquina = maquina
    
    @property
    def gerente(self) -> bool:
        return self._gerente
    
    @gerente.setter
    def gerente(self, gerente):
        self._gerente = gerente
    
    @property
    def ativo(self) -> bool:
        return self._ativo
    
    @ativo.setter
    def ativo(self, ativo):
        self._ativo = ativo
    
    @property
    def delete(self) -> bool:
        return self._delete

    @delete.setter
    def delete(self, delete):
        self._delete = delete


    def toJson(self) -> dict:
        json ={
            "id": self._id,
            "nome": self._nome,
            "cracha": self._cracha,
            "maquina": self._maquina,
            "gerente": self._gerente,
            "ativo": self._ativo,
            "delete": self._delete
        }

        return json

    

