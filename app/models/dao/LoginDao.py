from ...configurations.Database import DB
from ..entity.Usuario import Usuario
from ..Tables import SysUser

class LoginDao:
    """
    Classe Dao para login no sistema
    @tables - SysUser
    @author - Fabio
    @version - 1.0
    @since - 25/04/2023
    """
    
    def consultaUsuario(self, login: Usuario):
        """
        Consulta um usuário no banco de dados.

        :param login: Um objeto 'Usuario' contendo o nome de usuário (login) a ser consultado.

        :return: O objeto 'SysUser' correspondente se o usuário for encontrado, caso contrário, retorna 0.
        """

        sysuser = SysUser.query.filter_by(us_usuario=login.usuario).first()
        if sysuser:
            login.id = sysuser.id
            login.nome = sysuser.us_nome
            login.email = sysuser.us_email
            login.grupo = sysuser.us_grupo
            login.complex = sysuser.us_complex
            login.ativo = sysuser.us_inativo
            login.delete = sysuser.us_delete
            login.senhaCompara = sysuser.us_senha
            return sysuser
        else:
            return 0 


    def verficaTrocaSenha(self, login: Usuario) -> bool:
        """
        Verifica se um usuário que está efetuando o login solicitou a troca de senha.

        :param login: Um objeto 'Usuario' contendo as informações do usuário.

        :return: True se o usuário precisa trocar a senha, False caso contrário.
        """

        sysuser = SysUser.query.get(login.id)
        if sysuser.us_novaSenha:
            return True
        else:
            return False
        
    
    def atulizaTrocaSenha(self, login: Usuario) -> bool:
        """
        Atualiza as informações após a troca de senha.

        :param login: Um objeto 'Usuario' contendo as informações do usuário.

        :return: True se as informações foram atualizadas com sucesso, False em caso de erro.
        """

        sysuser = SysUser.query.get(login.id)
        sysuser.us_hashNovaSenha = ""
        sysuser.us_novaSenha = False
        sysuser.us_limiteNovasenha = ""

        DB.session.commit()
        return True
    

    def consultaQuantideUsers(self) -> int:
        """
        Consulta a quantidade de usuários cadastrados.

        :return: A quantidade de usuários.
        """

        quantidade = SysUser.query.count()

        return int(quantidade)
            
    
         