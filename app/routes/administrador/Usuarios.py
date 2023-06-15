from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from flask_login import login_required
from ...controllers.ControleManterUsuario import ControleManterUsuario

usuarioAdm = Blueprint("usuarioAdm", __name__)

#Rota para a listagem de usuários
@usuarioAdm.route('/adm/lista-usuarios', methods=["GET"])
def listaUsuariosAdm():
    context = {"titulo": "Listagem de Usuários", "active": "cadUser"}
    return render_template("administrador/usuario/listaUsuarios.html", context=context)


#Rota para a listagem de usuários
@usuarioAdm.route('/adm/lista-usuarios', methods=["POST"])
def listaUsuariosAPI():
    controleManterUsuario = ControleManterUsuario()
    respControle = controleManterUsuario.mostarUsuarios()
    return jsonify(respControle)


#Rota para a tela de cadastro de usuários
@usuarioAdm.route('/adm/cadastro-usuario', methods=["GET"])
def cadastroUsuarioAdm():
    context = {"titulo": "Cadastro de Usuário", "action": f"{url_for('usuarioAdm.insertUsuarioAdm')}" ,"botao": "Cadastrar", "active": "cadUser"}
    return render_template("administrador/usuario/cadastroUsuario.html", context=context)


#Rota para inserir usuário
@usuarioAdm.route('/adm/cadastro-usuario',  methods=["POST"])
def insertUsuarioAdm():
    if request.method == "POST":
        controleManterUsuario = ControleManterUsuario()
        if controleManterUsuario.incluirUsuario(request.form["nome"].upper(), request.form["usuario"].upper(), request.form["email"].upper(), request.form["grupo"], request.form["senha"].upper()):
            flash("Usuário incluido com sucesso!", "success")
            return redirect(url_for("usuarioAdm.listaUsuariosAdm"))
        else:
            return print("deu ruim")


#Rota para a tela para editar o usuário
@usuarioAdm.route('/adm/editar-usuario/<id>',  methods=["GET"])
def editarUsuarioAdm(id):
    controleManterUsuario = ControleManterUsuario()
    usuario = controleManterUsuario.mostarUsuarioDetalhado(id)
    context = {"titulo": "Alterar Usuário", "action": f"{url_for('usuarioAdm.editUsuarioAdm')}", "botao": "Editar", "usuario": usuario, "active": "cadUser"}
    return render_template("administrador/usuario/cadastroUsuario.html", context=context)


#Rota para a tela para editar o usuário
@usuarioAdm.route('/adm/editar-usuario',  methods=["POST"])
def editUsuarioAdm():
    controleManterUsuario = ControleManterUsuario()
    if controleManterUsuario.editarUsuario(request.form["id"], request.form["nome"].upper(), request.form["usuario"].upper(), request.form["email"].upper(), request.form["grupo"], request.form["senha"].strip()):
        flash("Usuário alterado com sucesso!", "success")
        return redirect(url_for("usuarioAdm.listaUsuariosAdm"))
    else:
        return print("deu ruim")
    

#Rota para a tela com modal de confirmação de exclusão do usuário
@usuarioAdm.route('/adm/excluir-usuario/<id>',  methods=["GET"])
def deleteUsuarioAdm(id):
    controleManterUsuario = ControleManterUsuario()
    respControle = controleManterUsuario.excluirUsuario(int(id))
    if respControle == 2:
        flash("Usuário excluido com sucesso!", "success")
        return redirect(url_for("usuarioAdm.listaUsuariosAdm"))
    elif respControle == 0:
        flash("Deu ruim", "danger")
        return redirect(url_for("usuarioAdm.listaUsuariosAdm"))
    else:
        flash("Usuário logado não pode ser excluido", "danger")
        return redirect(url_for("usuarioAdm.listaUsuariosAdm"))
