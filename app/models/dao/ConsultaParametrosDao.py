from ...configurations.Database import DB
from ..Tables import CDA015

class ConsultaParametrosDao:
    """
    Classe Dao para funções de consulta de parametros das tabelas do sistema
    @tables - CDA015
    @author - Fabio
    @version - 1.0
    @since - 06/09/2023
    """

    def consultaParametros(self, codigo: str) -> int:
        """
        Consulta o parametro para definir a data da consulta da tabela de logs insert de usuários.

        :return: O número em meses para a consulta.
        """

        valor = CDA015.query.filter(CDA015.par_codigo==codigo).first()

        return int(valor.par_valor)
    

    def consultaTodosParametros(self) -> CDA015:
        """
        Consulta o parametro para definir a data da consulta da tabela de logs insert de usuários.

        :return: O número em meses para a consulta.
        """

        parametros = DB.session.query(CDA015.par_codigo, CDA015.par_valor, CDA015.par_desc).order_by(CDA015.par_codigo)

        return parametros
    
    

    def aleterarParametros(self, codigo: str, valor: int) -> bool:
        """
        Altera os valores de qualquer parâmetro que for passado.

        :param codigo: O código que corresponde ao parâmetro.
        :param valor: o novo valor a ser atualizado.

        :return: O número em meses para a consulta.
        """

        #Campos a serem atualizados
        campos = {
            "par_valor": valor
        }

        CDA015.query.filter(CDA015.par_codigo==codigo).update(campos)
        DB.session.commit()

        return True