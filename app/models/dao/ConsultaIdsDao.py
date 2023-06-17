from ..Tables import SysUser
from ...extensions.Database import DB

"""
Classe Dao para consultar IDs do sistema
@tables - SysUser
@author - Fabio
@version - 1.0
@since - 05/06/2023
"""

class ConsultaIds:

    def consultaIdUserLogado(self, usuario: str) -> int:
        #########################################################################################
        # Essa Função consulta o ID do usuário que está logado no sistema.
        
        # PARAMETROS:
        #   usuario = Instancia da classe Usuario com o ID do usuário.
        
        # RETORNOS:
        #   return id[0] = Retorna o ID do usuário.
        #########################################################################################

        id = DB.session.query(SysUser.id).filter(SysUser.us_usuario==usuario).order_by(SysUser.id.desc()).first()
        return id[0]
    

    def consultaIdFinalUser(self) -> int:
        #########################################################################################
        # Essa Função consulta o último ID da tabela de usuários para releciona no Log.
        
        # PARAMETROS:
        #   Não tem parametros. 
        
        # RETORNOS:
        #   return id[0] = Retorna o ID do usuário.
        #########################################################################################

        id = DB.session.query(SysUser.id).order_by(SysUser.id.desc()).first()
        return id[0]

    