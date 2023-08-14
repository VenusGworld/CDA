from flask import Blueprint, render_template, abort, request
from ...extensions.LogErro import LogErro
from flask_login import login_required
import traceback
import sys

dashTecBlue = Blueprint("dashTecBlue", __name__)


#Rota para a dashboard dos Tecnicos de Segurança
@dashTecBlue.route('/dashboard')
@login_required
def dashboardTec():
    try:
        context = {"titulo": "Dashboard"}
        return render_template("tecSeguranca/dashboard.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)