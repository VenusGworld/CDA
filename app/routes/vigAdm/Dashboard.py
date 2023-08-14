from flask import Blueprint, render_template, abort, request
from ...extensions.LogErro import LogErro
from flask_login import login_required
import traceback
import sys

dashVigBlue = Blueprint("dashVigBlue", __name__)


#Rota para a dashboard dos Vigilantes
@dashVigBlue.route('/dashboard', methods=["GET"])
@login_required
def dashboard():
    try:
        context = {"titulo": "Dashboard", "active": "dashboard"}
        return render_template("vigAdm/dashboard/dashboard.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)