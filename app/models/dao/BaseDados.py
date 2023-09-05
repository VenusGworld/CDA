from ...configurations.Database import DB

class BaseDados:
    """
    Classe Dao para consultar a data base que o sistema está conectado
    @tables - 
    @author - Fabio
    @version - 1.0
    @since - 01/09/2023
    """

    def verificaBase():
        """
        Consulta o base de dados que o sistema está conectado.

        :return: A base conectada.
        """

        base = DB.session.execute("SELECT current_database()").scalar()

        return base