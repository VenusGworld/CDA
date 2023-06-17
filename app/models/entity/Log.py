from ..entity.Usuario import Usuario
from datetime import datetime
import json

"""
Classe Log
@author - Fabio
@version - 2.0
@since - 23/05/2023
"""

class Log:
    id: int
    acao: str
    dataHora: datetime
    observacao: str
    usuario: Usuario
    dadosAntigos: dict
    dadosNovos: dict

    def set_acao(self, acao: str) -> None:
        self.acao = acao

    def set_dataHora(self, dataHora: datetime) -> None:
        self.dataHora = dataHora

    def set_observacao(self, observacao: str) -> None:
        self.observacao = observacao

    def set_usuario(self, usuario: Usuario) -> None:
        self.usuario = usuario

    def set_dadosAntigos(self, dadosAntigos: dict) -> None:
        self.dadosAntigos = dadosAntigos

    def set_dadosNovos(self, dadosNovos: dict) -> None:
        self.dadosNovos = dadosNovos

    def get_acao(self) -> str:
        return self.acao
    
    def get_dataHora(self) -> datetime:
        return self.dataHora
    
    def get_observacao(self) -> str:
        return self.observacao
    
    def get_usuario(self) -> Usuario:
        return self.usuario
    
    def converteDadosAntigos(self) -> bytes:
        jsondata = json.dumps(self.dadosAntigos)

        return bytes(jsondata, encoding='utf-8')
    
    def converteDadosNovos(self) -> bytes:
        jsondata = json.dumps(self.dadosNovos)

        return bytes(jsondata, encoding='utf-8')