from ..models.dao.PesquisaDao import PesquisaDao


class ControlePesquisa:

    def pesquisaChave(self, pesquisa: str) -> list[dict]:
        controleChaveDao = PesquisaDao()
        listaChave = []
        if pesquisa[0:3] in ["CH0", "CH1", "CH2", "CH3", "CH4", "CH5", "CH6", "CH7", "CH8", "CH9"] or pesquisa[0:2] == "CH":
            respDao = controleChaveDao.pesquisaChaveCodigo(pesquisa)
            for chave in respDao:
                dictChave = {"chave": f"{chave.ch_codigo} - {chave.ch_nome}"}
                listaChave.append(dictChave)
            return listaChave
        else:
            respDao = controleChaveDao.pesquisaChaveNome(pesquisa)
            for chave in respDao:
                dictChave = {"chave": f"{chave.ch_codigo} - {chave.ch_nome}"}
                listaChave.append(dictChave)
            return listaChave
      
        
    def pesquisaFuncionario(self, pesquisa: str) -> list[dict]:
        controleChaveDao = PesquisaDao()
        listaFuncionarios = []
        if pesquisa.isdigit():
            respDao = controleChaveDao.pesquisaFuncCrachaChave(pesquisa)
            for funcionario in respDao:
                dictFunc = {"funcionario": f"{funcionario.fu_cracha} - {funcionario.fu_nome}"}
                listaFuncionarios.append(dictFunc)
            return listaFuncionarios
        else:
            respDao = controleChaveDao.pesquisaFuncNomeChave(pesquisa)
            for funcionario in respDao:
                dictFunc = {"funcionario": f"{funcionario.fu_cracha} - {funcionario.fu_nome}"}
                listaFuncionarios.append(dictFunc)
            return listaFuncionarios