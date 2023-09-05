from ..models.dao.ManterFuncionarioDao import ManterFuncionarioDao
from ..models.dao.ControleChaveDao import ControleChaveDao
from ..models.entity.MovimentoChave import MovimentoChave
from ..models.dao.ManterChaveDao import ManterChaveDao
from typing import Optional


class ControleGerarRelatorio:
    """
    Classe Controller para funções relacionadas ao gerar relatórios
    @author - Fabio
    @version - 1.0
    @since - 28/06/2023
    """

    def gerarRelatControleChave(self, dataDe: str, dataAte: str, chaveRet: Optional[str]=None) -> list[MovimentoChave]:
        """
        Consulta movimentos de chaves dentro do range de datas que foi passado.

        :param dataDe: A data início da consulta no formato YYYY-MM-DD.
        :param dataAte: A data final da consulta no formato YYYY-MM-DD.
        :param chave: (opcional) Uma chave específica para consultar os movimentos.

        :return: Uma lista com objetos MovimentoChave contendo as informações da cada um.
        """

        manterChaveDao = ManterChaveDao()
        controleChaveDao = ControleChaveDao()
        manterFuncionarioDao = ManterFuncionarioDao()

        if chaveRet != None:
            chave = manterChaveDao.consultarChaveDetalhadaCodigo(list(chaveRet.split())[0])
            movimentos = controleChaveDao.consultaMovimentosRelatIdChave(dataDe.replace("-", ""), dataAte.replace("-", ""), chave.id)
        else:
            movimentos = controleChaveDao.consultaMovimentosRelatChave(dataDe.replace("-", ""), dataAte.replace("-", ""))

        listaMovimentos = []
        for movimento in movimentos:
            chave = manterChaveDao.consultarChaveDetalhadaId(movimento.mch_idChav)
            funcRet = manterFuncionarioDao.consultarFuncionarioDetalhado(movimento.mch_respRet)
            funcDev = manterFuncionarioDao.consultarFuncionarioDetalhado(movimento.mch_respDev)
            movChave = MovimentoChave(dataRet=movimento.mch_dataRet, horaRet=movimento.mch_horaRet, respRet=funcRet, 
                                      dataDev=movimento.mch_dataDev, horaDev=movimento.mch_horaDev, respDev=funcDev, 
                                      chave=chave)
            
            listaMovimentos.append(movChave)

        return listaMovimentos