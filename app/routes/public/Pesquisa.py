from flask import Blueprint, jsonify
from ...controllers.ControlePesquisa import ControlePesquisa

pesquisaBlue = Blueprint("pesquisaBlue", __name__)


#Rota para pesquisa de crachas no form do cadastro de usuário
@pesquisaBlue.route('/usuario-pesquisa/<pesquisa>/<int:id>')
def pesquisaUsuarioForm(pesquisa, id):
    controlePesquisa = ControlePesquisa()
    respControle = controlePesquisa.pesquisaUsuario(pesquisa.upper().strip(), id)
    return jsonify(respControle)


#Rota para pesquisa de chaves no input
@pesquisaBlue.route('/chave-pesquisa/<pesquisa>')
def pesquisaChaveInput(pesquisa):
    controlePesquisa = ControlePesquisa()
    respControle = controlePesquisa.pesquisaChave(pesquisa.upper().strip())
    return jsonify(respControle)


#Rota para pesquisa de chaves no input
@pesquisaBlue.route('/funcionario-pesquisa/<pesquisa>')
def pesquisaFuncionarioInput(pesquisa):
    controlePesquisa = ControlePesquisa()
    respControle = controlePesquisa.pesquisaFuncionario(pesquisa.upper().strip())
    return jsonify(respControle)


#Rota para pesquisa de crachas no form do cadastro de funcionário
@pesquisaBlue.route('/cracha-pesquisa/<pesquisa>/<int:id>')
def pesquisaCrachaForm(pesquisa, id):
    controlePesquisa = ControlePesquisa()
    respControle = controlePesquisa.pesquisaCracha(pesquisa.upper().strip(), id)
    return jsonify(respControle)


#Rota para pesquisa de crachas no form do cadastro de funcionário
@pesquisaBlue.route('/maquina-pesquisa/<pesquisa>')
def pesquisaMaquinaForm(pesquisa):
    controlePesquisa = ControlePesquisa()
    respControle = controlePesquisa.pesquisaMaquina(pesquisa.upper().strip())
    return jsonify(respControle)


#Rota para pesquisa de chaves no form de inclusão de retirada de chave
@pesquisaBlue.route('/chave-pesquisa-mov/<pesquisa>')
def pesquisaChaveFormMov(pesquisa):
    controlePesquisa = ControlePesquisa()
    respControle = controlePesquisa.pesquisaChaveFormMov(pesquisa.upper().strip())
    return jsonify(respControle)


#Rota para pesquisa de funcionários no form de inclusão de retirada de chave
@pesquisaBlue.route('/funcionario-pesquisa-mov/<pesquisa>')
def pesquisaFuncFormMov(pesquisa):
    controlePesquisa = ControlePesquisa()
    respControle = controlePesquisa.pesquisaFuncFormMov(pesquisa.upper().strip())
    return jsonify(respControle)


#Rota para pesquisa de funcionários no form de inclusão de retirada de chave
@pesquisaBlue.route('/chaveRet-pesquisa-mov/<pesquisa>')
def pesquisaChaveRetFormMov(pesquisa):
    controlePesquisa = ControlePesquisa()
    respControle = controlePesquisa.pesquisaChaveRetFormMov(pesquisa.upper().strip())
    return jsonify(respControle)