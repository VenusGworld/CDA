from .ManterFuncionarioDao import ManterFuncionarioDao
from ..entity.MovimentoChave import MovimentoChave
from ..Tables import CDA002, CDA005, CDA007
from .ManterChaveDao import ManterChaveDao
from ...configurations.Database import DB

"""
Classe Dao para funções do contole de chave
@tables - CDA002, CDA005, CDA007
@author - Fabio
@version - 1.0
@since - 10/07/2023
"""

class ControleChaveDao:

    def inserirRetirada(self, movimento: MovimentoChave) -> bool:
        movimentoRet = CDA002(dataRet=movimento.dataRet, horaRet=movimento.horaRet,
                              delete=movimento.delete, idChave=movimento.chave.id,
                              idFunc=movimento.respRet.id)
        
        DB.session.add(movimentoRet)
        DB.session.commit()
        return True
    

    def inserirDevolucao(self, movimento: MovimentoChave) -> bool:
        movimentoDev = CDA002.query.get(movimento.id)
        
        movimentoDev.mch_dataDev = movimento.dataDev
        movimentoDev.mch_horaDev = movimento.horaDev
        movimentoDev.mch_respDev = movimento.respDev.id
       

        DB.session.commit()
        return True

    
    def consultaMovimentoChaveDetalhado(self, id: int) -> MovimentoChave:
        manterFuncionarioDao = ManterFuncionarioDao()
        manterChaveDao = ManterChaveDao()
        movimento = CDA002.query.get(id)

        mov = MovimentoChave()
        mov.id = movimento.id_movChave
        mov.dataRet = movimento.mch_dataRet
        mov.horaRet = movimento.mch_horaRet
        mov.respRet = manterFuncionarioDao.mostarFuncionarioDetalhado(movimento.mch_respRet)
        mov.dataDev = movimento.mch_dataDev
        mov.horaDev = movimento.mch_horaDev
        mov.respDev = manterFuncionarioDao.mostarFuncionarioDetalhado(movimento.mch_respDev)
        mov.delete = movimento.mch_delete
        mov.chave = manterChaveDao.mostrarChaveDetalhadaId(movimento.mch_idChav)
        
        return mov


    def consultaChavesRetiradas(self) -> CDA002:
        chavesRetiradas = DB.session\
            .query(CDA002.id_movChave, CDA002.mch_horaRet, CDA002.mch_dataRet, CDA002.mch_respRet, CDA005.ch_nome.label("nomeChave"), CDA007.fu_nome.label("nomeResp"))\
            .join(CDA005, CDA005.id_chave == CDA002.mch_idChav).join(CDA007, CDA007.id_funcionarios == CDA002.mch_respRet)\
                .filter(CDA002.mch_dataDev==None, CDA002.mch_horaDev==None, CDA002.mch_delete!=True)
       
        return chavesRetiradas
    

    def consultaChavesManut(self) -> CDA002:
        chavesRetiradas = DB.session\
            .query(CDA002.id_movChave, CDA002.mch_horaRet, CDA002.mch_dataRet, CDA002.mch_respRet, CDA002.mch_dataDev, CDA002.mch_horaDev, CDA005.ch_nome.label("nomeChave"), CDA007.fu_nome.label("nomeResp"))\
            .join(CDA005, CDA005.id_chave == CDA002.mch_idChav).join(CDA007, CDA007.id_funcionarios == CDA002.mch_respRet)\
                .filter(CDA002.mch_dataDev!=None, CDA002.mch_horaDev!=None, CDA002.mch_delete!=True)
       
        return chavesRetiradas
    

    def verificaMovAbertoChave(self, idChave: int) -> CDA002:
        idsMov = DB.session.query(CDA002.id_movChave).filter(CDA002.mch_idChav==idChave)

        return idsMov
    

    def consultaMovAbertoChave(self, id: int) -> CDA002:
        movimento = CDA002.query.filter(CDA002.id_movChave==id, CDA002.mch_dataDev==None, CDA002.mch_horaDev==None).first()

        return movimento