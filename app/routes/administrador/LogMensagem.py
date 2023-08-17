from flask import Blueprint, render_template, request, abort
from ...extensions.LogErro import LogErro
from flask_login import login_required
import traceback
import sys


logMenAdmBlue = Blueprint("logMenAdmBlue", __name__)

##############################################################
# Rotas relacionadas aos logs das Mensagens
##############################################################

#Rota para tela de log de Mensagem
@logMenAdmBlue.route("/log/log-mensagem")
@login_required
def listagemLog():
    try:
        context = {"titulo": "Logs Mensagem", "active": "logMsg"}
        return render_template("administrador/logMansagem/cosultaLogMen.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)