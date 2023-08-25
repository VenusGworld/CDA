from ..Tables import CDA013, CDA011, CDA001, CDA010, CDA012, CDA008, CDA006, CDA014
from ...configurations.Database import DB
from app.models.entity.Log import Log

class GeraLogDao:
    """
    Classe Dao para gerar log
    @tables - CDA013, CDA011, CDA001, CDA010, CDA012, CDA008, CDA006, CDA014
    @author - Fabio
    @version - 4.0
    @since - 05/06/2023
    """

    def inserirLogUsuario(self, log: Log) -> bool:
        """
        Insere um registro de log de usuário no banco de dados.

        :param log: Um objeto 'Log' contendo as informações do registro de log.
        
        :return: True se o log foi inserido com sucesso, False em caso de erro.
        """

        logUser = CDA013(dataHora=log.dataHora, acao=log.acao, 
                         dadosAntigos=log.converteBytesDadosAntigos(), 
                         dadosNovos=log.converteBytesDadosNovos(), idUsua=log.usuario.id)
        
        DB.session.add(logUser)
        DB.session.commit()
        return True
        

    def inserirLogFuncionario(self, log: Log) -> bool:
        """
        Insere um registro de log de funcionário no banco de dados.

        :param log: Um objeto 'Log' contendo as informações do registro de log.

        :return: True se o log foi inserido com sucesso, False em caso de erro.
        """

        logFunc = CDA011(dataHora=log.dataHora, acao=log.acao, 
                         dadosAntigos=log.converteBytesDadosAntigos(), 
                         dadosNovos=log.converteBytesDadosNovos(), idUsua=log.usuario.id)
    
        DB.session.add(logFunc)
        DB.session.commit()
        return True
    

    def inserirLogChave(self, log: Log) -> bool:
        """
        Insere um registro de log de chave no banco de dados.

        :param log: Um objeto 'Log' contendo as informações do registro de log.

        :return: True se o log foi inserido com sucesso, False em caso de erro.
        """

        logChave = CDA010(dataHora=log.dataHora, acao=log.acao, observacao=log.observacao, 
                         dadosAntigos=log.converteBytesDadosAntigos(), 
                         dadosNovos=log.converteBytesDadosNovos(), idUsua=log.usuario.id)
    
        DB.session.add(logChave)
        DB.session.commit()
        return True
    

    def inserirLogControleChave(self, log: Log) -> bool:
        """
        Insere um registro de log de controle de chaves no banco de dados.

        :param log: Um objeto 'Log' contendo as informações do registro de log.

        :return: True se o log foi inserido com sucesso, False em caso de erro.
        """

        logControleChave = CDA001(dataHora=log.dataHora, acao=log.acao, observacao=log.observacao, 
                         dadosAntigos=log.converteBytesDadosAntigos(), 
                         dadosNovos=log.converteBytesDadosNovos(), idUsua=log.usuario.id)
    
        DB.session.add(logControleChave)
        DB.session.commit()
        return True
    

    def inserirLogTerceiro(self, log: Log) -> bool:
        """
        Insere um registro de log de terceiro no banco de dados.

        :param log: Um objeto 'Log' contendo as informações do registro de log.

        :return: True se o log foi inserido com sucesso, False em caso de erro.
        """

        logTerc = CDA012(dataHora=log.dataHora, acao=log.acao, observacao=log.observacao, 
                         dadosAntigos=log.converteBytesDadosAntigos(), 
                         dadosNovos=log.converteBytesDadosNovos(), idUsua=log.usuario.id)
    
        DB.session.add(logTerc)
        DB.session.commit()
        return True
    

    def inserirLogControleTerceiro(self, log: Log) -> bool:
        """
        Insere um registro de log de controle de terceiro no banco de dados.

        :param log: Um objeto 'Log' contendo as informações do registro de log.

        :return: True se o log foi inserido com sucesso, False em caso de erro.
        """

        logControleTerc = CDA008(dataHora=log.dataHora, acao=log.acao, observacao=log.observacao, 
                         dadosAntigos=log.converteBytesDadosAntigos(), 
                         dadosNovos=log.converteBytesDadosNovos(), idUsua=log.usuario.id)
    
        DB.session.add(logControleTerc)
        DB.session.commit()
        return True
    

    def inserirLogControleGerente(self, log: Log) -> bool:
        """
        Insere um registro de log de controle de gerente no banco de dados.

        :param log: Um objeto 'Log' contendo as informações do registro de log.

        :return: True se o log foi inserido com sucesso, False em caso de erro.
        """

        logControleGer = CDA006(dataHora=log.dataHora, acao=log.acao, observacao=log.observacao, 
                         dadosAntigos=log.converteBytesDadosAntigos(), 
                         dadosNovos=log.converteBytesDadosNovos(), idUsua=log.usuario.id)
    
        DB.session.add(logControleGer)
        DB.session.commit()
        return True
    

    def inserirLogMensagem(self, log: Log) -> bool:
        """
        Insere um registro de log de mensagem no banco de dados.

        :param log: Um objeto 'Log' contendo as informações do registro de log.

        :return: True se o log foi inserido com sucesso, False em caso de erro.
        """

        logMensagem = CDA014(dataHora=log.dataHora, mensagem=log.observacao, idUsua=log.usuario.id)
    
        DB.session.add(logMensagem)
        DB.session.commit()
        return True
    

        
        