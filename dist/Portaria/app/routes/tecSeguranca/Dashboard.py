from flask import Blueprint, render_template
from flask_login import login_required

dashTec = Blueprint("dashTec", __name__)


#Rota para a dashboard dos Tecnicos de Segurança
@dashTec.route('/tec/dashboard')
@login_required
def dashboardTec():
    context = {"titulo": "Dashboard"}
    return render_template("tecSeguranca/dashboard.html", context=context)