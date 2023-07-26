from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash, abort
from flask_login import login_required
from ...controllers.ControleManterUsuario import ControleManterUsuario
from ...extensions.LogErro import LogErro
import sys
import traceback

logUserAdmBlue = Blueprint("logUserAdmBlue", __name__)

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
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)