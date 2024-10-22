from ..entity.MovimentoGerente import MovimentoGerente
from ...configurations.Database import DB
from ..Tables import CDA003, CDA007

class ControleGerenteDao:
    """
    Classe Dao para funções do contole de Gerenete
    @tables - CDA003
    @author - Fabio
    @version - 1.0
    @since - 10/07/2023
    """

    def inserirEntrada(self, movimento: MovimentoGerente) -> bool:
        """
        Insere um novo registro de entrada de gerente na base de dados.

        :param movimento: O objeto de movimento de gerente contendo os dados da entrada.

        :return: True se a inserção for bem-sucedida, False caso contrário.
        """
        
        mov = CDA003(dataEntrada=movimento.dataEnt, horaEntrada=movimento.horaEnt,
                              delete=movimento.delete, idFunc=movimento.gerente.id)
        
        DB.session.add(mov)
        DB.session.commit()
        return True
    

    def inserirSaida(self, movimento: MovimentoGerente) -> bool:
        """
        Insere um registro de saída para um movimento de gerente na base de dados.

        :param movimento: O objeto de movimento de gerente contendo os dados da saída.

        :return: True se a atualização for bem-sucedida, False caso contrário.
        """

        #Campos a serem atualizados
        campos = {
            "mge_dataSaid": movimento.dataSai,
            "mge_horaSaid": movimento.horaSai
        }

        CDA003.query.filter(CDA003.id_movGere==movimento.id).update(campos)
        DB.session.commit()

        return True
    

    def consultaGerentesEntrada(self) -> CDA003:
        """
        Consulta os registros de entrada de gerentes na base de dados.

        :return: Uma lista de registros de entrada de gerentes em andamento.
        """
        movimentos = DB.session.query(CDA003.id_movGere, CDA003.mge_dataEntra, CDA003.mge_horaEntra, CDA007.fu_nome.label("nomeGer"))\
            .join(CDA007, CDA007.id_funcionario==CDA003.mge_idFunc)\
                .filter(CDA003.mge_dataSaid==None, CDA003.mge_horaSaid==None, CDA003.mge_delete!=True)
        
        return movimentos
    

    def editarMovimentoGerente(self, movimento: MovimentoGerente) -> bool:
        """
        Altera os dados de um movimento de gerente específico.

        :param movimento: Um objeto da classe MovimentoGerente contendo as informações para a alteração.
        
        :return: True se a edição for bem-sucedida, False caso contrário.
        """

        #Campos a serem atualizados
        campos = {
            "mge_dataEntra": movimento.dataEnt,
            "mge_horaEntra": movimento.horaEnt,
            "mge_dataSaid": movimento.dataSai,
            "mge_horaSaid": movimento.horaSai
        }

        CDA003.query.filter(CDA003.id_movGere==movimento.id).update(campos)
        DB.session.commit()

        return True
    

    def excluirMovimentoGerente(self, movimento: MovimentoGerente) -> bool:
        """
        Marca um movimento de gerente como excluido no sistema.

        :param movimento: Um objeto da classe MovimentoGerente contando o ID do movimento de gerente a ser excluido.

        :return: True se a inativação for bem-sucedida, False caso contrário.
        """

        #Campos a serem atualizados
        campos = {
            "mge_delete": True
        }

        CDA003.query.filter(CDA003.id_movGere==movimento.id).update(campos)
        DB.session.commit()

        return True
    

    def consultaMovimentoDetalhado(self, id: int) -> MovimentoGerente:
        """
        Consulta os detalhes de um registro de movimento de gerente na base de dados.

        :param id: O ID do registro de movimento de gerente a ser consultado.

        :return: Um objeto contendo os detalhes do movimento de gerente.
        """

        mov = CDA003.query.filter(CDA003.id_movGere==id).first()

        movimento = MovimentoGerente(id=mov.id_movGere, dataEnt=mov.mge_dataEntra, horaEnt=mov.mge_horaEntra, 
                                     dataSai=mov.mge_dataSaid, horaSai=mov.mge_horaSaid, delete=mov.mge_delete)

        return movimento
    

    def consultaIdGerMov(self, id: int) -> int:
        """
        Consulta o ID do gerente associado a um registro de movimento de gerente.

        :param id: O ID do registro de movimento de gerente a ser consultado.

        :return: O ID do gerente associado ao movimento.
        """
        
        mov = CDA003.query.filter(CDA003.id_movGere==id).first()

        return mov.mge_idFunc
    

    def consultaGerentesManut(self, data: str) -> CDA003:
        """
        Consulta os registros de movimento de gerentes com entrada e saída (completos) para manutenções.

        :return: Uma consulta que retorna os registros de movimento de gerentes para a manutenção.
        """
        
        movimentos = DB.session.query(CDA003.id_movGere, CDA003.mge_dataEntra, CDA003.mge_horaEntra, CDA003.mge_dataSaid, CDA003.mge_horaSaid, CDA007.fu_nome.label("nomeGer"))\
            .join(CDA007, CDA007.id_funcionario==CDA003.mge_idFunc)\
                .filter(CDA003.mge_dataSaid!=None, CDA003.mge_horaSaid!=None, CDA003.mge_delete!=True, CDA003.mge_dataEntra>=data)
        
        return movimentos
    

    def verificaMovIdGerente(self, idFunc: int) -> CDA003:
        """
        Verifica se existem movimentos de gerentes abertos associados a uma gerente específico.

        :param idFunc: O ID do gerente para a qual deseja verificar a existência de movimentos abertos.

        :return: Um objeto de consulta contendo os IDs dos movimentos de gerente abertos associados ao gerente fornecida.
        """

        idsMov = DB.session.query(CDA003.id_movGere).filter(CDA003.mge_idFunc==idFunc)

        return idsMov
    

    def consultaMovAbertoGerente(self, id: int) -> CDA003:
        """
        Consulta um movimento de gerente aberto pelo seu ID.

        :param id: O ID do movimento de gerente que deseja consultar.

        :return: O objeto de movimento de gerente aberto correspondente ao ID fornecido.
        """

        movimento = CDA003.query.filter(CDA003.id_movGere==id, CDA003.mge_dataSaid==None, CDA003.mge_horaSaid==None).first()

        return movimento
    

    def consultaMovimentosRelatIdGerente(self, dataDe: str, dataAte: str, idFunc: int) -> CDA003:
        """
        Consulta os movimentos de um gerente específico que tem a data dentro do range passado.

        :param dataDe: A data início da consulta no formato YYYYMMDD.
        :param dataAte: A data final da consulta no formato YYYYMMDD.
        :param idFunc: Um ID de um gerente específico para consultar os movimentos.

        :return: Uma lista contendo as informações da cada movimento.
        """

        movimentos = CDA003.query.filter(CDA003.mge_dataEntra>=dataDe, CDA003.mge_dataEntra<=dataAte, CDA003.mge_horaSaid!=None, CDA003.mge_dataSaid!=None, CDA003.mge_idFunc==idFunc)\
            .join(CDA007, CDA007.id_funcionario==CDA003.mge_idFunc)\
                .order_by(CDA003.mge_dataEntra, CDA007.fu_nome, CDA003.mge_horaEntra)

        return movimentos
    

    def consultaMovimentosRelatGerente(self, dataDe: str, dataAte: str) -> CDA003:
        """
        Consulta os movimentos do gerentes que tem a data dentro do range passado.

        :param dataDe: A data início da consulta no formato YYYYMMDD.
        :param dataAte: A data final da consulta no formato YYYYMMDD.

        :return: Uma lista contendo as informações da cada movimento.
        """

        movimentos = CDA003.query.filter(CDA003.mge_dataEntra>=dataDe, CDA003.mge_dataEntra<=dataAte, CDA003.mge_horaSaid!=None, CDA003.mge_dataSaid!=None)\
            .join(CDA007, CDA007.id_funcionario==CDA003.mge_idFunc)\
                .order_by(CDA003.mge_dataEntra, CDA007.fu_nome, CDA003.mge_horaEntra)

        return movimentos