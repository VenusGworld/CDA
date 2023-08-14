from ..Tables import CDA013, CDA008, CDA012, CDA006, CDA011, CDA010, CDA001, CDA014, CDA002, CDA003, CDA016

"""
Classe Dao para verificar movimento do usuário no sistema
@tables - CDA013, CDA008, CDA012, CDA006, CDA011, CDA010, CDA001, CDA014, CDA002, CDA003, CDA016
@author - Fabio
@version - 1.0
@since - 07/06/2023
"""

class VerificaMovimentoDao:

    def verificaMovimentoUsuario(self, id: int) -> bool:
        #########################################################################################
        # Essa Função verifica nas tabelas de log se o usuário teve movimentação no sistema.
        
        # PARAMETROS:
        #   id = ID do usuário para consulta as tabelas.
        
        # RETORNOS:
        #   return True = Retorna True caso o usuário não tenha movimento;
        #   return False = Retorna False caso o usuário tenha movimento.
        #########################################################################################

        movimento = 0
        if CDA013.query.filter(CDA013.lus_idUsua==id).first():
            movimento += 1

        if CDA008.query.filter(CDA008.lmte_idUsua==id).first():
            movimento += 1

        if CDA012.query.filter(CDA012.lte_idUsua==id).first():
            movimento += 1

        if CDA006.query.filter(CDA006.lmge_idUsua==id).first():
            movimento += 1

        if CDA010.query.filter(CDA010.lch_idUsua==id).first():
            movimento += 1

        if CDA011.query.filter(CDA011.lfu_idUsua==id).first():
            movimento += 1

        if CDA014.query.filter(CDA014.lme_idUsua==id).first():
            movimento += 1

        if CDA001.query.filter(CDA001.lmch_idUsua==id).first():
            movimento += 1

        if movimento == 0:
            return False
        else:
            return True
        

    def verificaMovimentoFuncionario(self, id: int) -> bool:
        #########################################################################################
        # Essa Função consulta nas tabelas de movimento de gerentes e movimento de chaves para 
        # verificar se o funcionário teve movimentação no sistema.
        
        # PARAMETROS:
        #   id = ID do funcionário para consulta as tabelas.
        
        # RETORNOS:
        #   return True = Retorna True caso o funcionário não tenha movimento;
        #   return False = Retorna False caso o funcionário tenha movimento.
        #########################################################################################

        movimento = 0

        if CDA003.query.filter(CDA003.mge_idFunc==id).first():
            movimento += 1

        if CDA002.query.filter(CDA002.mch_respRet==id).first():
            movimento += 1

        if CDA002.query.filter(CDA002.mch_respDev==id).first():
            movimento += 1
        
        if movimento == 0:
            return False
        else:
            return True

    
    def verificaMovimentoChave(self, id: int) -> bool:
        #########################################################################################
        # Essa Função consulta na tabela de movimento de chaves para verificar se a chave teve 
        # movimentação no sistema.
        
        # PARAMETROS:
        #   id = ID do chave para consulta as tabelas.
        
        # RETORNOS:
        #   return True = Retorna True caso o chave não tenha movimento;
        #   return False = Retorna False caso o chave tenha movimento.
        #########################################################################################

        movimento = 0

        if CDA002.query.filter(CDA002.mch_idChav==id).first():
            movimento += 1


        if movimento == 0:
            return False
        else:
            return True
        

    def verificaMovimentoTerceiro(self, id: int) -> bool:
        #########################################################################################
        # Essa Função consulta na tabela de movimento de terceiros para verificar se o terceiro teve 
        # movimentação no sistema.
        
        # PARAMETROS:
        #   id = ID do tercerio para consulta as tabelas.
        
        # RETORNOS:
        #   return True = Retorna True caso o tercerio não tenha movimento;
        #   return False = Retorna False caso o tercerio tenha movimento.
        #########################################################################################

        movimento = 0

        if CDA016.query.filter(CDA016.id_terceiro==id).first():
            movimento += 1


        if movimento == 0:
            return False
        else:
            return True