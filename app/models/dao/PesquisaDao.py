from ..Tables import CDA005, CDA007, CDA002, CDA009, SysUser
from ldap3 import Server, Connection, SAFE_SYNC, SUBTREE

"""
Classe Dao para pesquisas do sistema
@tables - CDA005, CDA007, CDA002, CDA009, SysUser
@author - Fabio
@version - 1.0
@since - 05/06/2023
"""

class PesquisaDao:

    def pesquisaChaveNomeDao(self, nome: str) -> CDA005:
        chaves = CDA005.query.filter(CDA005.ch_nome.like(f"%{nome}%"), CDA005.ch_delete!=True, CDA005.ch_ativo!=True)

        return chaves
    

    def pesquisaChaveCodigoDao(self, codigo: str) -> CDA005:
        chaves = CDA005.query.filter(CDA005.ch_codigo.like(f"%{codigo}%"), CDA005.ch_delete!=True, CDA005.ch_ativo!=True)

        return chaves
    

    def pesquisaFuncNomeChaveDao(self, nome: str) -> CDA007:
        funcionarios = CDA007.query.filter(CDA007.fu_nome.like(f"%{nome}%"), CDA007.fu_delete!=True, CDA007.fu_ativo!=True)

        return funcionarios
    
    
    def pesquisaFuncCrachaChaveDao(self, cracha: str) -> CDA007:
        funcionarios = CDA007.query.filter(CDA007.fu_cracha.like(f"%{cracha}%"), CDA007.fu_delete!=True, CDA007.fu_ativo!=True)

        return funcionarios
    
    
    def pesquisaCpfTerc(self, cpf: str) -> CDA009:
        terceiros = CDA009.query.filter(CDA009.te_cpf.like(f"%{cpf}%"), CDA009.te_delete!=True, CDA009.te_ativo!=True)

        return terceiros
    

    def pesquisaCrachaFormDao(self, cracha: str, id: int) -> CDA007:
        crachaFunc = CDA007.query.filter(CDA007.fu_cracha==cracha, CDA007.id_funcionarios!=id).first()

        return crachaFunc
    
    
    def pesquisaMaquinasFormDao(self) -> list:
        conn = Connection(Server(''),
                            auto_bind=True,
                            user="{}\\{}".format("", ""),
                            password="",
                            auto_referrals=False)

        maquinas = conn.extend.standard.paged_search(f'', '(objectClass=computer)', attributes=['cn', 'givenName'])

        return maquinas
    

    def pesquisaUsuarioFormDao(self, usuario: str, id: int) -> SysUser:
        user = SysUser.query.filter(SysUser.us_usuario==usuario, SysUser.id!=id).first()

        return user
    

    def pesquisaChaveFormMovDao(self, codigo: str) -> CDA005:
        chave = CDA005.query.filter(CDA005.ch_codigo==codigo, CDA005.ch_delete!=True, CDA005.ch_ativo!=True).first()

        return chave
    

    def pesquisaFuncFormMovDao(self, cracha: str) -> CDA005:
        funcionario = CDA007.query.filter(CDA007.fu_cracha==cracha, CDA007.fu_delete!=True, CDA007.fu_ativo!=True).first()

        return funcionario
    

    def pesquisaChaveRetFormMovDao(self, id: int) -> CDA002:
        movimento = CDA002.query.filter(CDA002.mch_idChav==id, CDA002.mch_dataDev==None, CDA002.mch_horaDev==None, CDA002.mch_delete!=True).first()

        return movimento
    

    def pesquisaCpfTercFormMov(self, cpf: str) -> CDA009:
        terceiro = CDA009.query.filter(CDA009.te_cpf==cpf, CDA009.te_delete!=True, CDA009.te_ativo!=True).first()

        return terceiro
    

    def pesquisaGerNomeMoveDao(self, nome: str) -> CDA007:
        gerentes = CDA007.query.filter(CDA007.fu_nome.like(f"%{nome}%"), CDA007.fu_delete!=True, CDA007.fu_ativo!=True, CDA007.fu_gerente==True)

        return gerentes
    
    
    def pesquisaGerCrachaMoveDao(self, cracha: str) -> CDA007:
        gerentes = CDA007.query.filter(CDA007.fu_cracha.like(f"%{cracha}%"), CDA007.fu_delete!=True, CDA007.fu_ativo!=True, CDA007.fu_gerente==True)

        return gerentes