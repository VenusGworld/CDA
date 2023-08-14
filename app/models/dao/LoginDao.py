from ...configurations.Database import DB
from ..entity.Usuario import Usuario
from ..Tables import SysUser

"""
Classe Dao para login no sistema
@tables - SysUser
@author - Fabio
@version - 1.0
@since - 25/04/2023
"""

class LoginDao:
    
    def consultaUsuario(self, login: Usuario):
        #########################################################################################
        # Essa Função verfica se usuário existe no banco.
         
        # PARAMETROS:
        #   login = Instancia da classe Usuario com usuário e senha.
        
        # RETORNO:
        #   return user = Retorna o usuário que achou no banco.
        #   return 0 = Retorna 0 caso o usuário não exista.
        #########################################################################################

        sysuser = SysUser.query.filter_by(us_usuario=login.usuario).first()
        if sysuser:
            login.id = sysuser.id
            login.nome = sysuser.us_nome
            login.email = sysuser.us_email
            login.grupo = sysuser.us_grupo
            login.complex = sysuser.us_complex
            login.ativo = sysuser.us_ativo
            login.delete = sysuser.us_delete
            login.senhaCompara = sysuser.us_senha
            return sysuser
        else:
            return 0 


    def verficaTrocaSenha(self, login: Usuario) -> bool:
        #########################################################################################
        # Essa Função verfica se usuário está logando solicitou a troca de senha.
         
        # PARAMETROS:
        #   login = Instancia da classe Usuario com usuário e senha.
        
        # RETORNO:
        #   return True = Retorna True caso foi solicitado;
        #   return False = Retorna False caso não foi solicitado.
        #########################################################################################

        sysuser = SysUser.query.get(login.id)
        if sysuser.us_novaSenha:
            return True
        else:
            return False
        
    
    def atulizaTrocaSenha(self, login: Usuario) -> bool:
        #########################################################################################
        # Essa Função atualiza os campos de troca senha, para retirar a solicitação.
         
        # PARAMETROS:
        #   login = Instancia da classe Usuario com usuário e senha.
        
        # RETORNO:
        #   return True = Retorna True caso foi alterado com sucesso;
        #   return False = Retorna False caso de erro.
        #########################################################################################

        sysuser = SysUser.query.get(login.id)
        sysuser.us_hashNovaSenha = ""
        sysuser.us_novaSenha = False
        sysuser.us_limiteNovasenha = ""

        DB.session.commit()
        return True
        
            
    
         