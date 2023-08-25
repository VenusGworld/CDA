from ..models.dao.EsqueciSenhaDao import EsqueciSenhaDao
from ..extensions.EnviaEmail import EnviaEmail
from ..models.entity.Usuario import Usuario
from datetime import datetime

class ControleEsqueciSenha:
    """
    Classe Controller para funções relacionadas ao esqueci a senha
    @author - Fabio
    @version - 1.0
    @since - 13/06/2023
    """

    def verificarUsuario(self, usuario: str, email: str) -> int:
        """
        Essa Função recebe usuario e e-mail como parametro para verificar se o usuário existe
        e gera o hash que vai ser enviado posteriormente por e-mail, para efutar a troca da senha.

        :param usuario: O nome de usuário.
        :param email: O endereço de e-mail associado ao usuário.

        :return: Um código de retorno que indica o resultado da operação.
                - 1: Sucesso na redefinição da senha e envio do e-mail.
                - 2: Erro ao enviar o e-mail.
                - 3: Falha na verificação das informações do usuário.
        """

        user = Usuario()
        esqueciSenhaDao = EsqueciSenhaDao()
        user.usuario = usuario
        user.email = email
        respDao = esqueciSenhaDao.verificaUsuario(user)
        #Verifica se o usuário existe
        if respDao != 0:
            #Gera um hash para nova senha
            user.gerarHashSenhaNova()
            #Loop para garantir a unicidade do hash
            while True:
                if esqueciSenhaDao.verificaHash(user.hashSenhaNova):
                    break
                else:
                    user.gerarHashSenhaNova()
            
            esqueciSenhaDao.insereHash(user)

            #Envia e-mail para a redifinição de senha
            enviaEmail = EnviaEmail()
            if enviaEmail.enviarEmail(user):
                return 1
            else:
                return 2
        else:
            return 3


    def verificarHash(self, hash: str) -> int:
        """
        Verifica a validade de um hash de redefinição de senha.

        :param hash: O hash associado à redefinição de senha.

        :return: Um código de retorno que indica a validade do hash.
                - 1: Hash válido e dentro do limite de tempo.
                - 2: Hash inválido.
                - 3: Hash válido, mas expirado.
        """

        dataAtual = datetime.now()
        esqueciSenhaDao = EsqueciSenhaDao()
        usuario = esqueciSenhaDao.verificaHashTempo(hash)
        #Verifica se o usuário associado ao hash existe
        if usuario:
            #Verifica se a data atual é posterior ao limite de tempo do hash
            if str(dataAtual) > usuario.us_limiteNovasenha:
                return 3
            else:
                return 1
        else:
            return 2
        

    def trocaSenha(self, senha: str, hash: str) -> bool:
        """
        Realiza a troca de senha com base no hash de redefinição de senha.

        :param senha: A nova senha a ser definida.
        :param hash: O hash associado à redefinição de senha.
        """
        
        user = Usuario()
        user.gerarSenha(senha)
        user.hashSenhaNova= ""
        user.senhaNova = False

        esqueciSenhaDao = EsqueciSenhaDao()
        esqueciSenhaDao.trocaSenha(hash, user)
            
        return True