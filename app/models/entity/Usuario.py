from datetime import datetime
from random import randint
import bcrypt

"""
Classe Usuario
@author - Fabio
@version - 2.0
@since - 23/05/2023
"""

class Usuario:
    id: int
    nome: str
    email: str
    grupo: str
    usuario: str
    senha: str
    complex: str
    ativo: bool
    delete: bool
    senhaCompara: str
    senhaNova: bool
    hashSenhaNova: str
    limiteNovasenha: datetime

    def __init__(self) -> None:
        self._id = None
        self._nome = None
        self._email = None
        self._grupo = None
        self._usuario = None
        self._senha = None
        self._complex = None
        self._ativo = None
        self._delete = None
        self._senhaCompara = None
        self._senhaNova = None
        self._hashSenhaNova = None
        self._limiteNovasenha = None

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, email: str) -> None:
        self._email = email

    @property
    def grupo(self) -> str:
        return self._grupo
    
    @grupo.setter
    def grupo(self, grupo: str) -> None:
        self._grupo = grupo
    
    @property
    def usuario(self) -> str:
        return self._usuario
    
    @usuario.setter
    def usuario(self, usuario: str) -> None:
        self._usuario = usuario
    
    @property
    def senha(self) -> str:
        return self._senha
    
    @senha.setter
    def senha(self, senha: str) -> None:
        self._senha = senha
    
    @property
    def complex(self) -> str:
        return self._complex
    
    @complex.setter
    def complex(self, complex: str) -> None:
        self._complex = complex
    
    @property
    def ativo(self) -> bool:
        return self._ativo
    
    @ativo.setter
    def ativo(self, ativo: bool) -> None:
        self._ativo = ativo
    
    @property
    def delete(self) -> bool:
        return self._delete
    
    @delete.setter
    def delete(self, delete: bool) -> None:
        self._delete = delete
    
    @property
    def senhaCompara(self) -> str:
        return self._senhaCompara
    
    @senhaCompara.setter
    def senhaCompara(self, senhaCompara: str) -> None:
        self._senhaCompara = senhaCompara
    
    @property
    def senhaNova(self) -> bool:
        return self._senhaNova
    
    @senhaNova.setter
    def senhaNova(self, senhaNova: bool) -> None:
        self._senhaNova = senhaNova
    
    @property
    def hashSenhaNova(self) -> str:
        return self._hashSenhaNova
    
    @hashSenhaNova.setter
    def hashSenhaNova(self, hashSenhaNova: str) -> None:
        self._hashSenhaNova = hashSenhaNova

    @property
    def limiteNovasenha(self) -> str:
        return self._limiteNovasenha
    
    @limiteNovasenha.setter
    def limiteNovasenha(self, limiteNovasenha: str) -> None:
        self._limiteNovasenha = limiteNovasenha
    

    def gerarSenha(self, senha: str) -> None:
        salt = bcrypt.gensalt(8)
        hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
        self._senha = hash.decode("utf-8")
        self._complex = salt.decode("utf-8")
        

    def verificarSenha(self) -> bool:
        print(self._senha)
        hash = bcrypt.hashpw(self._senha.encode('utf-8'), bytes(self._complex, 'utf-8'))
        if hash.decode('utf-8') == self._senhaCompara:
            return True
        else:
            return False


    def toJson(self) -> dict:
        json = {
            "id": self._id,
            "nome": self._nome,
            "email": self._email,
            "usuario": self._usuario,
            "senha": self._senha,
            "grupo": self._grupo,
            "complex": self._complex,
            "ativo": self._ativo,
            "delete": self._delete
        }

        return json
    

    def toUsuario(self, dic: dict):
        pass


    def gerarHashSenhaNova(self):
        hash: list = []

        for x in range(10):
            hash.append(randint(1, 9))

        self._hashSenhaNova = "".join(map(str, hash))
        self._senhaNova = True


    def apagaHashSenhaNova(self):
        self._hashSenhaNova = ""
        self._senhaNova = False