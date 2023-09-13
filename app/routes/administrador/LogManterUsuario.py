from ...controllers.ControleConsultaParametros import ControleConsultaParametros
from ...controllers.ControleConsultarLogUser import ControleConsultarLogUser
from flask import Blueprint, render_template, request, abort
from ...extensions.LogErro import LogErro
from flask_login import login_required
import traceback
import sys


logUserAdmBlue = Blueprint("logUserAdmBlue", __name__)

##############################################################
# Rotas relacionadas aos logs do CRUD de usuário
##############################################################

#Rota para tela de log de usuários
@logUserAdmBlue.route("/log/log-manter-usuario", methods=["GET"])
@login_required
def listagemLogUser():
    try:
        constroleConsultaParametros = ControleConsultaParametros()
        meses = constroleConsultaParametros.consultaParametros("PAR_LOG_MANT_USER")
        context = {"titulo": "Logs Manter Usuário", "active": "logUser", "meses": meses}
        return render_template("administrador/logUsuario/cosultaLogUser.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para tela com modal para visualização detalhada dos logs do usuário
@logUserAdmBlue.route("/log/log-manter-usuario/<id>", methods=["GET"])
@login_required
def vizualizarLog(id):
    try:
        controleConsultarLogUser = ControleConsultarLogUser()
        log = controleConsultarLogUser.consultaLogUsertDetelhado(int(id))
        if log.acao == "INSERT":
            modal = 1
        elif log.acao == "UPDATE":
            modal = 2
        elif log.acao in ["DELETE", "ACTIVE"]:
            modal = 3
        context = {"titulo": "Logs Manter Usuário", "active": "logUser", "modal": modal, "log": log}
        return render_template("administrador/logUsuario/cosultaLogUser.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)