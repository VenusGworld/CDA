from ..models.dao.PesquisaDao import PesquisaDao
from ..models.dao.ManterChaveDao import ManterChaveDao

class ControlePesquisa:

    def pesquisaChave(self, pesquisa: str) -> list[dict]:
        pesquisaDao = PesquisaDao()
        listaChave = []
        if pesquisa[0:3] in ["CH0", "CH1", "CH2", "CH3", "CH4", "CH5", "CH6", "CH7", "CH8", "CH9"] or pesquisa[0:2] == "CH":
            respDao = pesquisaDao.pesquisaChaveCodigoDao(pesquisa)
            for chave in respDao:
                dictChave = {"chave": f"{chave.ch_codigo} - {chave.ch_nome}"}
                listaChave.append(dictChave)
            return listaChave
        else:
            respDao = pesquisaDao.pesquisaChaveNomeDao(pesquisa)
            for chave in respDao:
                dictChave = {"chave": f"{chave.ch_codigo} - {chave.ch_nome}"}
                listaChave.append(dictChave)
            return listaChave
      
        
    def pesquisaFuncionario(self, pesquisa: str) -> list[dict]:
        pesquisaDao = PesquisaDao()
        listaFuncionarios = []
        if pesquisa.isdigit():
            respDao = pesquisaDao.pesquisaFuncCrachaChaveDao(pesquisa)
            for funcionario in respDao:
                dictFunc = {"funcionario": f"{funcionario.fu_cracha} - {funcionario.fu_nome}"}
                listaFuncionarios.append(dictFunc)
            return listaFuncionarios
        else:
            respDao = pesquisaDao.pesquisaFuncNomeChaveDao(pesquisa)
            for funcionario in respDao:
                dictFunc = {"funcionario": f"{funcionario.fu_cracha} - {funcionario.fu_nome}"}
                listaFuncionarios.append(dictFunc)
            return listaFuncionarios


    def pesquisaCracha(self, pesquisa: str, id: int) -> bool:
        pesquisaDao = PesquisaDao()
        if pesquisaDao.pesquisaCrachaFormDao(pesquisa, id):
            return True
        else:
            return False
       
        
    def pesquisaMaquina(self, pesquisa: str) -> bool:
        pesquisaDao = PesquisaDao()
        listaMaquinas = pesquisaDao.pesquisaMaquinasFormDao()
        maquinaExiste = 0
        for maquina in listaMaquinas:
            if maquina["attributes"]["cn"] == pesquisa:
                maquinaExiste = 1
        
        if maquinaExiste == 1:
            return True
        else:
            return False
        

    def pesquisaUsuario(self, pesquisa: str, id: int) -> bool:
        pesquisaDao = PesquisaDao()
        if pesquisaDao.pesquisaUsuarioFormDao(pesquisa, id):
            return True
        else:
            return False
        

    def pesquisaChaveFormMov(self, pesquisa: str) -> bool:
        pesquisaDao = PesquisaDao()
        if pesquisaDao.pesquisaChaveFormMovDao(pesquisa):
            return True
        else:
            return False
        

    def pesquisaFuncFormMov(self, pesquisa: str) -> bool:
        pesquisaDao = PesquisaDao()
        if pesquisaDao.pesquisaFuncFormMovDao(pesquisa):
            return True
        else:
            return False
        

    def pesquisaChaveRetFormMov(self, pesquisa: str) -> bool:
        manterchaveDao = ManterChaveDao()
        chave = manterchaveDao.mostrarChaveDetalhadaCodigo(pesquisa)
        pesquisaDao = PesquisaDao()
        if pesquisaDao.pesquisaChaveRetFormMovDao(chave.id):
            return False
        else:
            return True