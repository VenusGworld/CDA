from ..models.entity.Usuario import Usuario
from ..models.entity.Log import Log
from ..models.dao.ManterUsuarioDao import ManterUsuarioDao
from ..models.dao.ConsultaIdsDao import ConsultaIds
from ..models.dao.GeraLogUsuarioDao import GeraLogUsuarioDao
from ..models.dao.VerificamovimentoDao import VerificaMovimentoDao
from datetime import datetime
from flask import session

class ControleManterUsuario:

    def mostarUsuarios(self) -> list:
        manterUsuarioDao = ManterUsuarioDao()
        usuarios = manterUsuarioDao.mostarUsuarios()
        listaDados = []
        for usuario in usuarios:
            dicUser = {
                "id": usuario.get_id(),
                "nome": usuario.get_nome(),
                "usuario": usuario.get_usuario(),
                "grupo": usuario.get_grupo(),
            }

            listaDados.append(dicUser)

        return listaDados
    

    def mostarUsuarioDetalhado(self, id: int) -> Usuario:
        manterUsuarioDao = ManterUsuarioDao()
        usuario = manterUsuarioDao.mostarUsuarioDetalhado(id)
        
        return usuario

    
    def incluirUsuario(self, nome: str, user: str, email: str, grupo: str, senha: str) -> bool:
        self.usuarioNovo = Usuario()
        self.usuarioNovo.set_nome(nome)
        self.usuarioNovo.set_email(email)
        self.usuarioNovo.set_usuario(user)
        self.usuarioNovo.set_grupo(grupo)
        self.usuarioNovo.gerarSenha(senha)
        self.usuarioNovo.set_ativo(False)
        self.usuarioNovo.set_delete(False)

        self.usuarioLogado = Usuario()

        manterUsuarioDao = ManterUsuarioDao()
        if manterUsuarioDao.inserirUsuario(self.usuarioNovo):
            #Consulta o ultimo id da tabela
            consultaIdUser = ConsultaIds()
            self.usuarioLogado.set_id(consultaIdUser.consultaIdUserLogado(session["usuario"]))
            self.usuarioNovo.set_id(consultaIdUser.consultaIdFinalUser())
            #Gera Log
            self.geraLogUsuario("INSERT")
            return True
        else:
            return False
        
    def editarUsuario(self, id: int, nome: str, user: str, email: str, grupo: str, senha: str) -> bool:
        self.usuarioNovo = Usuario()
        self.usuarioLogado = Usuario()
        self.usuarioAntigo = Usuario()
        manterUsuarioDao = ManterUsuarioDao()
        consultaIdUser = ConsultaIds()    

        self.usuarioAntigo = manterUsuarioDao.mostarUsuarioDetalhado(id)

        self.usuarioNovo.set_id(id)
        self.usuarioNovo.set_nome(nome)
        self.usuarioNovo.set_email(email)
        self.usuarioNovo.set_usuario(user)
        self.usuarioNovo.set_grupo(grupo)
        self.usuarioNovo.set_senha(senha)
        self.usuarioNovo.set_ativo(False)
        self.usuarioNovo.set_delete(False)
        self.usuarioNovo.set_complex(self.usuarioAntigo.get_complex())

        if self.usuarioAntigo.get_senha() != self.usuarioNovo.get_senha():
            self.usuarioNovo.gerarSenha(senha.upper())

        if manterUsuarioDao.editarUsuario(self.usuarioNovo):
            #Consulta o ultimo id da tabela
            self.usuarioLogado.set_id(consultaIdUser.consultaIdUserLogado(session["usuario"]))
            #Gera Log
            self.geraLogUsuario("UPDATE")
            return True
        else:
            return False
        
    
    def excluirUsuario(self, id: int) -> int:
        manterUsuarioDao = ManterUsuarioDao()
        verificaMovimentoDao = VerificaMovimentoDao()
        consultaIdUser = ConsultaIds()
        self.usuarioLogado = Usuario()
        self.usuarioAntigo = Usuario()

        self.usuarioAntigo = manterUsuarioDao.mostarUsuarioDetalhado(id)

        self.usuarioLogado.set_id(consultaIdUser.consultaIdUserLogado(session["usuario"]))

        if id == self.usuarioLogado.get_id():
            return 1
        else:
            if verificaMovimentoDao.verificaMovimentoUsuario(id):
                if manterUsuarioDao.excluirUsuario(id, 2):
                    self.geraLogUsuario("ACTIVE")
                    return 2
                else:
                    return 0
                
            else:
                if manterUsuarioDao.excluirUsuario(id, 1):
                    self.geraLogUsuario("DELETE")
                    return 2
                else:
                    return 0


    def geraLogUsuario(self, acao: str):
        log = Log()
        log.set_acao(acao)
        log.set_dataHora(datetime.now())
        log.set_observacao("")
        log.set_usuario(self.usuarioLogado)

        if acao == "INSERT":
            log.set_dadosAntigos({"vazio": 0})
            log.set_dadosNovos(self.usuarioNovo.toJson())
        elif acao == "UPDATE":
            log.set_dadosAntigos(self.usuarioAntigo.toJson())
            log.set_dadosNovos(self.usuarioNovo.toJson())
        else:
            log.set_dadosAntigos(self.usuarioAntigo.toJson())
            log.set_dadosNovos({"vazio": 0})

        logDao = GeraLogUsuarioDao()
        logDao.inserirLog(log)


