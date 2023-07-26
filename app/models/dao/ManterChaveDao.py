from ..entity.Chave import Chave
from ..Tables import CDA005
from ...configurations.Database import DB

"""
Classe Dao para o manter Chave
@tables - CDA005
@author - Fabio
@version - 1.0
@since - 27/06/2023
"""


class ManterChaveDao:


    def mostraChaves(self) -> CDA005:
        chaves = CDA005.query.filter(CDA005.ch_delete!=True, CDA005.ch_ativo!=True)

        return chaves


    def mostrarChaveDetalhadaId(self, id: int) -> Chave:
        chave = CDA005.query.filter(CDA005.id_chave==id).first()

        chav = Chave()
        chav.id = chave.id_chave
        chav.codigo = chave.ch_codigo
        chav.nome = chave.ch_nome
        chav.ativo = chave.ch_ativo
        chav.delete = chave.ch_delete

        return chav
    

    def mostrarChaveDetalhadaCodigo(self, codigo: str) -> Chave:
        chave = CDA005.query.filter(CDA005.ch_codigo==codigo).first()

        chav = Chave()
        chav.id = chave.id_chave
        chav.codigo = chave.ch_codigo
        chav.nome = chave.ch_nome
        chav.ativo = chave.ch_ativo
        chav.delete = chave.ch_delete

        return chav


    def consultaUltimoCodigo(self) -> str:
        codigo = DB.session.query(CDA005.ch_codigo).order_by(CDA005.ch_codigo.desc()).first()
        
        return codigo


    def incluirChave(self, chave: Chave) -> bool:
        chav = CDA005(codigo=chave.codigo, nome=chave.nome, 
                      ativo=chave.ativo, delete=chave.delete)
        
        DB.session.add(chav)
        DB.session.commit()

        return True
    
    def editarChave(self, chave: Chave) -> bool:
        chav = CDA005.query.get(chave.id)

        chav.ch_nome = chave.nome
        DB.session.commit()

        return True

    def excuirChave(self, id: int) -> bool:
        chave = CDA005.query.get(id)

        chave.ch_delete = True
        DB.session.commit()

        return True


    def inativarChave(self, id: int) -> bool:
        chave = CDA005.query.get(id)

        chave.ch_ativo = True
        DB.session.commit()
        
        return True
    

    def consultaUltimoId(self) -> int:
        id = DB.session.query(CDA005.id_chave).order_by(CDA005.id_chave.desc()).first()

        return id[0]