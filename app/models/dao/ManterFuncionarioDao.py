from ..entity.Funcionario import Funcionario
from ..Tables import CDA007
from ...configurations.Database import DB
import sys

class ManterFuncionarioDao:

    def mostarFuncionarios(self) -> CDA007:
        funcionarios = CDA007.query.filter(CDA007.fu_delete!=True).order_by(CDA007.fu_nome)

        return funcionarios
    

    def mostarFuncionarioDetalhado(self, id: int) -> Funcionario:
        if id != None:
            func = CDA007.query.get(id)
            funcionario = Funcionario()
            funcionario.id = id
            funcionario.cracha = func.fu_cracha
            funcionario.nome = func.fu_nome
            funcionario.gerente = func.fu_gerente
            funcionario.maquina = func.fu_maquina
            funcionario.ativo = func.fu_ativo
            funcionario.delete = func.fu_delete
            return funcionario
        else:
            return Funcionario()
    

    def mostarFuncionarioDetalhadoCracha(self, cracha: str) -> Funcionario:
        func = CDA007.query.filter(CDA007.fu_cracha==cracha).first()

        funcionario = Funcionario()
        funcionario.id = func.id_funcionarios
        funcionario.cracha = func.fu_cracha
        funcionario.nome = func.fu_nome
        funcionario.gerente = func.fu_gerente
        funcionario.maquina = func.fu_maquina
        funcionario.ativo = func.fu_ativo
        funcionario.delete = func.fu_delete

        return funcionario
    
    def editarFuncionario(self, funcionario: Funcionario) -> bool:
        func = CDA007.query.get(funcionario.id)
        func.fu_cracha = funcionario.cracha
        func.fu_nome = funcionario.nome
        func.fu_maquina = funcionario.maquina
        func.fu_gerente = funcionario.gerente
        func.fu_ativo = funcionario.ativo
        func.fu_delete = funcionario.delete

        DB.session.commit()
        return True

    def inativarFuncionario(self, id: int) -> bool:
        func = CDA007.query.get(id)
        func.fu_ativo = True

        DB.session.commit()
        return True
    

    def excluirFuncionario(self, id: int) -> bool:
        func = CDA007.query.get(id)
        func.fu_delete = True

        DB.session.commit()
        return True


    def inserirFuncionario(self, funcionario: Funcionario) -> bool:
        func  = CDA007(funcionario.cracha, funcionario.nome, funcionario.ativo, funcionario.delete, funcionario.gerente, funcionario.maquina)
        
        DB.session.add(func)
        DB.session.commit()
        return True
        
        
    def verificarFuncionario(self, cracha: str) -> bool:
        func = CDA007.query.filter(CDA007.fu_cracha==cracha).first()

        if func:
            return True
        else: 
            return False


    def alterarIntegracao(self, funcionario: Funcionario) -> bool:
        func = CDA007.query.filter(CDA007.fu_cracha==funcionario.cracha).first()
        func.fu_cracha = funcionario.cracha
        func.fu_nome = funcionario.nome

        DB.session.commit()
        return True
        


