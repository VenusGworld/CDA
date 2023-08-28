from typing import Optional

"""
Classe Terceiro
@author - Fabio
@version - 2.0
@since - 26/07/2023
"""

class Terceiro:
    id: int
    codigo: str
    nome: str
    cpf: str
    ativo: bool
    delete: bool

    def __init__(self, id: Optional[int]=None, codigo: Optional[str]=None, nome: Optional[str]=None,
                 cpf: Optional[str]=None, ativo: Optional[bool]=None, delete: Optional[bool]=None) -> None:
        self._id = id
        self._codigo = codigo
        self._nome = nome
        self._cpf = cpf
        self._ativo = ativo
        self._delete = delete

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def codigo(self) -> str:
        return self._codigo
    
    @codigo.setter
    def codigo(self, codigo: str) -> None:
        self._codigo = codigo
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def cpf(self) -> str:
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf: str) -> None:
        self._cpf = cpf

    @property
    def ativo(self) -> str:
        return self._ativo
    
    @ativo.setter
    def ativo(self, ativo: str) -> None:
        self._ativo = ativo
        
    @property
    def delete(self) -> str:
        return self._delete
    
    @delete.setter
    def delete(self, delete: str) -> None:
        self._delete = delete
    
    def toJson(self) -> dict:
        json = {
            "id": self._id,
            "codigo": self._codigo,
            "nome": self._nome,
            "cpf": self._cpf,
            "ativo": self._ativo,
            "delete": self._delete
        }

        return json