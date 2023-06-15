from flask import Blueprint, render_template
from flask_login import login_required

dashVig = Blueprint("dashVig", __name__)


#Rota para a dashboard dos Vigilantes
@dashVig.route('/vig/dashboard')
@login_required
def dashboardVig():
    context = {"titulo": "Dashboard"}
    return render_template("vigilante/dashboard.html", context=context)