from .ManterFuncionarioDao import ManterFuncionarioDao
from ..entity.MovimentoChave import MovimentoChave
from ..Tables import CDA002, CDA005, CDA007
from .ManterChaveDao import ManterChaveDao
from ...configurations.Database import DB


class ControleChaveDao:
    """
    Classe Dao para funções do contole de chave
    @tables - CDA002, CDA005, CDA007
    @author - Fabio
    @version - 1.0
    @since - 10/07/2023
    """

    def inserirRetirada(self, movimento: MovimentoChave) -> bool:
        """
        Insere um registro de movimento de retirada de chave.

        :param movimento: Um objeto contendo informações sobre a retirada de chave.

        :return: True se a inserção foi bem-sucedida, False caso contrário.
        """
        
        movimentoRet = CDA002(dataRet=movimento.dataRet, horaRet=movimento.horaRet,
                              delete=movimento.delete, idChave=movimento.chave.id,
                              idFunc=movimento.respRet.id)
        
        DB.session.add(movimentoRet)
        DB.session.commit()
        return True
    

    def inserirDevolucao(self, movimento: MovimentoChave) -> bool:
        """
        Insere um registro de devolução de chave.

        :param movimento: Um objeto contendo informações sobre a devolução de chave.
        
        :return: True se a atualização foi bem-sucedida, False caso contrário.
        """
        movimentoDev = CDA002.query.get(movimento.id)
        
        movimentoDev.mch_dataDev = movimento.dataDev
        movimentoDev.mch_horaDev = movimento.horaDev
        movimentoDev.mch_respDev = movimento.respDev.id
       

        DB.session.commit()
        return True

    
    def consultaMovimentoChaveDetalhado(self, id: int) -> MovimentoChave:
        """
        Consulta detalhes de um movimento de chave específico.

        :param id: O ID do movimento de chave a ser consultado.

        :return: Um objeto MovimentoChave contendo os detalhes do movimento de chave.
        """

        manterFuncionarioDao = ManterFuncionarioDao()
        manterChaveDao = ManterChaveDao()
        mov = CDA002.query.get(id)

        movimento = MovimentoChave(id=mov.id_movChave, dataRet=mov.mch_dataRet, horaRet=mov.mch_horaRet, 
                                   respRet=manterFuncionarioDao.consultarFuncionarioDetalhado(mov.mch_respRet),
                                   respDev=manterFuncionarioDao.consultarFuncionarioDetalhado(mov.mch_respDev),
                                   dataDev=mov.mch_dataDev, horaDev=mov.mch_horaDev, delete=mov.mch_delete,
                                   chave=manterChaveDao.consultarChaveDetalhadaId(mov.mch_idChav))
        
        return movimento


    def consultaChavesRetiradas(self) -> CDA002:
        """
        Consulta as chaves que foram retiradas, mas ainda não foram devolvidas.

        :return: Um objeto de consulta contendo detalhes dos movimentos de chave em aberto.
        """

        chavesRetiradas = DB.session\
            .query(CDA002.id_movChave, CDA002.mch_horaRet, CDA002.mch_dataRet, CDA002.mch_respRet, CDA005.ch_nome.label("nomeChave"), CDA007.fu_nome.label("nomeResp"))\
            .join(CDA005, CDA005.id_chave == CDA002.mch_idChav).join(CDA007, CDA007.id_funcionario == CDA002.mch_respRet)\
                .filter(CDA002.mch_dataDev==None, CDA002.mch_horaDev==None, CDA002.mch_delete!=True)
       
        return chavesRetiradas
    

    def consultaChavesManut(self) -> CDA002:
        """
        Consulta os registros de movimento de chaves com retirada e devolução (completos) para manutenções.

        :return: Um objeto de consulta contendo detalhes dos movimentos de chave para a manutenção.
        """
        
        chavesRetiradas = DB.session\
            .query(CDA002.id_movChave, CDA002.mch_horaRet, CDA002.mch_dataRet, CDA002.mch_respRet, CDA002.mch_dataDev, CDA002.mch_horaDev, CDA005.ch_nome.label("nomeChave"), CDA007.fu_nome.label("nomeResp"))\
            .join(CDA005, CDA005.id_chave == CDA002.mch_idChav).join(CDA007, CDA007.id_funcionario == CDA002.mch_respRet)\
                .filter(CDA002.mch_dataDev!=None, CDA002.mch_horaDev!=None, CDA002.mch_delete!=True)
       
        return chavesRetiradas
    

    def verificaMovAbertoChave(self, idChave: int) -> CDA002:
        """
        Verifica se existem movimentos de chave abertos associados a uma chave específica.

        :param idChave: O ID da chave para a qual deseja verificar a existência de movimentos abertos.

        :return: Um objeto de consulta contendo os IDs dos movimentos de chave abertos associados à chave fornecida.
        """

        idsMov = DB.session.query(CDA002.id_movChave).filter(CDA002.mch_idChav==idChave)

        return idsMov
    

    def consultaMovAbertoChave(self, id: int) -> CDA002:
        """
        Consulta um movimento de chave aberto pelo seu ID.

        :param id: O ID do movimento de chave que deseja consultar.

        :return: O objeto de movimento de chave aberto correspondente ao ID fornecido.
        """

        movimento = CDA002.query.filter(CDA002.id_movChave==id, CDA002.mch_dataDev==None, CDA002.mch_horaDev==None).first()

        return movimento