from ..entity.Funcionario import Funcionario
from ...configurations.Database import DB
from ..Tables import CDA007

class ManterFuncionarioDao:
    """
    Classe Dao para o manter Funcionário
    @tables - CDA007
    @author - Fabio
    @version - 1.0
    @since - 10/07/2023
    """

    def consultarFuncionarios(self) -> CDA007:
        """
        Consulta os funcionários que não estão inativos ou deletados cadastradas no sistema.

        :return: Uma lista de funcionários ordenados pelo nome.
        """

        funcionarios = CDA007.query.filter(CDA007.fu_delete!=True).order_by(CDA007.fu_nome)

        return funcionarios
    

    def consultarFuncionarioDetalhado(self, id: int) -> Funcionario:
        """
        Consulta e retorna os detalhes de um funcionário específico com base no seu ID.

        :param id: O ID do funcionário que se deseja consultar os detalhes.

        :return: Um objeto Funcionario contendo os detalhes do funcionário consultado.
        """

        if id != None:
            func = CDA007.query.get(id)
            funcionario = Funcionario(id=id, cracha=func.fu_cracha, nome=func.fu_nome, gerente=func.fu_gerente,
                                      maquina=func.fu_maquina, ativo=func.fu_inativo, delete=func.fu_delete)
            
            return funcionario
        else:
            return Funcionario()
    

    def consultarFuncionarioDetalhadoCracha(self, cracha: str) -> Funcionario:
        """
        Consulta e retorna os detalhes de um funcionário específico com base no seu crachá.

        :param crachá: O crachá do funcionário que se deseja consultar os detalhes.

        :return: Um objeto Funcionario contendo os detalhes do funcionário consultado.
        """

        func = CDA007.query.filter(CDA007.fu_cracha==cracha).first()
        funcionario = Funcionario(id=func.id_funcionario, cracha=func.fu_cracha, nome=func.fu_nome, gerente=func.fu_gerente,
                                      maquina=func.fu_maquina, ativo=func.fu_inativo, delete=func.fu_delete)

        return funcionario
    

    def editarFuncionario(self, funcionario: Funcionario) -> bool:
        """
        Edita as informações de um funcionário no banco de dados.

        :param funcionario: O objeto Funcionario com as informações atualizadas do funcionário.

        :return: True se a edição for bem-sucedida, False caso contrário.
        """

        func = CDA007.query.get(funcionario.id)
        func.fu_cracha = funcionario.cracha
        func.fu_nome = funcionario.nome
        func.fu_maquina = funcionario.maquina
        func.fu_gerente = funcionario.gerente
        func.fu_inativo = funcionario.ativo
        func.fu_delete = funcionario.delete

        DB.session.commit()
        return True


    def inativarFuncionario(self, id: int) -> bool:
        """
        Marca um funcionário como inativo no sistema.

        :param id: O ID do funcionário a ser inativado.

        :return: True se a inativação for bem-sucedida, False caso contrário.
        """

        func = CDA007.query.get(id)
        func.fu_inativo = True

        DB.session.commit()
        return True
    

    def excluirFuncionario(self, id: int) -> bool:
        """
        Marca um funcionário como excluído no sistema.

        :param id: O ID do funcionário a ser inativado.

        :return: True se a inativação for bem-sucedida, False caso contrário.
        """

        func = CDA007.query.get(id)
        func.fu_delete = True

        DB.session.commit()
        return True


    def inserirFuncionario(self, funcionario: Funcionario) -> bool:
        """
        Insere um novo funcionário no banco de dados.

        :param funcionario: O objeto Funcionario contendo as informações do novo funcionário.

        :return: True se a inserção for bem-sucedida, False caso contrário.
        """

        func  = CDA007(funcionario.cracha, funcionario.nome, funcionario.ativo, funcionario.delete, funcionario.gerente, funcionario.maquina)
        
        DB.session.add(func)
        DB.session.commit()
        return True
        
        
    def verificarFuncionario(self, cracha: str) -> bool:
        """
        Verifica se um funcionário com o crachá especificado já existe no banco de dados.

        :param cracha: O número de crachá do funcionário a ser verificado.

        :return: True se o funcionário com o crachá existir, False caso contrário.
        """

        func = CDA007.query.filter(CDA007.fu_cracha==cracha).first()

        if func:
            return True
        else: 
            return False


    def editarFuncionarioIntegra(self, funcionario: Funcionario) -> bool:
        """
        Altera os dados do funcionário que veio através da integração.

        :param funcionario: O objeto Funcionario com as informações crachá e nome atualizadas do funcionário.

        :return: True se a edição for bem-sucedida, False caso contrário.
        """

        func = CDA007.query.filter(CDA007.fu_cracha==funcionario.cracha).first()
        func.fu_cracha = funcionario.cracha
        func.fu_nome = funcionario.nome

        DB.session.commit()
        return True
        


