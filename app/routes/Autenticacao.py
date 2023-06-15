from flask import Blueprint, request, render_template, redirect, session, flash
from flask_login import login_required
from ..models.Tables import *
from ..models.entity.Usuario import Usuario
from ..models.dao.LoginDao import LoginDao
from ..controllers.ControleLogin import ControleLogin

autenticacao = Blueprint('autenticacao', __name__)


#Rota para efetuar o login no sistema
@autenticacao.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        controleLogin = ControleLogin()
        respLogin = controleLogin.login(request.form["user"].upper(), request.form["pssd"].upper())
        if respLogin == 1: #Redireciona para o acesso de administrador
            session.permanent = True
            return redirect("/adm/dashboard")
        elif respLogin == 2: #Redireciona para o acesso de tecnico de segurança
            session.permanent = True
            return redirect("/tec/dashboard")
        elif respLogin == 3: #Redireciona para o acesso de vigilante
            session.permanent = True
            return redirect("/vig/dashboard")
        elif respLogin == 4:
            flash("Usuário/Senha incorreto!")
            return redirect("/index")
        elif respLogin == 5:
            flash("Usuário inativo ou deletado")
            return redirect("/index")
        else:
            flash("Usuário não existe")
            return redirect("/index")


#Rota para efetuar logout no sistema
@autenticacao.route('/logout', methods=['GET'])
@login_required
def logout():
    controleLogin = ControleLogin()
    controleLogin.logout()
    return redirect("/")
