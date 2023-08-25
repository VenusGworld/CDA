from ...configurations.Database import DB
from datetime import datetime, timedelta
from ..entity.Usuario import Usuario
from ..Tables import SysUser

class EsqueciSenhaDao:
    """
    Classe Dao para funções do esqueci a senha
    @tables - SysUser
    @author - Fabio
    @version - 1.0
    @since - 13/06/2023
    """

    def insereHash(self, usuario: Usuario) -> bool:
        """
        Insere o hash e informações da nova senha de um usuário no banco de dados.

        :param usuario: Objeto do usuário contendo as informações do hash e nova senha.

        :return: True se a operação for bem-sucedida, False em caso contrário.
        """

        dataAtual = datetime.now()
        sysuser = SysUser.query.get(usuario.id)
        sysuser.us_hashNovaSenha = usuario.hashSenhaNova
        sysuser.us_novaSenha = usuario.senhaNova
        sysuser.us_limiteNovasenha = str(dataAtual + timedelta(minutes=2))

        DB.session.commit()
        return True
        


    def verificaUsuario(self, usuario: Usuario):
        """
        Verifica a existência de um usuário no banco de dados com base no nome de usuário e e-mail.

        :param usuario: Objeto do usuário contendo nome de usuário e e-mail para verificação.

        :return: Objeto do usuário com informações do banco de dados se encontrado, ou 0 se não encontrado.
        """

        sysuser = SysUser.query.filter(SysUser.us_usuario==usuario.usuario, SysUser.us_email==usuario.email, SysUser.us_ativo==False, SysUser.us_delete==False).first()
        if sysuser:
            usuario.id = sysuser.id
            usuario.nome = sysuser.us_nome
            usuario.grupo = sysuser.us_grupo
            usuario.complex = sysuser.us_complex
            usuario.ativo = sysuser.us_ativo
            usuario.delete = sysuser.us_delete
            usuario.senhaCompara = sysuser.us_senha
            usuario.hashSenhaNova = sysuser.us_hashNovaSenha
            usuario.senhaNova = sysuser.us_novaSenha
            usuario.limiteNovasenha = sysuser.us_limiteNovasenha
            return usuario
        else:
            return 0


    def verificaHash(self, hash: str) -> bool:
        """
        Verifica a existência de um hash de solicitação de uma nova senha no banco de dados.

        :param hash: Hash a ser verificado.

        :return: False se o hash estiver presente e válido, True se não estiver presente.
        """

        sysuser = SysUser.query.filter(SysUser.us_hashNovaSenha==hash).first()

        if sysuser:
            return False
        else:
            return True
        

    def verificaHashTempo(self, hash: str) -> bool:
        """
        Verifica a existência de um hash de senha nova no banco de dados. Se existir, verifica a validade do link de troca de senha.

        :param hash: Hash a ser verificado.

        :return: Instância do objeto SysUser se o hash estiver presente e válido, ou False se não estiver presente.
        """

        sysuser = SysUser.query.filter(SysUser.us_hashNovaSenha==hash).first()

        if sysuser:
            return sysuser
        else:
            return False
        

    def trocaSenha(self, hash: str, usuario: Usuario) -> bool:
        """
        Atualiza a senha do usuário com base no hash.

        :param hash: Hash associado à redefinição de senha.
        :param usuario: Instância do objeto Usuario contendo a nova senha e informações relacionadas.

        :return: True se a atualização for bem-sucedida, False se o hash não for encontrado.
        """

        sysuser = SysUser.query.filter(SysUser.us_hashNovaSenha==hash).first()

        sysuser.us_senha = usuario.senha
        sysuser.us_complex = usuario.complex
        sysuser.us_novaSenha = usuario.senhaNova
        sysuser.us_hashNovaSenha = usuario.hashSenhaNova
        sysuser.us_limiteNovasenha = ""

        DB.session.commit()
        return True
        


