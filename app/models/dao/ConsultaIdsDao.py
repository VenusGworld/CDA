from ..Tables import SysUser, CDA007, CDA002, CDA004, CDA009, CDA003
from ...configurations.Database import DB

"""
Classe Dao para consultar IDs do sistema
@tables - SysUser, CDA007, CDA002, CDA004, CDA009, CDA003
@author - Fabio
@version - 1.0
@since - 05/06/2023
"""

class ConsultaIdsDao:

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
        # Essa Função consulta o último ID da tabela de Usuários.
        
        # PARAMETROS:
        #   Não tem parametros. 
        
        # RETORNOS:
        #   return id[0] = Retorna o ID do Usuário.
        #########################################################################################

        id = DB.session.query(SysUser.id).order_by(SysUser.id.desc()).first()
        return id[0]
    

    def consultaIdFinalFunc(self) -> int:
        #########################################################################################
        # Essa Função consulta o último ID da tabela de Funcionários.
        
        # PARAMETROS:
        #   Não tem parametros. 
        
        # RETORNOS:
        #   return id[0] = Retorna o ID do Funcionário.
        #########################################################################################

        id = DB.session.query(CDA007.id_funcionarios).order_by(CDA007.id_funcionarios.desc()).first()
        return id[0]
    

    def consultaIdFinalMovChave(self) -> int:
        #########################################################################################
        # Essa Função consulta o último ID da tabela do Movimento de Chave.
        
        # PARAMETROS:
        #   Não tem parametros. 
        
        # RETORNOS:
        #   return id[0] = Retorna o ID do Movimento de Chave.
        #########################################################################################

        id = DB.session.query(CDA002.id_movChave).order_by(CDA002.id_movChave.desc()).first()
        return id[0]
    

    def consultaIdFinalMovTerc(self) -> int:
        #########################################################################################
        # Essa Função consulta o último ID da tabela do Movimento de Terceiro.
        
        # PARAMETROS:
        #   Não tem parametros. 
        
        # RETORNOS:
        #   return id[0] = Retorna o ID do Movimento de Terceiro.
        #########################################################################################

        id = DB.session.query(CDA004.id_movTerc).order_by(CDA004.id_movTerc.desc()).first()
        return id[0]
    

    def consultaIdFinalTerc(self) -> int:
        #########################################################################################
        # Essa Função consulta o último ID da tabela de Terceiros.
        
        # PARAMETROS:
        #   Não tem parametros. 
        
        # RETORNOS:
        #   return id[0] = Retorna o ID do Movimento de Terceiros.
        #########################################################################################

        id = DB.session.query(CDA009.id_terceiro).order_by(CDA009.id_terceiro.desc()).first()

        return id[0]
    

    def consultaCodFinalTerc(self) -> str:
        #########################################################################################
        # Essa Função consulta o último código da tabela de Terceiros.
        
        # PARAMETROS:
        #   Não tem parametros. 
        
        # RETORNOS:
        #   return id[0] = Retorna o ID do Movimento de Terceiros.
        #########################################################################################

        codigo = DB.session.query(CDA009.te_codigo).order_by(CDA009.te_codigo.desc()).first()
        
        return codigo
    

    def consultaIdFinalMovGer(self) -> int:
        #########################################################################################
        # Essa Função consulta o último ID da tabela do Movimento de Gerente.
        
        # PARAMETROS:
        #   Não tem parametros. 
        
        # RETORNOS:
        #   return id[0] = Retorna o ID do Movimento de Gerente.
        #########################################################################################

        id = DB.session.query(CDA003.id_movGere).order_by(CDA003.id_movGere.desc()).first()
        return id[0]
    