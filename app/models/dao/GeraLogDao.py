from ..Tables import CDA013, CDA011, CDA001, CDA010, CDA012, CDA008, CDA006
from ...configurations.Database import DB
from app.models.entity.Log import Log

"""
Classe Dao para gerar log
@tables - CDA013, CDA011, CDA001, CDA010, CDA012, CDA008, CDA006
@author - Fabio
@version - 4.0
@since - 05/06/2023
"""

class GeraLogDao:

    def inserirLogUsuario(self, log: Log) -> bool:
        #########################################################################################
        # Essa Função insere o log no banco.
        
        # PARAMETROS:
        #   log = Instancia da classe Log com os dados para inserir o log.
        
        # RETORNOS:
        #   return True = Retorna True caso foi inserido com sucesso.
        #########################################################################################

        logUser = CDA013(dataHora=log.dataHora, acao=log.acao, 
                         dadosAntigos=log.converteBytesDadosAntigos(), 
                         dadosNovos=log.converteBytesDadosNovos(), idUsua=log.usuario.id)
        
        DB.session.add(logUser)
        DB.session.commit()
        return True
        
    

    def inserirLogFuncionario(self, log: Log) -> bool:
        #########################################################################################
        # Essa Função insere o log no banco.
        
        # PARAMETROS:
        #   log = Instancia da classe Log com os dados para inserir o log.
        
        # RETORNOS:
        #   return True = Retorna True caso foi inserido com sucesso.
        #########################################################################################

        logFunc = CDA011(dataHora=log.dataHora, acao=log.acao, 
                         dadosAntigos=log.converteBytesDadosAntigos(), 
                         dadosNovos=log.converteBytesDadosNovos(), idUsua=log.usuario.id)
    
        DB.session.add(logFunc)
        DB.session.commit()
        return True
    

    def inserirLogChave(self, log: Log) -> bool:
        #########################################################################################
        # Essa Função insere o log no banco.
        
        # PARAMETROS:
        #   log = Instancia da classe Log com os dados para inserir o log.
        
        # RETORNOS:
        #   return True = Retorna True caso foi inserido com sucesso.
        #########################################################################################

        logChave = CDA010(dataHora=log.dataHora, acao=log.acao, observacao=log.observacao, 
                         dadosAntigos=log.converteBytesDadosAntigos(), 
                         dadosNovos=log.converteBytesDadosNovos(), idUsua=log.usuario.id)
    
        DB.session.add(logChave)
        DB.session.commit()
        return True
    

    def inserirLogControleChave(self, log: Log) -> bool:
        #########################################################################################
        # Essa Função insere o log no banco.
        
        # PARAMETROS:
        #   log = Instancia da classe Log com os dados para inserir o log.
        
        # RETORNOS:
        #   return True = Retorna True caso foi inserido com sucesso.
        #########################################################################################

        logControleChave = CDA001(dataHora=log.dataHora, acao=log.acao, observacao=log.observacao, 
                         dadosAntigos=log.converteBytesDadosAntigos(), 
                         dadosNovos=log.converteBytesDadosNovos(), idUsua=log.usuario.id)
    
        DB.session.add(logControleChave)
        DB.session.commit()
        return True
    

    def inserirLogTerceiro(self, log: Log) -> bool:
        #########################################################################################
        # Essa Função insere o log no banco.
        
        # PARAMETROS:
        #   log = Instancia da classe Log com os dados para inserir o log.
        
        # RETORNOS:
        #   return True = Retorna True caso foi inserido com sucesso.
        #########################################################################################

        logTerc = CDA012(dataHora=log.dataHora, acao=log.acao, observacao=log.observacao, 
                         dadosAntigos=log.converteBytesDadosAntigos(), 
                         dadosNovos=log.converteBytesDadosNovos(), idUsua=log.usuario.id)
    
        DB.session.add(logTerc)
        DB.session.commit()
        return True
    

    def inserirLogControleTerceiro(self, log: Log) -> bool:
        #########################################################################################
        # Essa Função insere o log no banco.
        
        # PARAMETROS:
        #   log = Instancia da classe Log com os dados para inserir o log.
        
        # RETORNOS:
        #   return True = Retorna True caso foi inserido com sucesso.
        #########################################################################################

        logControleTerc = CDA008(dataHora=log.dataHora, acao=log.acao, observacao=log.observacao, 
                         dadosAntigos=log.converteBytesDadosAntigos(), 
                         dadosNovos=log.converteBytesDadosNovos(), idUsua=log.usuario.id)
    
        DB.session.add(logControleTerc)
        DB.session.commit()
        return True
    

    def inserirLogControleGerente(self, log: Log) -> bool:
        #########################################################################################
        # Essa Função insere o log no banco.
        
        # PARAMETROS:
        #   log = Instancia da classe Log com os dados para inserir o log.
        
        # RETORNOS:
        #   return True = Retorna True caso foi inserido com sucesso.
        #########################################################################################

        logControleGer = CDA006(dataHora=log.dataHora, acao=log.acao, observacao=log.observacao, 
                         dadosAntigos=log.converteBytesDadosAntigos(), 
                         dadosNovos=log.converteBytesDadosNovos(), idUsua=log.usuario.id)
    
        DB.session.add(logControleGer)
        DB.session.commit()
        return True
    

    

        
        