
"""
Classe Chave
@author - Fabio
@version - 1.0
@since - 19/06/2023
"""

class Chave:
    id: int
    codigo: str
    nome: str

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
