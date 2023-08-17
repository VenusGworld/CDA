from ..models.dao.ManterChaveDao import ManterChaveDao
from ..models.dao.ManterFuncionarioDao import ManterFuncionarioDao
from ..models.dao.PesquisaDao import PesquisaDao
from ..extensions.FiltrosJson import filtroCpf

"""
Classe Controller para as pesquisas do sistema
@author - Fabio
@version - 1.0
@since - 20/06/2023
"""

class ControlePesquisa:

    def pesquisaChave(self, pesquisa: str) -> list[dict]:
        #########################################################################################
        # Essa função recebe uma string para pesquisa de chaves no input, ela verifica
        # se o que foi digitado o código retorna a(s) chave(s) correspondente(s) ao código, se foi o 
        # nome retorna a(s) chave(s) correspondente(s) ao nome.
        
        # PARAMETROS:
        #   pesquisa = Nome ou Código da chave que foi digitado no input.
        
        # RETORNOS:
        #   return listaChave = Retorna uma lista com dicionário contendo as chave(s) correspondente(s)
        #     a pesquisa.
        #########################################################################################

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
        #########################################################################################
        # Essa função recebe uma string para pesquisa de funcionários no input, se o que foi 
        # digitado for crácha retorna o(s) funcionário(s) correspondente(s) ao crácha, se foi o 
        # nome retorna o(s) funcionário(s) correspondente(s) ao nome.
        
        # PARAMETROS:
        #   pesquisa = Nome ou Crácha do funcionário que foi digitado no input.
        
        # RETORNOS:
        #   return listaFuncionarios = Retorna uma lista com dicionário contendo os funcionário(s) 
        #     correspondente(s) a pesquisa.
        #########################################################################################

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
        

    def pesquisaTerceiros(self, pesquisa: str) -> list[dict]:
        #########################################################################################
        # Essa função recebe uma string para pesquisa de funcionários no input, se o que foi 
        # digitado for crácha retorna o(s) funcionário(s) correspondente(s) ao crácha, se foi o 
        # nome retorna o(s) funcionário(s) correspondente(s) ao nome.
        
        # PARAMETROS:
        #   pesquisa = Nome ou Crácha do funcionário que foi digitado no input.
        
        # RETORNOS:
        #   return listaFuncionarios = Retorna uma lista com dicionário contendo os funcionário(s) 
        #     correspondente(s) a pesquisa.
        #########################################################################################

        pesquisaDao = PesquisaDao()
        listaCPFs = []
        pesquisa = ''.join(filter(str.isdigit, pesquisa))

        respDao = pesquisaDao.pesquisaCpfTerc(pesquisa)
        for terceiro in respDao:
            dictFunc = {"terceiro": f"{filtroCpf(terceiro.te_cpf)}"}
            
            listaCPFs.append(dictFunc)
        return listaCPFs


    def pesquisaCracha(self, pesquisa: str, id: int) -> bool:
        #########################################################################################
        # Essa função recebe um crácha que foi digitado e verifica se ele já está vinculado a um
        # funcionário.
        
        # PARAMETROS:
        #   pesquisa = Crácha do funcionário que foi digitado no input.
        
        # RETORNOS:
        #   return True = Retorna True caso o crácha já está vinculado;
        #   return False = Retorna False caso o crácha não esteja vinculado.
        #########################################################################################

        pesquisaDao = PesquisaDao()
        if pesquisaDao.pesquisaCrachaFormDao(pesquisa, id):
            return True
        else:
            return False
       
        
    def pesquisaMaquina(self, pesquisa: str) -> bool:
        #########################################################################################
        # Essa função recebe o nome da máquina que foi digitado e verifica se ela existe no AD
        # (se está no dóminio).
        
        # PARAMETROS:
        #   pesquisa = Nome da máquina que foi digitado no input.
        
        # RETORNOS:
        #   return True = Retorna True caso a máquina existe;
        #   return False = Retorna False caso a máquina não exista.
        #########################################################################################

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
        #########################################################################################
        # Essa função recebe um crácha que foi digitado e verifica se ele já está vinculado a um
        # funcionário.
        
        # PARAMETROS:
        #   pesquisa = Crácha do funcionário que foi digitado no input.
        
        # RETORNOS:
        #   return True = Retorna True caso o crácha já está vinculado;
        #   return False = Retorna False caso o crácha não esteja vinculado.
        #########################################################################################

        pesquisaDao = PesquisaDao()
        if pesquisaDao.pesquisaUsuarioFormDao(pesquisa, id):
            return True
        else:
            return False
        

    def pesquisaChaveFormMov(self, pesquisa: str) -> bool:
        #########################################################################################
        # Essa função recebe um código da chave que foi digitado e verifica se ela existe.
        
        # PARAMETROS:
        #   pesquisa = Código da chave que foi digitado no input.
        
        # RETORNOS:
        #   return True = Retorna True caso a chave exista;
        #   return False = Retorna False caso a chave não exista.
        #########################################################################################

        pesquisaDao = PesquisaDao()
        if pesquisaDao.pesquisaChaveFormMovDao(pesquisa):
            return True
        else:
            return False
        

    def pesquisaFuncFormMov(self, pesquisa: str) -> bool:
        #########################################################################################
        # Essa função recebe um crácha do funcionário que foi digitado e verifica se ele existe.
        
        # PARAMETROS:
        #   pesquisa = Crácha do funcionário que foi digitado no input.
        
        # RETORNOS:
        #   return True = Retorna True caso o funcionário exista;
        #   return False = Retorna False caso o funcionário não exista.
        #########################################################################################

        pesquisaDao = PesquisaDao()
        if pesquisaDao.pesquisaFuncFormMovDao(pesquisa):
            return True
        else:
            return False
        

    def pesquisaChaveRetFormMov(self, pesquisa: str) -> bool:
        #########################################################################################
        # Essa função recebe um código da chave que foi digitado e verifica se ela já foi devolvida.
        
        # PARAMETROS:
        #   pesquisa = Código da chave que foi digitado no input.
        
        # RETORNOS:
        #   return True = Retorna True caso a chave foi devolvida;
        #   return False = Retorna False caso a chave ainda não foi devolvida.
        #########################################################################################

        manterchaveDao = ManterChaveDao()
        chave = manterchaveDao.mostrarChaveDetalhadaCodigo(pesquisa)
        pesquisaDao = PesquisaDao()
        if pesquisaDao.pesquisaChaveRetFormMovDao(chave.id):
            return False
        else:
            return True
        

    def pesquisaTerceiroFormmov(self, pesquisa: str) -> dict:
        #########################################################################################
        # Essa função recebe uma string para pesquisa de funcionários no input, se o que foi 
        # digitado for crácha retorna o(s) funcionário(s) correspondente(s) ao crácha, se foi o 
        # nome retorna o(s) funcionário(s) correspondente(s) ao nome.
        
        # PARAMETROS:
        #   pesquisa = Nome ou Crácha do funcionário que foi digitado no input.
        
        # RETORNOS:
        #   return listaFuncionarios = Retorna uma lista com dicionário contendo os funcionário(s) 
        #     correspondente(s) a pesquisa.
        #########################################################################################

        pesquisaDao = PesquisaDao()
        respDao = pesquisaDao.pesquisaCpfTercFormMov(pesquisa)
        if respDao:
            dictFunc = {"nome": f"{respDao.te_nome}"}
            return dictFunc

        else:
            return {"nome": ""}
        

    def pesquisaGerente(self, pesquisa: str) -> list[dict]:
        #########################################################################################
        # Essa função recebe uma string para pesquisa de funcionários no input, se o que foi 
        # digitado for crácha retorna o(s) funcionário(s) correspondente(s) ao crácha, se foi o 
        # nome retorna o(s) funcionário(s) correspondente(s) ao nome.
        
        # PARAMETROS:
        #   pesquisa = Nome ou Crácha do funcionário que foi digitado no input.
        
        # RETORNOS:
        #   return listaFuncionarios = Retorna uma lista com dicionário contendo os funcionário(s) 
        #     correspondente(s) a pesquisa.
        #########################################################################################

        pesquisaDao = PesquisaDao()
        listaGerente = []
        if pesquisa.isdigit():
            respDao = pesquisaDao.pesquisaGerCrachaMoveDao(pesquisa)
            for gerente in respDao:
                dictGer = {"gerente": f"{gerente.fu_cracha} - {gerente.fu_nome}"}
                listaGerente.append(dictGer)
            return listaGerente
        else:
            respDao = pesquisaDao.pesquisaGerNomeMoveDao(pesquisa)
            for gerente in respDao:
                dictGer = {"gerente": f"{gerente.fu_cracha} - {gerente.fu_nome}"}
                listaGerente.append(dictGer)
            return listaGerente
            
        
    def pesquisaGerenteSaiFormMov(self, pesquisa: str) -> bool:
        #########################################################################################
        # Essa função recebe um código da chave que foi digitado e verifica se ela já foi devolvida.
        
        # PARAMETROS:
        #   pesquisa = Código da chave que foi digitado no input.
        
        # RETORNOS:
        #   return True = Retorna True caso a chave foi devolvida;
        #   return False = Retorna False caso a chave ainda não foi devolvida.
        #########################################################################################

        manterFuncionarioDao = ManterFuncionarioDao()
        gerente = manterFuncionarioDao.mostarFuncionarioDetalhadoCracha(pesquisa)
        pesquisaDao = PesquisaDao()
        if pesquisaDao.pesquisaGerenteSaiFormMovDao(gerente.id):
            return False
        else:
            return True
    