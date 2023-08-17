from ldap3 import Server, Connection, SAFE_SYNC, SUBTREE

class Ldap:

    def mostrarMaquinas(self, grupo: str) -> list:
        conn = Connection(Server('LDAP:'),
                            auto_bind=True,
                            user="{}\\{}".format("", ""),
                            password="",
                            auto_referrals=False)

        maquinas = conn.extend.standard.paged_search(f'', '(objectClass=computer)', attributes=['cn', 'givenName'])

        return maquinas