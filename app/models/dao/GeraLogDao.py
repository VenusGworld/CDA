from app.models.entity.Log import Log
from ..Tables import CDA013, CDA011, CDA001, CDA010
from ...configurations.Database import DB
import sys

"""
Classe Dao para gerar de log
@tables - CDA013, CDA011, CDA001, CDA010
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

        logUser = CDA011(dataHora=log.dataHora, acao=log.acao, 
                         dadosAntigos=log.converteBytesDadosAntigos(), 
                         dadosNovos=log.converteBytesDadosNovos(), idUsua=log.usuario.id)
    
        DB.session.add(logUser)
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

        logUser = CDA010(dataHora=log.dataHora, acao=log.acao, observacao=log.observacao, 
                         dadosAntigos=log.converteBytesDadosAntigos(), 
                         dadosNovos=log.converteBytesDadosNovos(), idUsua=log.usuario.id)
    
        DB.session.add(logUser)
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

        logUser = CDA001(dataHora=log.dataHora, acao=log.acao, observacao=log.observacao, 
                         dadosAntigos=log.converteBytesDadosAntigos(), 
                         dadosNovos=log.converteBytesDadosNovos(), idUsua=log.usuario.id)
    
        DB.session.add(logUser)
        DB.session.commit()
        return True

        
        