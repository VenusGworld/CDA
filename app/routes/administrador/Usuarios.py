from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash, abort
from flask_login import login_required
from ...controllers.ControleManterUsuario import ControleManterUsuario
from ...extensions.Log import LogErro
import sys
import traceback

usuarioAdmBlue = Blueprint("usuarioAdmBlue", __name__)

#Rota para a tela de listagem de usuários
@usuarioAdmBlue.route('/lista-usuarios', methods=["GET"])
@login_required
def listaUsuariosAdm():
    try:
        context = {"titulo": "Listagem de Usuários", "active": "cadUser"}
        return render_template("administrador/usuario/listaUsuarios.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)


#Rota para a tela de cadastro de usuários
@usuarioAdmBlue.route('/cadastro-usuario', methods=["GET"])
@login_required
def cadastroUsuarioAdm():
    try:
        context = {"titulo": "Cadastro de Usuário", "action": f"{url_for('usuarioAdmBlue.insertUsuarioAdm')}", "botao": "Cadastrar", "active": "cadUser"}
        return render_template("administrador/usuario/cadastroUsuario.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)

#Rota para inserir usuário
@usuarioAdmBlue.route('/cadastro-usuario',  methods=["POST"])
@login_required
def insertUsuarioAdm():
    try:
        controleManterUsuario = ControleManterUsuario()
        if controleManterUsuario.incluirUsuario(request.form["nome"].upper().strip(), request.form["usuario"].upper().strip(), request.form["email"].strip(), request.form["grupo"], request.form["senha"].upper().strip()):
            flash("Usuário incluido com sucesso!", "success")
            return redirect(url_for("usuarioAdmBlue.listaUsuariosAdm"))         
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)


#Rota para a tela para editar o usuário
@usuarioAdmBlue.route('/editar-usuario/<id>',  methods=["GET"])
@login_required
def editarUsuarioAdm(id):
    try:
        controleManterUsuario = ControleManterUsuario()
        usuario = controleManterUsuario.mostarUsuarioDetalhado(id)
        context = {"titulo": "Alterar Usuário", "action": f"{url_for('usuarioAdmBlue.editUsuarioAdm')}", "botao": "Editar", "usuario": usuario, "active": "cadUser"}
        return render_template("administrador/usuario/cadastroUsuario.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)


#Rota para editar o usuário
@usuarioAdmBlue.route('/editar-usuario',  methods=["POST"])
@login_required
def editUsuarioAdm():
    try:
        controleManterUsuario = ControleManterUsuario()
        if controleManterUsuario.editarUsuario(request.form["id"], request.form["nome"].upper().strip(), request.form["usuario"].upper().strip(), request.form["email"].strip(), request.form["grupo"], request.form["senha"].strip().strip()):
            flash("Usuário alterado com sucesso!", "success")
            return redirect(url_for("usuarioAdmBlue.listaUsuariosAdm"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)
    

#Rota para a tela com modal de confirmação de exclusão do usuário
@usuarioAdmBlue.route('/excluir-usuario/<id>',  methods=["GET"])
@login_required
def deleteUsuarioAdm(id):
    try: 
        controleManterUsuario = ControleManterUsuario()
        respControle = controleManterUsuario.excluirUsuario(int(id))
        if respControle == 0:
            flash("Deu ruim", "danger")
            return redirect(url_for("usuarioAdmBlue.listaUsuariosAdm"))
        elif respControle == 1:
            flash("Usuário logado não pode ser excluido", "danger")
            return redirect(url_for("usuarioAdmBlue.listaUsuariosAdm"))
        elif respControle == 2:
            flash("Usuário excluido com sucesso!", "success")
            return redirect(url_for("usuarioAdmBlue.listaUsuariosAdm"))
        else:
            flash("Usuário possue movimentação no sistema, então foi desativado", "success")
            return redirect(url_for("usuarioAdmBlue.listaUsuariosAdm"))
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo[-1][0], tracebackInfo[-1][1], request.url)
        abort(500)
        
