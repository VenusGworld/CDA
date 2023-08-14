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
@logUserAdmBlue.route("/log/log-manter-usuario")
@login_required
def listagemLog():
    try:
        context = {"titulo": "Logs Manter Usuário", "active": "logUser"}
        return render_template("administrador/logUsuario/cosultaLogUser.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)