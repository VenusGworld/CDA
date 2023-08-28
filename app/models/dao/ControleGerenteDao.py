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

        mov = CDA003.query.get(movimento.id)
        mov.mge_dataSaid = movimento.dataSai
        mov.mge_horaSaid = movimento.horaSai

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
    

    def consultaGerentesManut(self) -> CDA003:
        """
        Consulta os registros de movimento de gerentes com entrada e saída (completos) para manutenções.

        :return: Uma consulta que retorna os registros de movimento de gerentes para a manutenção.
        """
        
        movimentos = DB.session.query(CDA003.id_movGere, CDA003.mge_dataEntra, CDA003.mge_horaEntra, CDA003.mge_dataSaid, CDA003.mge_horaSaid, CDA007.fu_nome.label("nomeGer"))\
            .join(CDA007, CDA007.id_funcionario==CDA003.mge_idFunc)\
                .filter(CDA003.mge_dataSaid!=None, CDA003.mge_horaSaid!=None,CDA003.mge_delete!=True)
        
        return movimentos