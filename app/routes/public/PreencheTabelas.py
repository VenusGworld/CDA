from ...controllers.ControleConsultarLogControlChav import ControleConsultarLogControlChav
from ...controllers.ControleConsultarLogControlTerc import ControleConsultarLogControlTerc
from ...controllers.ControleConsultarLogControlGer import ControleConsultarLogControlGer
from ...controllers.ControleManterFuncionario import ControleManterFuncionario
from ...controllers.ControleConsultarLogChave import ControleConsultarLogChave
from ...controllers.ControleConsultarLogTerc import ControleConsultarLogTerc
from ...controllers.ControleConsultarLogUser import ControleConsultarLogUser
from ...controllers.ControleConsultarLogFunc import ControleConsultarLogFunc
from ...controllers.ControleConsultarLogMen import ControleConsultarLogMen
from ...controllers.ControleManterTerceiro import ControleManterTerceiro
from ...controllers.ControleManterUsuario import ControleManterUsuario
from ...controllers.ControleManterChave import ControleManterChave
from ...controllers.ControleTerceiro import ControleTerceiro
from ...controllers.ControleGerente import ControleDeGerente
from ...controllers.ControleChave import ControleChave
from flask import Blueprint, session, request, Response
from flask_login import login_required
import json

preencheTabelasBlue = Blueprint("preencheTabelasBlue", __name__)

##############################################################
# Rotas relacionadas ao preenchimento de tabelas
##############################################################

#Rota para preencher a lista de Usuários
@preencheTabelasBlue.route('/lista-usuarios', methods=["POST"])
@login_required
def listaUsuariosAPI():
    controleManterUsuario = ControleManterUsuario()
    respControle = controleManterUsuario.consultarUsuarios()
    
    resp = Response(response=json.dumps(respControle), status=200, mimetype="application/json")
    return resp


#Rotapara para preencher a lista de Chaves retiradas
@preencheTabelasBlue.route('/lista-chaves-retiradas', methods=["POST"])
@login_required
def listaChavesRetAPI():
    controleChave = ControleChave()
    respControle = controleChave.listaChavesRetiradas()

    resp = Response(response=json.dumps({"login": session["grupo"], "data": respControle}), status=200, mimetype="application/json")
    return resp


#Rotapara para preencher a lista de Movimento de Chaves
@preencheTabelasBlue.route('/lista-chaves-manutencao', methods=["POST"])
@login_required
def listaChavesManutAPI():
    controleChave = ControleChave()
    respControle = controleChave.listaChavesManut()

    resp = Response(response=json.dumps({"login": session["grupo"], "data": respControle}), status=200, mimetype="application/json")
    return resp


#Rota para preencher a lista de Funcionários
@preencheTabelasBlue.route('/lista-funcionarios', methods=["POST"])
@login_required
def listaFuncionariosAPI():
    controleManterFuncionario = ControleManterFuncionario()
    respControle = controleManterFuncionario.consultarFuncionarios()

    resp = Response(response=json.dumps(respControle), status=200, mimetype="application/json")
    return resp


#Rota para preencher a lista de Chaves
@preencheTabelasBlue.route('/lista-chaves', methods=["POST"])
@login_required
def listaChavesAPI():
    controleManterChave = ControleManterChave()
    respControle = controleManterChave.consultaChaves()

    resp = Response(response=json.dumps({"login": session["grupo"], "data": respControle}), status=200, mimetype="application/json")
    return resp


#Rota para preencher a lista de Terceiros
@preencheTabelasBlue.route('/lista-terceiros', methods=["POST"])
@login_required
def listaTerceirosAPI():
    controleManterTerceiro = ControleManterTerceiro()
    respControle = controleManterTerceiro.consultarTerceiros()

    resp = Response(response=json.dumps({"login": session["grupo"], "data": respControle}), status=200, mimetype="application/json")
    return resp


#Rota para preencher a lista de Terceiros que entraram
@preencheTabelasBlue.route('/lista-terceiros-entradas', methods=["POST"])
@login_required
def listaTerceirosEntradaAPI():
    controleTerceiro = ControleTerceiro()
    respControle = controleTerceiro.consultaTerceirosEntrada()

    resp = Response(response=json.dumps({"login": session["grupo"], "data": respControle}), status=200, mimetype="application/json")
    return resp


#Rota para preencher a lista de Terceiros que entraram
@preencheTabelasBlue.route('/lista-gerentes-entradas', methods=["POST"])
@login_required
def listaGerestesEntradaAPI():
    controlegerente = ControleDeGerente()
    respControle = controlegerente.consultaGerentesEntrada()

    resp = Response(response=json.dumps({"login": session["grupo"], "data": respControle}), status=200, mimetype="application/json")
    return resp


