
"""
Classe Chave
@author - Fabio
@version - 2.0
@since - 27/06/2023
"""

class Chave:
    id: int
    codigo: str
    nome: str
    ativo: bool
    delete: bool

    def __init__(self) -> None:
        self._id = None
        self._codigo = None
        self._nome = None
        self._ativo = None
        self._delete = None

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
            "ativo": self._ativo,
            "delete": self._delete
        }

        return json