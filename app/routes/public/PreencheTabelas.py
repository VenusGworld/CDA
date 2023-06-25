from flask import Blueprint, jsonify
from flask_login import login_required
from ...controllers.ControleManterUsuario import ControleManterUsuario
from ...controllers.ControleChave import ControleCrontoleDeChave
from ...controllers.ControleManterFuncionario import ControleManterFuncionario

preencheTabelasBlue = Blueprint("preencheTabelasBlue", __name__)

#Rota para a listagem de Usuários
@preencheTabelasBlue.route('/lista-usuarios', methods=["POST"])
@login_required
def listaUsuariosAPI():
    controleManterUsuario = ControleManterUsuario()
    respControle = controleManterUsuario.mostarUsuarios()
    return jsonify(respControle)


#Rota para a listagem Chaves retiradas
@preencheTabelasBlue.route('/lista-chaves-retiradas', methods=["POST"])
@login_required
def listaChavesRetAPI():
    controleManterChave = ControleCrontoleDeChave()
    respControle = controleManterChave.listaChavesRetiradas()
    return jsonify(respControle)


#Rota para a listagem Chaves retiradas
@preencheTabelasBlue.route('/lista-funcionarios', methods=["POST"])
@login_required
def listaFuncionariosAPI():
    controleManterFuncionario = ControleManterFuncionario()
    respControle = controleManterFuncionario.mostarFuncionarios()
    return jsonify(respControle)
