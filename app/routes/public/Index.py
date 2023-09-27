from flask import Blueprint, render_template, session
from ...controllers.ControleLogin import ControleLogin
from ...models.dao.BaseDados import BaseDados


indexBlue = Blueprint("indexBlue", __name__)

##############################################################
# Rotas relacionadas ao Index do sistema
##############################################################

#Rota o index do sistema
@indexBlue.route("/", methods=['GET'])
@indexBlue.route("/index", methods=['GET'])
def index():
    # session["base"] = BaseDados.verificaBase()
    controleLogin = ControleLogin()
    quantide = controleLogin.verificaQuantidadeUser()
    context = {"qtde": quantide}
    return render_template("public/index.html", context=context)