#Rotapara para preencher a lista de manutenção de Movimento de Gerentes
@preencheTabelasBlue.route('/lista-gerentes-manutencao', methods=["POST"])
@login_required
def listaGerManutAPI():
    controleDeGerente = ControleDeGerente()
    respControle = controleDeGerente.listaGerentesManut()

    resp = Response(response=json.dumps({"login": session["grupo"], "data": respControle}), status=200, mimetype="application/json")
    return resp


#Rotapara para preencher a lista de Movimento de Terceiro
@preencheTabelasBlue.route('/lista-terceiro-manutencao', methods=["POST"])
@login_required
def listaTerceiroManutAPI():
    controleTerceiro = ControleTerceiro()
    respControle = controleTerceiro.listaTercManut()

    resp = Response(response=json.dumps({"login": session["grupo"], "data": respControle}), status=200, mimetype="application/json")
    return resp


#Rota para preencher a lista de logs de usuários
@preencheTabelasBlue.route('/lista-logs-usuario', methods=["POST"])
@login_required
def listaLogsUserAPI():
    data = request.get_json()
    controleConsultaLogUser = ControleConsultarLogUser()
    respControle = controleConsultaLogUser.consultaLogUserInsert(data["acao"])
    
    resp = Response(response=json.dumps(respControle), status=200, mimetype="application/json")
    return resp


#Rota para preencher a lista de logs de usuários
@preencheTabelasBlue.route('/lista-logs-funcionarios', methods=["POST"])
@login_required
def listaLogsFuncAPI():
    data = request.get_json()
    controleConsultaLogFunc = ControleConsultarLogFunc()
    respControle = controleConsultaLogFunc.consultaLogFunc(data["acao"])
    
    resp = Response(response=json.dumps(respControle), status=200, mimetype="application/json")
    return resp


#Rota para preencher a lista de logs de MEnsagens
@preencheTabelasBlue.route('/lista-logs-mensagens', methods=["POST"])
@login_required
def listaLogsMenAPI():
    controleConsultarLogMen = ControleConsultarLogMen()
    respControle = controleConsultarLogMen.consultaLogMen()
    resp = Response(response=json.dumps(respControle), status=200, mimetype="application/json")
    return resp


#Rota para preencher a lista de logs de chaves
@preencheTabelasBlue.route('/lista-logs-chaves', methods=["POST"])
@login_required
def listaLogsChaveAPI():
    data = request.get_json()
    controleConsultarLogChave = ControleConsultarLogChave()
    respControle = controleConsultarLogChave.consultaLogChave(data["acao"])
    
    resp = Response(response=json.dumps({"login": session["grupo"], "data": respControle}), status=200, mimetype="application/json")
    return resp


#Rota para preencher a lista de logs de terceiros
@preencheTabelasBlue.route('/lista-logs-terceiros', methods=["POST"])
@login_required
def listaLogsTerceiroAPI():
    data = request.get_json()
    controleConsultarLogTerc = ControleConsultarLogTerc()
    respControle = controleConsultarLogTerc.consultaLogTerc(data["acao"])
    
    resp = Response(response=json.dumps({"login": session["grupo"], "data": respControle}), status=200, mimetype="application/json")
    return resp


#Rota para preencher a lista de logs de controle de chaves
@preencheTabelasBlue.route('/lista-logs-controle-chaves', methods=["POST"])
@login_required
def listaLogsControlChavesAPI():
    data = request.get_json()
    controleConsultarLogControlChav = ControleConsultarLogControlChav()
    respControle = controleConsultarLogControlChav.consultaLogControlChave(data["acao"])
    
    resp = Response(response=json.dumps({"login": session["grupo"], "data": respControle}), status=200, mimetype="application/json")
    return resp


#Rota para preencher a lista de logs de controle de terceiros
@preencheTabelasBlue.route('/lista-logs-controle-terceiros', methods=["POST"])
@login_required
def listaLogsControlTerceirosAPI():
    data = request.get_json()
    controleConsultarLogControlTerc = ControleConsultarLogControlTerc()
    respControle = controleConsultarLogControlTerc.consultaLogControlTercEnt(data["acao"])
    
    resp = Response(response=json.dumps({"login": session["grupo"], "data": respControle}), status=200, mimetype="application/json")
    return resp


#Rota para preencher a lista de logs de controle de gerentes
@preencheTabelasBlue.route('/lista-logs-controle-gerentes', methods=["POST"])
@login_required
def listaLogsControlGerentesAPI():
    data = request.get_json()
    controleConsultarLogControlGer = ControleConsultarLogControlGer()
    respControle = controleConsultarLogControlGer.consultaLogControlGer(data["acao"])
    
    resp = Response(response=json.dumps({"login": session["grupo"], "data": respControle}), status=200, mimetype="application/json")
    return resp