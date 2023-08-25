from ..models.dao.ManterUsuarioDao import ManterUsuarioDao
from flask_login import login_user, logout_user
from ..models.entity.Usuario import Usuario
from ..models.dao.LoginDao import LoginDao
from flask import session

class ControleLogin:
    """
    Classe Controller para funções relacionadas ao login no sistema
    @author - Fabio
    @version - 1.0
    @since - 23/05/2023
    """
    
    def login(self, user: str, pssd: str) -> int:
        """
        Realiza o processo de login do usuário.

        :param user: O nome de usuário.
        :param pssd: A senha do usuário.

        :return: Um código indicando o resultado do processo de login.
            1 - Login bem-sucedido para grupo "ADM".
            2 - Login bem-sucedido para grupo "TEC".
            3 - Login bem-sucedido para grupo "VIG".
            4 - Senha/Usuário estão incorretos.
            5 - Usuário inativo ou deletado.
            6 - Usuário não encontrado.
        """

        usuario = Usuario()
        usuario.usuario = user
        usuario.senha = pssd
        if user == "ADMIN":
            return self.loginAdm(usuario)
        else:
            loginDao = LoginDao()
            userResp = loginDao.consultaUsuario(usuario)
            if userResp != 0:
                #Verifica se o usuário está inativo ou deletado
                if usuario.delete != True and usuario.ativo != True: 
                    #Verfica a senha digitada
                    if usuario.verificarSenha(): 
                        #Verifica se usuário que está logando solicitou troca de senha
                        self.verficaTrocaSenha(usuario) 
                        login_user(userResp)
                        session["nome"] = usuario.nome
                        session["usuario"] = usuario.usuario
                        session["grupo"] = usuario.grupo
                        if usuario.grupo == "ADM":
                            return 1
                        elif usuario.grupo == "TEC":
                            return 2
                        elif usuario.grupo == "VIG":
                            return 3
                    else:
                        return 4
                else:
                    return 5
            else:
                return 6
    

    def loginAdm(self, usuario: Usuario) -> int:
        """
        Realiza o processo de login para o usuário administrador (ADMIN).

        :param usuario: A instância do usuário.

        :return: Um código indicando o resultado do processo de login ADMIN.
            1 - Login ADMIN bem-sucedido.
            4 - Senha ADMIN incorreta.
        """

        loginDao = LoginDao()
        #Verifica se o ADMIN já existe
        userResp = loginDao.consultaUsuario(usuario) 
        if userResp != 0:
            if usuario.verificarSenha():
                #Verifica se usuário que está logando solicitou troca de senha
                self.verficaTrocaSenha(usuario)  
                login_user(userResp)
                session["nome"] = usuario.nome
                session["usuario"] = usuario.usuario
                session["grupo"] = usuario.grupo
                return 1
            else:
                return 4
        else:
            controleManterUsuario = ManterUsuarioDao()
            controleManterUsuario.adicionarAdm(usuario)
            controleManterUsuario.inserirUsuario(usuario)
            userResp = loginDao.consultaUsuario(usuario)
            if usuario.verificarSenha():
                #Verifica se usuário que está logando solicitou troca de senha
                self.verficaTrocaSenha(usuario) 
                login_user(userResp)
                session["nome"] = usuario.nome
                session["usuario"] = usuario.usuario
                session["grupo"] = usuario.grupo
                return 1
            else: 
                return 4
      
            
    def loginVig(self, user: str, pssd: str) -> int:
        """
        Realiza o processo de login na hora da movimentação no sistema dos usuários vigilantes (VIG).

        :param user: O nome de usuário.
        :param pssd: A senha do usuário.

        :return: Um código indicando o resultado do processo de login VIG.
            1 - Login bem-sucedido para grupo "ADM".
            2 - Login bem-sucedido para grupo "TEC".
            3 - Login bem-sucedido para grupo "VIG".
            4 - Senha/Usuário estão incorretos.
            5 - Usuário inativo ou deletado.
            6 - Usuário não encontrado.
        """
        
        usuario = Usuario()
        usuario.usuario = user
        usuario.senha = pssd
        loginDao = LoginDao()
        userResp = loginDao.consultaUsuario(usuario)
        if userResp != 0:
            #Verifica se o usuário está inativo ou deletado
            if usuario.delete != True and usuario.ativo != True: 
                #Verfica a senha digitada
                if usuario.verificarSenha(): 
                    #Verifica se usuário que está logando solicitou troca de senha
                    self.verficaTrocaSenha(usuario) 
                    login_user(userResp)
                    session["usuarioVIG"] = usuario.usuario
                    if usuario.grupo == "ADM":
                        return 1
                    elif usuario.grupo == "TEC":
                        return 2
                    elif usuario.grupo == "VIG":
                        return 3
                else:
                    return 4
            else:
                return 5
        else:
            return 6


    def verficaTrocaSenha(self, usuario: Usuario) -> None:
        """
        Essa Função recebe o usuário que está efetuando o login no sistema, e verifica se foi
        solicitado a troca de senha, caso tenha solicitado o sistema retira a solicitação.

        :param usuario: Objeto do tipo Usuario.

        :return: Nenhum valor é retornado.
        """
        
        loginDao = LoginDao()
        if loginDao.verficaTrocaSenha(usuario):
            loginDao.atulizaTrocaSenha(usuario)
        else:
            pass


    def logout(self) -> None:
        """
        Realiza o logout do usuário.

        :return: Nenhum valor é retornado.
        """
        
        logout_user()
        session.clear()