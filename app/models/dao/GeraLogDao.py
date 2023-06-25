from app.models.entity.Log import Log
from ..Tables import CDA013, CDA011
from ...configurations.Database import DB
import sys

"""
Classe Dao para gerar de log
@tables - CDA013, CDA011
@author - Fabio
@version - 1.0
@since - 05/06/2023
"""

class GeraLogDao:

    def inserirLogUsuario(self, log: Log) -> bool:
        #########################################################################################
        # Essa Função insere o log no banco.
        
        # PARAMETROS:
        #   log = Instancia da classe Log com os dados para inserir o log.
        
        # RETORNOS:
        #   return True = Retorna True caso foi inserido com sucesso;
        #   return False = Retorna False caso ocorra erro na inserção.
        #########################################################################################

        logUser = CDA013(dataHora=log.dataHora, acao=log.acao, 
                         dadosAntigos=log.converteDadosAntigos(), 
                         dadosNovos=log.converteDadosNovos(), idUsua=log.usuario.id)
        
        DB.session.add(logUser)
        DB.session.commit()
        return True
        
    

    def inserirLogFuncionario(self, log: Log) -> bool:
        #########################################################################################
        # Essa Função insere o log no banco.
        
        # PARAMETROS:
        #   log = Instancia da classe Log com os dados para inserir o log.
        
        # RETORNOS:
        #   return True = Retorna True caso foi inserido com sucesso;
        #   return False = Retorna False caso ocorra erro na inserção.
        #########################################################################################

        logUser = CDA011(dataHora=log.dataHora, acao=log.acao, 
                         dadosAntigos=log.converteDadosAntigos(), 
                         dadosNovos=log.converteDadosNovos(), idUsua=log.usuario.id)
    
        DB.session.add(logUser)
        DB.session.commit()
        return True
        
        