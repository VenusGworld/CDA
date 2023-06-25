from ..Tables import CDA005, CDA007

class PesquisaDao:

    def pesquisaChaveNome(self, nome: str) -> CDA005:
        chaves = CDA005.query.filter(CDA005.ch_nome.like(f"%{nome}%"), CDA005.ch_delete!=True)

        return chaves
    

    def pesquisaChaveCodigo(self, codigo: str) -> CDA005:
        chaves = CDA005.query.filter(CDA005.ch_codigo.like(f"%{codigo}%"), CDA005.ch_delete!=True)

        return chaves
    

    def pesquisaFuncNomeChave(self, nome: str) -> CDA007:
        funcionarios = CDA007.query.filter(CDA007.fu_nome.like(f"%{nome}%"), CDA007.fu_delete!=True, CDA007.fu_ativo!=True)

        return funcionarios
    
    
    def pesquisaFuncCrachaChave(self, cracha: str) -> CDA007:
        funcionarios = CDA007.query.filter(CDA007.fu_cracha.like(f"%{cracha}%"), CDA007.fu_delete!=True, CDA007.fu_ativo!=True)

        return funcionarios