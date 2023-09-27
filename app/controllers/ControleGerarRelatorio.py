from ..models.dao.ManterFuncionarioDao import ManterFuncionarioDao
from ..models.dao.ControleTerceiroDao import ControleTerceiroDao
from ..models.dao.ControleGerenteDao import ControleGerenteDao
from ..models.entity.MovimentoGerente import MovimentoGerente
from ..models.dao.ManterTerceiroDao import ManterTerceiroDao
from ..models.dao.ControleChaveDao import ControleChaveDao
from ..models.entity.MovimentoChave import MovimentoChave
from ..models.dao.ManterChaveDao import ManterChaveDao

class ControleGerarRelatorio:
    """
    Classe Controller para funções relacionadas ao gerar relatórios
    @author - Fabio
    @version - 1.0
    @since - 28/06/2023
    """

    def gerarRelatControleChave(self, dataDe: str, dataAte: str, chaveRet: str) -> list[MovimentoChave]:
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

        if len(chaveRet.strip()) != 0:
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
    

    def gerarRelatControleGerente(self, dataDe: str, dataAte: str, func: str) -> list[MovimentoGerente]:
        """
        Consulta movimentos de gerentes dentro do range de datas que foi passado.

        :param dataDe: A data início da consulta no formato YYYY-MM-DD.
        :param dataAte: A data final da consulta no formato YYYY-MM-DD.
        :param gerente: (opcional) Um gerente específico para consultar os movimentos.

        :return: Uma lista com objetos MovimentoGerente contendo as informações da cada um.
        """

        controleGerenteDao = ControleGerenteDao()
        manterFuncionarioDao = ManterFuncionarioDao()

        if len(func.strip()) != 0:
            gerente = manterFuncionarioDao.consultarFuncionarioDetalhadoCracha(list(func.split())[0])
            movimentos = controleGerenteDao.consultaMovimentosRelatIdGerente(dataDe.replace("-", ""), dataAte.replace("-", ""), gerente.id)
        else:
            movimentos = controleGerenteDao.consultaMovimentosRelatGerente(dataDe.replace("-", ""), dataAte.replace("-", ""))

        listaMovimentos = []
        for movimento in movimentos:
            gerente = manterFuncionarioDao.consultarFuncionarioDetalhado(movimento.mge_idFunc)
            movGerente = MovimentoGerente(dataEnt=movimento.mge_dataEntra, horaEnt=movimento.mge_horaEntra, gerente=gerente, 
                                          dataSai=movimento.mge_dataSaid, horaSai=movimento.mge_horaSaid)
            
            listaMovimentos.append(movGerente)

        return listaMovimentos
    

    def gerarRelatControleTerceiros(self, dataDe: str, dataAte: str, terceiro: str) -> list[MovimentoGerente]:
        """
        Consulta movimentos de gerentes dentro do range de datas que foi passado.

        :param dataDe: A data início da consulta no formato YYYY-MM-DD.
        :param dataAte: A data final da consulta no formato YYYY-MM-DD.
        :param gerente: (opcional) Um gerente específico para consultar os movimentos.

        :return: Uma lista com objetos MovimentoGerente contendo as informações da cada um.
        """

        controleTerceiroDao = ControleTerceiroDao()
        manterTerceiroDao = ManterTerceiroDao()

        if len(terceiro.strip()) != 0:
            gerente = manterTerceiroDao.consultarTerceiroDetalhadoCpf(list(terceiro.split())[0])
            movimentos = controleTerceiroDao.consultaMovimentosRelatIdTerc(dataDe.replace("-", ""), dataAte.replace("-", ""), gerente.id)
        else:
            movimentos = controleTerceiroDao.consultaMovimentosRelatTerceiro(dataDe.replace("-", ""), dataAte.replace("-", ""))

        listaMovimentos = []
        for movimento in movimentos:
            gerente = manterTerceiroDao.consultarTerceiroDetalhadoId(movimento.mge_idFunc)
            movGerente = MovimentoGerente(dataEnt=movimento.mge_dataEntra, horaEnt=movimento.mge_horaEntra, gerente=gerente, 
                                          dataSai=movimento.mge_dataSaid, horaSai=movimento.mge_horaSaid)
            
            listaMovimentos.append(movGerente)

        return listaMovimentos