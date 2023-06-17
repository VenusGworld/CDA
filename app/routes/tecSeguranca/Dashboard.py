from flask import Blueprint, render_template
from flask_login import login_required

dashTecBlue = Blueprint("dashTecBlue", __name__)


#Rota para a dashboard dos Tecnicos de Segurança
@dashTecBlue.route('/tec/dashboard')
@login_required
def dashboardTec():
    context = {"titulo": "Dashboard"}
    return render_template("tecSeguranca/dashboard.html", context=context)