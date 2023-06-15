from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from ...controllers.ControleManterUsuario import ControleManterUsuario

usuarioAdm = Blueprint("usuarioAdm", __name__)

#Rota para a listagem de usuários
@usuarioAdm.route('/adm/lista-usuarios', methods=["GET"])
def listaUsuariosAdm():
    context = {"titulo": "Listagem de Usuários"}
    return render_template("administrador/usuario/listaUsuarios.html", context=context)


#Rota para a tela de cadastro de usuários
@usuarioAdm.route('/adm/cadastro-usuario', methods=["GET"])
def cadastroUsuarioAdm():
    context = {"titulo": "Cadastro de Usuário", "botao": "Cadastrar"}
    return render_template("administrador/usuario/cadastroUsuario.html", context=context)


#Rota para inserir usuário
@usuarioAdm.route('/adm/cadastro-usuario',  methods=["POST"])
def insertUsuarioAdm():
    if request.method == "POST":
        controleManterUsuario = ControleManterUsuario()
        if controleManterUsuario.incluirUsuario(request.form["nome"].upper(), request.form["usuario"].upper(), request.form["email"].upper(), request.form["grupo"], request.form["senha"].upper()):
            redirect(url_for("usuarioAdm.listaUsuariosAdm"))
        else:
            print("deu ruim")