from flask import Blueprint, render_template, abort, request
from flask_login import login_required
from ...extensions.LogErro import LogErro
import sys
import traceback

dashAdmBlue = Blueprint("dashAdmBlue", __name__)


#Rota para a dashboard do admin
@dashAdmBlue.route('/dashboard')
@login_required
def dashboardAdm():
    try:
        context = {"titulo": "Dashboard", "active": "dashboard"}
        return render_template("administrador/dashboard.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)