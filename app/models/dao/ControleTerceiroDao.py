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
                .join(CDA007, CDA007.id_funcionarios == CDA004.mte_idFunc)\
                    .filter(CDA004.mte_dataSaid==None, CDA004.mte_horaSaid==None, CDA004.mte_delete!=True)
        
        return movimentos
    

    def consultaMovTercDetalhado(self, id: int) -> MovimentoTerceiro:
        """
        Consulta detalhes de um movimento de entrada e saída de terceiro.

        :param id: O ID do movimento de entrada e saída de terceiro.

        :return: Um objeto MovimentoTerceiro contendo informações detalhadas do movimento.
        """

        movimento = CDA004.query.get(id)

        mov = MovimentoTerceiro()
        mov.id = movimento.id_movTerc
        mov.dataEnt = movimento.mte_dataEntra
        mov.horaEnt = movimento.mte_horaEntra
        mov.empresa = movimento.mte_empresa
        mov.veiculo = movimento.mte_veiculo
        mov.placa = movimento.mte_placa
        mov.motivo = movimento.mte_motivo
        mov.dataSai = movimento.mte_dataSaid
        mov.horaSai = movimento.mte_horaSaid
        mov.delete = movimento.mte_delete

        return mov
    
    
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