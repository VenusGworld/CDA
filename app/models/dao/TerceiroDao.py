from ..Tables import CDA016

class TerceiroDao:
    """
    Classe Dao para a tabela de relacionamento de movimento de terceiro e terceiro
    @tables - CDA016
    @author - Fabio
    @version - 1.0
    @since - 09/08/2023
    """

    def terceirosMovimento(self, idMov: int) -> list[int]:
        """
        Consulta os IDs dos terceiros associados a um determinado movimento.

        :param idMov: O ID do movimento de terceiro para o qual se deseja obter os IDs dos terceiros.
        
        :return: Uma lista de IDs dos terceiros associados ao movimento.
        """

        ids = CDA016.query.filter(CDA016.id_movTerc==idMov)
        
        listaIds = []
        if ids:    
            for id in ids:
                listaIds.append(id.id_terceiro)
            return listaIds
        else:
            return listaIds