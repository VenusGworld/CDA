from ..entity.MovimentoGerente import MovimentoGerente
from ...configurations.Database import DB
from ..Tables import CDA003, CDA007

"""
Classe Dao para funções do contole de Gerenete
@tables - CDA003
@author - Fabio
@version - 1.0
@since - 10/07/2023
"""

class ControleGerenteDao:

    def inserirEntrada(self, movimento: MovimentoGerente) -> bool:
        mov = CDA003(dataEntrada=movimento.dataEnt, horaEntrada=movimento.horaEnt,
                              delete=movimento.delete, idFunc=movimento.gerente.id)
        
        DB.session.add(mov)
        DB.session.commit()
        return True
    

    def inserirSaida(self, movimento: MovimentoGerente) -> bool:
        mov = CDA003.query.get(movimento.id)
        mov.mge_dataSaid = movimento.dataSai
        mov.mge_horaSaid = movimento.horaSai

        DB.session.commit()
        return True
    

    def consultaGerentesEntrada(self) -> CDA003:
        movimentos = DB.session.query(CDA003.id_movGere, CDA003.mge_dataEntra, CDA003.mge_horaEntra, CDA007.fu_nome.label("nomeGer"))\
            .join(CDA007, CDA007.id_funcionarios==CDA003.mge_idFunc)\
                .filter(CDA003.mge_dataSaid==None, CDA003.mge_horaSaid==None, CDA003.mge_delete!=True)
        
        return movimentos
    

    def consultaMovimentoDetalhado(self, id: int) -> MovimentoGerente:
        mov = CDA003.query.filter(CDA003.id_movGere==id).first()

        movimento = MovimentoGerente()
        movimento.id = mov.id_movGere
        movimento.dataEnt = mov.mge_dataEntra
        movimento.horaEnt = mov.mge_horaEntra
        movimento.dataSai = mov.mge_dataSaid
        movimento.horaSai = mov.mge_horaSaid
        movimento.delete = mov.mge_delete

        return movimento
    

    def consultaIdGerMov(self, id: int) -> int:
        mov = CDA003.query.filter(CDA003.id_movGere==id).first()

        return mov.mge_idFunc
    

    def consultaGerentesManut(self) -> CDA003:
        movimentos = DB.session.query(CDA003.id_movGere, CDA003.mge_dataEntra, CDA003.mge_horaEntra, CDA003.mge_dataSaid, CDA003.mge_horaSaid, CDA007.fu_nome.label("nomeGer"))\
            .join(CDA007, CDA007.id_funcionarios==CDA003.mge_idFunc)\
                .filter(CDA003.mge_dataSaid!=None, CDA003.mge_horaSaid!=None,CDA003.mge_delete!=True)
        
        return movimentos