from ldap3 import Server, Connection, SAFE_SYNC, SUBTREE

class Ldap:
    """
    Classe Dao para Consultas no Servidor AD
    @author - Fabio
    @version - 1.0
    @since - 25/08/2023
    """

    def consultarMaquinas(self, grupo: str) -> list:
        """
        Esta função realiza uma consulta ao servidor LDAP para buscar as informações das máquinas pertencentes
        a um grupo específico. As máquinas são retornadas como uma lista de dicionários contendo os atributos
        "cn" (Common Name) e "givenName" (Nome Próprio) das máquinas.

        :param grupo: O nome do grupo para o qual deseja consultar as máquinas.

        :return: Uma lista de dicionários contendo informações das máquinas do grupo.
        """

        conn = Connection(Server(''),
                            auto_bind=True,
                            user="{}\\{}".format("", ""),
                            password="",
                            auto_referrals=False)

        maquinas = conn.extend.standard.paged_search(f'', '(objectClass=computer)', attributes=['cn', 'givenName'])

        return maquinas