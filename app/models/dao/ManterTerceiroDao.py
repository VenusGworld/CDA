from ...configurations.Database import DB
from ..entity.Terceiro import Terceiro
from ..Tables import CDA009, CDA016


"""
Classe Dao para o manter Tereceiro
@tables - CDA009, CDA016
@author - Fabio
@version - 1.0
@since - 26/07/2023
"""


class ManterTerceiroDao:

    def mostarTerceiros(self) -> CDA009:
        terceiros = CDA009.query.filter(CDA009.te_delete!=True, CDA009.te_ativo!=True).order_by(CDA009.te_nome)

        return terceiros
    

    def mostrarTerceiroDetalhadoCpf(self, cpf: str) -> Terceiro:
        terceiro = CDA009.query.filter(CDA009.te_cpf==cpf, CDA009.te_delete!=True, CDA009.te_ativo!=True).first()

        terceiroMov = Terceiro()
        terceiroMov.id = terceiro.id_terceiro
        terceiroMov.codigo = terceiro.te_codigo
        terceiroMov.nome = terceiro.te_nome
        terceiroMov.cpf = terceiro.te_cpf
        terceiroMov.ativo = terceiro.te_ativo
        terceiroMov.delete = terceiro.te_delete

        return terceiroMov
    

    def mostrarTerceiroDetalhadoId(self, id: int) -> Terceiro:
        terceiro = CDA009.query.filter(CDA009.id_terceiro==id, CDA009.te_delete!=True, CDA009.te_ativo!=True).first()

        terceiroMov = Terceiro()
        terceiroMov.id = terceiro.id_terceiro
        terceiroMov.codigo = terceiro.te_codigo
        terceiroMov.nome = terceiro.te_nome
        terceiroMov.cpf = terceiro.te_cpf
        terceiroMov.ativo = terceiro.te_ativo
        terceiroMov.delete = terceiro.te_delete

        return terceiroMov
    

    def incluirTerceiro(self, tereceiro: Terceiro) -> bool:
        terc = CDA009(codigo=tereceiro.codigo, nome=tereceiro.nome, 
                      cpf=tereceiro.cpf, ativo=tereceiro.ativo, 
                      delete=tereceiro.delete)
        
        DB.session.add(terc)
        DB.session.commit()

        return True
    

    def editarTerceiro(self, terceiro: Terceiro) -> bool:
        terc = CDA009.query.get(terceiro.id)

        terc.te_nome = terceiro.nome
        DB.session.commit()

        return True
    
    def inativarTerceiro(self, id: int) -> bool:
        terc = CDA009.query.get(id)

        terc.te_ativo = True
        DB.session.commit()

        return True
    

    def excluirTerceiro(self, id: int) -> bool:
        terc = CDA009.query.get(id)

        terc.te_delete = True
        DB.session.commit()

        return True
    

    def verificaMovAbertoTerceiro(self, id: int) -> CDA016:
        idsMov = DB.session.query(CDA016.id_movTerc).filter(CDA016.id_terceiro==id)

        return idsMov
    

    def consultaTerceiro(self, idMov: int) -> CDA009:
        terceiro = DB.session.query(CDA009.te_nome)\
            .join(CDA016, CDA016.id_terceiro==CDA009.id_terceiro)\
                .filter(CDA009.te_delete!=True, CDA016.id_movTerc==idMov).first()

        return terceiro