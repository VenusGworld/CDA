from ..Tables import SysUser
from ..entity.Usuario import Usuario
from ...extensions.Database import DB
import sys

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

        try:
            sysuser = SysUser.query.filter_by(us_usuario=login.get_usuario()).first()
            if sysuser:
                login.set_id(sysuser.id)
                login.set_nome(sysuser.us_nome)
                login.set_email(sysuser.us_email)
                login.set_grupo(sysuser.us_grupo)
                login.set_complex(sysuser.us_complex)
                login.set_ativo(sysuser.us_ativo)
                login.set_delete(sysuser.us_delete)
                login.set_senhaCompara(sysuser.us_senha)
                return sysuser
            else:
                return 0 
        except Exception as erro:
            print(erro, sys.exc_info()[0])
            pass


    def verficaTrocaSenha(self, login: Usuario) -> bool:
        #########################################################################################
        # Essa Função verfica se usuário está logando solicitou a troca de senha.
         
        # PARAMETROS:
        #   login = Instancia da classe Usuario com usuário e senha.
        
        # RETORNO:
        #   return True = Retorna True caso foi solicitado;
        #   return False = Retorna False caso não foi solicitado.
        #########################################################################################

        sysuser = SysUser.query.get(login.get_id())
        if sysuser.us_senhaNova:
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

        sysuser = SysUser.query.get(login.get_id())
        sysuser.us_hashNovaSenha = ""
        sysuser.us_senhaNova = False

        try:
            DB.session.commit()
            return True
        except Exception as erro:
            print(erro, sys.exc_info()[0])
            return False
            
    
         