from ..entity.MovimentoChave import MovimentoChave
from ..Tables import CDA001, CDA002, CDA005
from ...configurations.Database import DB
import sys

class ControleChaveDao:

    def inserirRetirada(self, movimento: MovimentoChave) -> bool:
        movimentoRet = CDA002(dataRet=movimento.dataRet, horaRet=movimento.horaRet,
                              delete=movimento.delete, idChave=movimento.chave.id)
        
        DB.session.add(movimentoRet)
        DB.session.commit()
        return True
        
    
    def consultaChavesRetiradas(self) -> CDA002:
        chavesRetiradas = CDA002.query.filter(CDA002.mch_dataDev=="", CDA002.mch_horaDev=="")

        return chavesRetiradas