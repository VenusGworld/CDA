
class Funcionario:
    id: int
    nome: str
    cracha: str
    maquina: str
    gerente: bool
    ativo: bool
    delete: bool

    def __init__(self) -> None:
        self._id = None
        self._nome = None
        self._cracha = None
        self._maquina = None
        self._gerente = None
        self._ativo = None
        self._delete = None

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

    

