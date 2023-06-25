from flask import Blueprint, render_template, abort, request
from flask_login import login_required
from ...extensions.Log import LogErro
import sys
import traceback

dashVigBlue = Blueprint("dashVigBlue", __name__)


#Rota para a dashboard dos Vigilantes
@dashVigBlue.route('/dashboard', methods=["GET"])
@login_required
def dashboardVig():
    try:
        context = {"titulo": "Dashboard", "active": "dashboard"}
        return render_template("vigilante/dashboard.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)