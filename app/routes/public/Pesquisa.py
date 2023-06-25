from flask import Blueprint, jsonify
from ...controllers.ControlePesquisa import ControlePesquisa

pesquisaBlue = Blueprint("pesquisaBlue", __name__)

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