from ...models.entity.MovimentoTerceiro import MovimentoTerceiro
from ...models.entity.Terceiro import Terceiro
from ..Tables import CDA004, CDA007, CDA016
from ...configurations.Database import DB

"""
Classe Dao para funções do contole de terceiro
@tables - CDA004, CDA007, CDA016
@author - Fabio
@version - 1.0
@since - 10/07/2023
"""


class ControleTerceiroDao:


    def inserirEntrada(self, mov: MovimentoTerceiro) -> bool:
        movimento = CDA004(dataEntrada=mov.dataEnt, horaEntrada=mov.horaEnt, empresa=mov.empresa, veiculo=mov.veiculo,
                           placa=mov.placa, motivo=mov.motivo, detele=mov.delete, idFunc=mov.pessoaVisit.id)
        
        DB.session.add(movimento)
        DB.session.commit()
        return True
    

    def inserirSaida(self, mov: MovimentoTerceiro) -> bool:
        movimento = CDA004.query.get(mov.id)

        movimento.mte_dataSaid = mov.dataSai
        movimento.mte_horaSaid = mov.horaSai
        DB.session.commit()

        return True
    

    def inserirVisitante(self, terceiro: Terceiro, mov: MovimentoTerceiro) -> bool:
        visitante = CDA016(idTerc=terceiro.id, idMovTerc=mov.id)

        DB.session.add(visitante)
        DB.session.commit()
        return True


    def consultaTerceirosEntrada(self) -> CDA004:
        movimentos = DB.session\
            .query(CDA004.id_movTerc, CDA004.mte_dataEntra, CDA004.mte_horaEntra, CDA004.mte_empresa, CDA007.fu_nome.label("nomeFunc"))\
                .join(CDA007, CDA007.id_funcionarios == CDA004.mte_idFunc)\
                    .filter(CDA004.mte_dataSaid==None, CDA004.mte_horaSaid==None, CDA004.mte_delete!=True)
        
        return movimentos
    

    def consultaMovTercDetalhado(self, id: int) -> MovimentoTerceiro:
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
        movimento = CDA004.query.get(id)

        return movimento.mte_idFunc
    

    def consultaMovAbertoTerc(self, id: int) -> CDA004:
        movimento = CDA004.query.filter(CDA004.id_movTerc==id, CDA004.mte_dataSaid==None, CDA004.mte_horaSaid==None).first()

        return movimento