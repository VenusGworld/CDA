from ..Tables import CDA013, CDA008, CDA012, CDA006, CDA011, CDA010, CDA001, CDA014, CDA002, CDA003, CDA016, CDA004

class VerificaMovimentoDao:
    """
    Classe Dao para verificação de moimentações no sistema.
    @tables - CDA013, CDA008, CDA012, CDA006, CDA011, CDA010, CDA001, CDA014, CDA002, CDA003, CDA016, CDA004
    @author - Fabio
    @version - 1.0
    @since - 07/06/2023
    """

    def verificaMovimentoUsuario(self, id: int) -> bool:
        """
        Esta função verifica se um usuário tem movimentos registrados em diferentes tipos de movimentos,
        como movimentos de chaves, movimentos de terceiros, etc. Ela percorre várias tabelas de movimentos
        (CDA013, CDA008, CDA012, etc.) e verifica se existe algum registro associado ao usuário com o ID fornecido.
        Se pelo menos um registro for encontrado em qualquer uma das tabelas, a função retorna True, indicando que
        o usuário possui movimentos registrados. Caso contrário, retorna False.

        :param id: O ID do usuário a ser verificado.

        :return: True se o usuário possui movimentos registrados, False caso contrário.
        """

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
        """
        Esta função verifica se um funcionário tem movimentos registrados em diferentes tipos de movimentos,
        como movimentos de chaves, movimentos de gerentes e movimento de terceiro. Ela percorre várias tabelas de movimentos
        (CDA003, CDA002, CDA004) e verifica se existe algum registro associado ao funcionário com o ID fornecido.
        Se pelo menos um registro for encontrado em qualquer uma das tabelas, a função retorna True, indicando que
        o funcionário possui movimentos registrados. Caso contrário, retorna False.

        :param id: O ID do funcionário a ser verificado.

        :return: True se o funcionário possui movimentos registrados, False caso contrário.
        """

        movimento = 0

        if CDA003.query.filter(CDA003.mge_idFunc==id).first():
            movimento += 1

        #Verifica se o funcionário foi responsável pele retirada da chave
        if CDA002.query.filter(CDA002.mch_respRet==id).first():
            movimento += 1

        #Verifica se o funcionário foi responsável pele devolução da chave
        if CDA002.query.filter(CDA002.mch_respDev==id).first():
            movimento += 1

        if CDA004.query.filter(CDA004.mte_idFunc==id).first():
            movimento += 1
        
        if movimento == 0:
            return False
        else:
            return True

    
    def verificaMovimentoChave(self, id: int) -> bool:
        """
        Esta função verifica se uma chave tem movimentos registrados na tabela CDA002 (tabela de movimentos de chave).
        Ela verifica se existe algum registro associado à chave com o ID fornecido na tabela de movimentos de chave.
        Se pelo menos um registro for encontrado, a função retorna True, indicando que a chave possui movimentos registrados.
        Caso contrário, retorna False.

        :param id: O ID da chave a ser verificada.

        :return: True se a chave possui movimentos registrados, False caso contrário.
        """

        movimento = 0

        if CDA002.query.filter(CDA002.mch_idChav==id).first():
            movimento += 1

        if movimento == 0:
            return False
        else:
            return True
        

    def verificaMovimentoTerceiro(self, id: int) -> bool:
        """
        Esta função verifica se um terceiro tem movimentos registrados na tabela CDA016 (tabela de relação entre terceiros e movimentos de terceiros).
        Ela verifica se existe algum registro associado ao terceiro com o ID fornecido na tabela de relação de movimentos de terceiros.
        Se pelo menos um registro for encontrado, a função retorna True, indicando que o terceiro possui movimentos registrados.
        Caso contrário, retorna False.

        :param id: O ID do terceiro a ser verificado.
        :return: True se o terceiro possui movimentos registrados, False caso contrário.
        """

        movimento = 0

        if CDA016.query.filter(CDA016.id_terceiro==id).first():
            movimento += 1

        if movimento == 0:
            return False
        else:
            return True