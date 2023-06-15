from flask import Blueprint, render_template
from flask_login import login_required

dashAdm = Blueprint("dashAdm", __name__)


#Rota para a dashboard do admin
@dashAdm.route('/adm/dashboard')
@login_required
def dashboardAdm():
    context = {"titulo": "Dashboard"}
    return render_template("administrador/dashboard.html", context=context)