from flask import Blueprint, render_template
from flask_login import login_required

dashAdmBlue = Blueprint("dashAdmBlue", __name__)


#Rota para a dashboard do admin
@dashAdmBlue.route('/adm/dashboard')
@login_required
def dashboardAdm():
    context = {"titulo": "Dashboard", "active": "dashboard"}
    return render_template("administrador/dashboard.html", context=context)