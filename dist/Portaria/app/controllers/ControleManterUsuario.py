from ..models.entity.Usuario import Usuario
from ..models.entity.Log import Log
from ..models.dao.ManterUsuarioDao import ManterUsuarioDao
from ..models.dao.ConsultaIdsDao import ConsultaIds
from ..models.dao.GeraLogUsuarioDao import GeraLogUsuarioDao
from datetime import datetime

class ControleManterUsuario:
    
    def incluirUsuario(self, nome: str, user: str, email: str, grupo: str, senha: str) -> bool:
        self.usuario = Usuario()
        self.usuario.set_nome(nome)
        self.usuario.set_email(email)
        self.usuario.set_usuario(user)
        self.usuario.set_grupo(grupo)
        self.usuario.gerarSenha(senha)
        self.usuario.set_ativo(False)
        self.usuario.set_delete(False)

        manterUsuarioDao = ManterUsuarioDao()
        if manterUsuarioDao.inserirUsuario(self.usuario):
            #Consulta o ultimo id da tabela
            consultaIdUser = ConsultaIds()
            self.usuario.set_id(consultaIdUser.consultaIdUsuario())
            #Gera Log
            self.geraLogUsuario()
            return True
        else:
            return False

    def geraLogUsuario(self):
        log = Log()
        log.set_acao("INSERT")
        log.set_dataHora(datetime.now())
        log.set_observacao("")
        log.set_usuario(self.usuario)
        log.set_dadosAntigos({"vazio": 0})
        log.set_dadosNovos({"vazio": 0})

        logDao = GeraLogUsuarioDao()
        logDao.inserirLog(log)


