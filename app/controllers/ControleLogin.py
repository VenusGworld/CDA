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
        #   return 1 = Retorna 1 se o usuário existe e está correto e usuário Administrador;
        #   return 2 = Retorna 2 se o usuário existe e está correto e usuário Tec. Segurança;
        #   return 3 = Retorna 3 se o usuário existe e está correto e usuário Vigilante;
        #   return 4 = Retorna 4 se a senha/usuário estão incorretos;
        #   return 5 = Retorna 5 se o usuário está inativo ou deletado;
        #   return 6 = Retorna 6 se o usuário não existe;
        #########################################################################################
        
        usuario = Usuario()
        usuario.set_usuario(user)
        usuario.set_senha(pssd)
        if user == "ADMIN":
            return self.loginAdm(usuario)
        else:
            loginDao = LoginDao()
            userResp = loginDao.consultaUsuario(usuario)
            if userResp != 0:
                if usuario.get_delete() != True or usuario.get_ativo() != True: #Verifica se o usuário está inativo ou deletado
                    if usuario.verificarSenha(): #Verfica a senha digitada
                        login_user(userResp)
                        session["nome"] = usuario.get_nome()
                        session["usuario"] = usuario.get_usuario()
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
    

    def loginAdm(self, usuario: Usuario) -> int:
        loginDao = LoginDao()
        userResp = loginDao.loginAdm(usuario)
        if usuario.verificarSenha():
            login_user(userResp)
            session["nome"] = usuario.get_nome()
            session["usuario"] = usuario.get_usuario()
            return 1
        else:
            return 4

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