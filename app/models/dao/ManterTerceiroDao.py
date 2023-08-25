from ...configurations.Database import DB
from ..entity.Terceiro import Terceiro
from ..Tables import CDA009, CDA016


class ManterTerceiroDao:
    """
    Classe Dao para o manter Tereceiro
    @tables - CDA009, CDA016
    @author - Fabio
    @version - 1.0
    @since - 26/07/2023
    """

    def consultarTerceiros(self) -> CDA009:
        """
        Consulta os terceiros que não estão inativos ou deletados cadastradas no sistema.

        :return: Uma lista de terceiros ordenados pelo nome.
        """

        terceiros = CDA009.query.filter(CDA009.te_delete!=True, CDA009.te_ativo!=True).order_by(CDA009.te_nome)

        return terceiros
    

    def consultarTerceiroDetalhadoCpf(self, cpf: str) -> Terceiro:
        """
        Consulta um terceiro no banco de dados pelo CPF.

        :param cpf: O CPF do terceiro a ser consultado.

        :return: Um objeto da classe Terceiro com os detalhes do terceiro encontrado.
        """

        terceiro = CDA009.query.filter(CDA009.te_cpf==cpf, CDA009.te_delete!=True, CDA009.te_ativo!=True).first()

        terceiroMov = Terceiro()
        terceiroMov.id = terceiro.id_terceiro
        terceiroMov.codigo = terceiro.te_codigo
        terceiroMov.nome = terceiro.te_nome
        terceiroMov.cpf = terceiro.te_cpf
        terceiroMov.ativo = terceiro.te_ativo
        terceiroMov.delete = terceiro.te_delete

        return terceiroMov
    

    def consultarTerceiroDetalhadoId(self, id: int) -> Terceiro:
        """
        Consulta um terceiro no banco de dados pelo ID.

        :param id: O ID do terceiro a ser consultado.
        
        :return: Um objeto da classe Terceiro com os detalhes do terceiro encontrado.
        """

        terceiro = CDA009.query.filter(CDA009.id_terceiro==id, CDA009.te_delete!=True, CDA009.te_ativo!=True).first()

        terceiroMov = Terceiro()
        terceiroMov.id = terceiro.id_terceiro
        terceiroMov.codigo = terceiro.te_codigo
        terceiroMov.nome = terceiro.te_nome
        terceiroMov.cpf = terceiro.te_cpf
        terceiroMov.ativo = terceiro.te_ativo
        terceiroMov.delete = terceiro.te_delete

        return terceiroMov
    

    def consultarTerceiroDetalhadoCodigo(self, codigo: str) -> Terceiro:
        """
        Consulta um terceiro no banco de dados pelo código.

        :param codigo: O código do terceiro a ser consultado.
        
        :return: Um objeto da classe Terceiro com os detalhes do terceiro encontrado.
        """

        terceiro = CDA009.query.filter(CDA009.te_codigo==codigo, CDA009.te_delete!=True, CDA009.te_ativo!=True).first()

        terceiroMov = Terceiro()
        terceiroMov.id = terceiro.id_terceiro
        terceiroMov.codigo = terceiro.te_codigo
        terceiroMov.nome = terceiro.te_nome
        terceiroMov.cpf = terceiro.te_cpf
        terceiroMov.ativo = terceiro.te_ativo
        terceiroMov.delete = terceiro.te_delete

        return terceiroMov
    

    def incluirTerceiro(self, tereceiro: Terceiro) -> bool:
        """
        Insere um novo terceiro no banco de dados.

        :param terceiro: Objeto da classe Terceiro contendo as informações do terceiro a ser inserido.

        :return: True se a inserção for bem-sucedida, False caso contrário.
        """

        terc = CDA009(codigo=tereceiro.codigo, nome=tereceiro.nome, 
                      cpf=tereceiro.cpf, ativo=tereceiro.ativo, 
                      delete=tereceiro.delete)
        
        DB.session.add(terc)
        DB.session.commit()

        return True
    

    def editarTerceiro(self, terceiro: Terceiro) -> bool:
        """
        Edita as informações de um terceiro no banco de dados.

        :param terceiro: Objeto da classe Terceiro contendo as novas informações do terceiro.

        :return: True se a edição for bem-sucedida, False caso contrário.
        """
        
        terc = CDA009.query.get(terceiro.id)

        terc.te_nome = terceiro.nome
        DB.session.commit()

        return True
    

    def inativarTerceiro(self, id: int) -> bool:
        """
        Marca um terceiro como desativado no sistema.

        :param id: ID do terceiro a ser marcado como desativado.
        
        :return: True se a marcação como desativado for bem-sucedida, False caso contrário.
        """

        terc = CDA009.query.get(id)

        terc.te_ativo = True
        DB.session.commit()

        return True
    

    def excluirTerceiro(self, id: int) -> bool:
        """
        Marca um terceiro como excluído no sistema.

        :param id: ID do terceiro a ser marcado como excluído.

        :return: True se a marcação como excluído for bem-sucedida, False caso contrário.
        """

        terc = CDA009.query.get(id)

        terc.te_delete = True
        DB.session.commit()

        return True
    

    def verificaMovAbertoTerceiro(self, id: int) -> CDA016:
        """
        Verifica se existem movimentos abertos para um terceiro no banco de dados.

        :param id: O ID do terceiro para o qual se deseja verificar movimentos abertos.

        :return: Uma consulta contendo os IDs dos movimentos abertos para o terceiro.
        """

        idsMov = DB.session.query(CDA016.id_movTerc).filter(CDA016.id_terceiro==id)

        return idsMov
    

    def consultaTerceiro(self, idMov: int) -> CDA009:
        """
        Consulta as informações de um terceiro com base no ID de um movimento.

        :param idMov: O ID do movimento para o qual se deseja consultar as informações do terceiro.

        :return: O nome do terceiro associado ao movimento.
        """

        terceiro = DB.session.query(CDA009.te_nome)\
            .join(CDA016, CDA016.id_terceiro==CDA009.id_terceiro)\
                .filter(CDA009.te_delete!=True, CDA016.id_movTerc==idMov).first()

        return terceiro