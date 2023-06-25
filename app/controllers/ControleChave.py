from flask import session
from ..models.entity.MovimentoChave import MovimentoChave
from ..models.dao.ControleChaveDao import ControleChaveDao

"""
Classe Controller para o controle de Chave
@author - Fabio
@version - 1.0
@since - 23/05/2023
"""

class ControleCrontoleDeChave:

    def inserirRetirada(self, dataRet: str, horaRet: str, idChave: str) -> int:
        movimentoChave = MovimentoChave()
        controleChaveDao = ControleChaveDao()
        movimentoChave.dataRet = dataRet
        movimentoChave.horaRet = horaRet
        movimentoChave.delete = False

        if controleChaveDao.inserirRetirada(movimentoChave):
            return 1
        else:
            return 0


    def listaChavesRetiradas(self) -> list[dict]:
        controleChaveDao = ControleChaveDao()
        respDao = controleChaveDao.consultaChavesRetiradas()
        listaChave = []
        for chave in respDao:
            dicChave ={
                "id": chave.id_movChave,
                "nome": chave.ch_nome,
                "retirada": f"{chave.mch_dataRet} + {chave.mch_horaRet}",
                "responsavel": chave.mch_respRet           
            }

            listaChave.append(dicChave)
        
        return listaChave


