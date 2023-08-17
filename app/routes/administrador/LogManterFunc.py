from flask import Blueprint, render_template, request, abort
from ...extensions.LogErro import LogErro
from flask_login import login_required
import traceback
import sys


logFuncAdmBlue = Blueprint("logFuncAdmBlue", __name__)

##############################################################
# Rotas relacionadas aos logs do CRUD de Funcionários
##############################################################

#Rota para tela de log de Funcionários
@logFuncAdmBlue.route("/log/log-manter-funcionario")
@login_required
def listagemLog():
    try:
        context = {"titulo": "Logs Manter Funcionário", "active": "logFunc"}
        return render_template("administrador/logFuncionario/cosultaLogFunc.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para tela de log de Funcionários
@logFuncAdmBlue.route("/log/log-manter-funcionario")
@login_required
def vizualizarLog():
    try:
        context = {"titulo": "Logs Manter Funcionário", "active": "logFunc"}
        return render_template("administrador/logFuncionario/cosultaLogFunc.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)