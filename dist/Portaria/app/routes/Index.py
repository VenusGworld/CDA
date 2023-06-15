from flask import Blueprint, render_template
from ..models.Tables import *

index = Blueprint("index", __name__)


#Rota o index do sistema
@index.route("/")
@index.route("/index")
def indeX():
    return render_template("index.html")


#Rota para exibir Modal para preencher os dados para a recuperação da senha
@index.route("/esqueci-senha-modal")
def esqueciSenha():
    contexto = {"modal": 1} #Dcionário com as váriaveis parta utilizar no template
    return render_template("index.html", contexto=contexto)