from ...models.entity.MovimentoTerceiro import MovimentoTerceiro
from ...models.entity.Terceiro import Terceiro
from ..Tables import CDA004, CDA007, CDA016
from ...configurations.Database import DB

class ControleTerceiroDao:
    """
    Classe Dao para funções do contole de terceiro
    @tables - CDA004, CDA007, CDA016
    @author - Fabio
    @version - 1.0
    @since - 10/07/2023
    """

    def inserirEntrada(self, mov: MovimentoTerceiro) -> bool:
        """
        Insere um novo registro de entrada de terceiro no banco de dados.

        :param mov: Objeto de MovimentoTerceiro contendo as informações do movimento de entrada.

        :return: True se o registro for inserido com sucesso, False caso contrário.
        """
        
        movimento = CDA004(dataEntrada=mov.dataEnt, horaEntrada=mov.horaEnt, empresa=mov.empresa, veiculo=mov.veiculo,
                           placa=mov.placa, motivo=mov.motivo, detele=mov.delete, idFunc=mov.pessoaVisit.id)
        
        DB.session.add(movimento)
        DB.session.commit()
        return True
    

    def inserirSaida(self, mov: MovimentoTerceiro) -> bool:
        """
        Insere um registro de saída para um movimento de terceiro na base de dados.

        :param mov: Objeto de MovimentoTerceiro contendo as informações da saída do movimento.

        :return: True se a atualização for bem-sucedida, False caso contrário.
        """
        
        movimento = CDA004.query.get(mov.id)

        movimento.mte_dataSaid = mov.dataSai
        movimento.mte_horaSaid = mov.horaSai
        DB.session.commit()

        return True
    

    def inserirVisitante(self, terceiro: Terceiro, mov: MovimentoTerceiro) -> bool:
        """
        Insere um registro de visitante associado a um movimento de terceiro no banco de dados.

        :param terceiro: Objeto de Terceiro contendo as informações do terceiro envolvido no movimento.
        :param mov: Objeto de MovimentoTerceiro contendo as informações do movimento de terceiro.

        :return: True se a inserção for bem-sucedida, False caso contrário.
        """
        
        visitante = CDA016(idTerc=terceiro.id, idMovTerc=mov.id)

        DB.session.add(visitante)
        DB.session.commit()
        return True


    def consultaTerceirosEntrada(self) -> CDA004:
        """
        Consulta os movimentos de entrada de terceiros não finalizados no banco de dados.

        :return: Um conjunto de resultados que contém informações sobre os movimentos de entrada de terceiros não finalizados.
        """
        
        movimentos = DB.session\
            .query(CDA004.id_movTerc, CDA004.mte_dataEntra, CDA004.mte_horaEntra, CDA004.mte_empresa, CDA007.fu_nome.label("nomeFunc"))\
                .join(CDA007, CDA007.id_funcionario == CDA004.mte_idFunc)\
                    .filter(CDA004.mte_dataSaid==None, CDA004.mte_horaSaid==None, CDA004.mte_delete!=True)
        
        return movimentos
    

    def consultaMovTercDetalhado(self, id: int) -> MovimentoTerceiro:
        """
        Consulta detalhes de um movimento de entrada e saída de terceiro.

        :param id: O ID do movimento de entrada e saída de terceiro.

        :return: Um objeto MovimentoTerceiro contendo informações detalhadas do movimento.
        """

        mov = CDA004.query.get(id)

        movimento = MovimentoTerceiro(id=mov.id_movTerc, dataEnt=mov.mte_dataEntra, horaEnt=mov.mte_horaEntra, empresa=mov.mte_empresa, veiculo=mov.mte_veiculo,
                                      placa=mov.mte_placa, motivo=mov.mte_motivo, dataSai=mov.mte_dataSaid, horaSai=mov.mte_horaSaid, delete=mov.mte_delete)

        return movimento
    
    
    def consultaIdFuncMovTerc(self, id: int) -> int:
        """
        Consulta o ID do funcionário associado a um movimento de entrada e saída de terceiro.

        :param id: O ID do movimento de entrada e saída de terceiro.

        :return: O ID do funcionário associado ao movimento.
        """

        movimento = CDA004.query.get(id)

        return movimento.mte_idFunc
    

    def consultaMovAbertoTerc(self, id: int) -> CDA004:
        """
        Consulta um movimento de terceiro aberto com base no ID fornecido.

        :param id: O ID do movimento de terceiro.

        :return: O movimento de terceiro aberto.
        """

        movimento = CDA004.query.filter(CDA004.id_movTerc==id, CDA004.mte_dataSaid==None, CDA004.mte_horaSaid==None).first()

        return movimento
    

    def listaTercManut(self, data: str) -> CDA004:
        """
        Consulta os registros de movimento de terceiros com entrada e saída (completos) para manutenções.

        :return: Uma consulta que retorna os registros de movimento de terceiros para a manutenção.
        """
        
        movimentos = DB.session.query(CDA004.id_movTerc, CDA004.mte_dataEntra, CDA004.mte_horaEntra, CDA004.mte_dataSaid, CDA004.mte_horaSaid, CDA004.mte_motivo, CDA004.mte_empresa, CDA007.fu_nome.label("nomeFunc"))\
            .join(CDA007, CDA007.id_funcionario == CDA004.mte_idFunc)\
                .filter(CDA004.mte_dataSaid!=None, CDA004.mte_horaSaid!=None, CDA004.mte_delete!=True, CDA004.mte_dataEntra>=data)
        
        return movimentos
    

    def editarMovimentoTerceiro(self, movimento: MovimentoTerceiro) -> bool:
        """
        Altera os dados de um movimento de terceiro específico.

        :param movimento: Um objeto da classe MovimentoTerceiro contendo as informações para a alteração.
        
        :return: True se a edição for bem-sucedida, False caso contrário.
        """

        #Campos a serem atualizados
        campos = {
            "mte_dataEntra": movimento.dataEnt,
            "mte_horaEntra": movimento.horaEnt,
            "mte_dataSaid": movimento.dataSai,
            "mte_horaSaid": movimento.horaSai
        }

        CDA004.query.filter(CDA004.id_movTerc==movimento.id).update(campos)
        DB.session.commit()

        return True
    

    def excluirMovimentoTerceiro(self, movimento: MovimentoTerceiro) -> bool:
        """
        Marca um movimento de terceiro como excluido no sistema.

        :param movimento: Um objeto da classe MovimentoTerceiro contando o ID do movimento de terceiro a ser excluido.

        :return: True se a inativação for bem-sucedida, False caso contrário.
        """

        #Campos a serem atualizados
        campos = {
            "mte_delete": True
        }

        CDA004.query.filter(CDA004.id_movTerc==movimento.id).update(campos)
        DB.session.commit()

        return True
    

    def verificaMovIdFuncionario(self, idFunc: int) -> CDA004:
        """
        Verifica se existem movimentos de terceiros abertos associados a uma gerente específico.

        :param idFunc: O ID do gerente para a qual deseja verificar a existência de movimentos abertos.

        :return: Um objeto de consulta contendo os IDs dos movimentos de terceiros abertos associados ao gerente fornecida.
        """

        idsMov = DB.session.query(CDA004.id_movTerc).filter(CDA004.mte_idFunc==idFunc)

        return idsMov
    

    def consultaMovimentosRelatIdTerc(self, dataDe: str, dataAte: str, idTerc: int) -> CDA004:
        """
        Consulta os movimentos de um terceiros específico que tem a data dentro do range passado.

        :param dataDe: A data início da consulta no formato YYYYMMDD.
        :param dataAte: A data final da consulta no formato YYYYMMDD.
        :param idTerc: Um ID de um terceiro específico para consultar os movimentos.

        :return: Uma lista contendo as informações da cada movimento.
        """

        movimentos = CDA004.query.filter(CDA004.mte_dataEntra>=dataDe, CDA004.mte_dataEntra<=dataAte, CDA004.mte_dataSaid!=None, CDA004.mte_dataSaid!=None, CDA016.id_terceiro==idTerc)\
            .join(CDA016, CDA016.id_terceiro==idTerc)\
                .order_by(CDA004.mte_dataEntra)

        return movimentos
    

    def consultaMovimentosRelatTerceiro(self, dataDe: str, dataAte: str) -> CDA004:
        """
        Consulta os movimentos do terceiros que tem a data dentro do range passado.

        :param dataDe: A data início da consulta no formato YYYYMMDD.
        :param dataAte: A data final da consulta no formato YYYYMMDD.

        :return: Uma lista contendo as informações da cada movimento.
        """

        movimentos = CDA004.query.filter(CDA004.mte_dataEntra>=dataDe, CDA004.mte_dataEntra<=dataAte, CDA004.mte_dataSaid!=None, CDA004.mte_dataSaid!=None)\
            .order_by(CDA004.mte_dataEntra)

        return movimentos


