from flask import Blueprint, render_template, session
from ...models.dao.BaseDados import BaseDados


indexBlue = Blueprint("indexBlue", __name__)

##############################################################
# Rotas relacionadas ao Index do sistema
##############################################################

#Rota o index do sistema
@indexBlue.route("/")
@indexBlue.route("/index")
def index():
    session["base"] = BaseDados.verificaBase()
    return render_template("public/index.html")


