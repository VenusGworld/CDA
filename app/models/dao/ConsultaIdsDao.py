from ..Tables import SysUser, CDA007, CDA002, CDA004, CDA009, CDA003
from ...configurations.Database import DB

class ConsultaIdsDao:
    """
    Classe Dao para consultar IDs do sistema
    @tables - SysUser, CDA007, CDA002, CDA004, CDA009, CDA003
    @author - Fabio
    @version - 1.0
    @since - 05/06/2023
    """

    def consultaIdUserLogado(self, usuario: str) -> int:
        """
        Consulta o ID do usuário logado.

        :param usuario: O nome de usuário (login) do usuário logado.

        :return: O ID do usuário logado.
        """

        id = DB.session.query(SysUser.id).filter(SysUser.us_usuario==usuario).order_by(SysUser.id.desc()).first()
        return id[0]
    

    def consultaIdFinalUser(self) -> int:
        """
        Consulta o ID do último usuário cadastrado.

        :return: O ID do último usuário cadastrado.
        """

        id = DB.session.query(SysUser.id).order_by(SysUser.id.desc()).first()
        return id[0]
    

    def consultaIdFinalFunc(self) -> int:
        """
        Consulta o ID do último funcionário cadastrado.

        :return: O ID do último funcionário cadastrado.
        """

        id = DB.session.query(CDA007.id_funcionario).order_by(CDA007.id_funcionario.desc()).first()
        return id[0]
    

    def consultaIdFinalMovChave(self) -> int:
        """
        Consulta o ID do último movimento de chave registrado.

        :return: O ID do último movimento de chave registrado.
        """

        id = DB.session.query(CDA002.id_movChave).order_by(CDA002.id_movChave.desc()).first()
        return id[0]
    

    def consultaIdFinalMovTerc(self) -> int:
        """
        Consulta o ID do último movimento de terceiro registrado.

        :return: O ID do último movimento de terceiro registrado.
        """

        id = DB.session.query(CDA004.id_movTerc).order_by(CDA004.id_movTerc.desc()).first()
        return id[0]
    

    def consultaIdFinalTerc(self) -> int:
        """
        Consulta o ID do último terceiro cadastrado.

        :return: O ID do último terceiro cadastrado.
        """

        id = DB.session.query(CDA009.id_terceiro).order_by(CDA009.id_terceiro.desc()).first()
        return id[0]
    

    def consultaCodFinalTerc(self) -> str:
        """
        Consulta o código do último terceiro cadastrado.

        :return: O código do último terceiro cadastrado.
        """

        codigo = DB.session.query(CDA009.te_codigo).order_by(CDA009.te_codigo.desc()).first()
        return codigo
    

    def consultaIdFinalMovGer(self) -> int:
        """
        Consulta o ID do último movimento de gerente registrado.

        :return: O ID do último movimento de gerente registrado.
        """

        id = DB.session.query(CDA003.id_movGere).order_by(CDA003.id_movGere.desc()).first()
        return id[0]
    