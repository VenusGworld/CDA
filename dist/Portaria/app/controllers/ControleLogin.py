from flask import session
from flask_login import login_user, current_user, logout_user
from ..models.entity.Usuario import Usuario
from ..models.dao.LoginDao import LoginDao

#Classe do controle de login
class ControleLogin:
    
    def login(self, user: str, pssd: str) -> int:
        #########################################################################################
        # Função que recebe os dados digitados nos inputs e chama a dao para verificar no banco.
        
        # PARAMETROS:
        #   user = Dados informados no input usuário da tela de login;
        #   pssd = Dados informados no input senha da tela de login.
        
        # RETORNOS:
        #   return True = Retorna True se o usuário existe e está correto;
        #   return False = Retorna False se a senha/usuário estão incorretos ou usuário não existe.
        #########################################################################################
        
        usuario = Usuario()
        usuario.set_usuario(user)
        usuario.set_senha(pssd)
        loginDao = LoginDao()
        userResp = loginDao.consultaUsuario(usuario)
        if userResp != 0:
            if usuario.get_delete() != True or usuario.get_ativo() != True: #Verifica se o usuário está inativo ou deletado
                if usuario.verificarSenha(): #Verfica a senha digitada
                    login_user(userResp)
                    session["usuario_logado"] = usuario.get_nome()
                    if usuario.get_grupo() == "ADM":
                        return 1
                    elif usuario.get_grupo() == "TEC":
                        return 2
                    elif usuario.get_grupo() == "VIG":
                        return 3
                else:
                    return 4
            else:
                return 5
        else:
            return 6
        
        
    def logout(self) -> None:
        #########################################################################################
        # Função que efetua o logout do sistema.
        
        # PARAMETROS:
        #   Não tem parametros.
        
        # RETORNOS:
        #   Não tem retornos.
        #########################################################################################
        
        logout_user()
        session.clear()