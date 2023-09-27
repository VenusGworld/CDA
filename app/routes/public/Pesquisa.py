from ...controllers.ControlePesquisa import ControlePesquisa
from flask import Blueprint, jsonify


pesquisaBlue = Blueprint("pesquisaBlue", __name__)

##############################################################
# Rotas relacionadas as pesquisas do sistema
##############################################################

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


#Rota para pesquisa de chaves no form de inclusão de retirada de chave
@pesquisaBlue.route('/chaveRet-pesquisa-mov/<pesquisa>')
def pesquisaChaveRetFormMov(pesquisa):
    controlePesquisa = ControlePesquisa()
    respControle = controlePesquisa.pesquisaChaveRetFormMov(pesquisa.upper().strip())
    return jsonify(respControle)


#Rota para pesquisa de terceiros no input de cpf na inclusão de saída de terceiro
@pesquisaBlue.route('/terceiro-pesquisa/<pesquisa>')
def pesquisaTerceiro(pesquisa):
    controlePesquisa = ControlePesquisa()
    respControle = controlePesquisa.pesquisaTerceiros(pesquisa.upper().strip())
    return jsonify(respControle)


#Rota para pesquisa de terceiros no form de inclusão de saída de terceiro
@pesquisaBlue.route('/terceiro-pesquisa-mov/<pesquisa>')
def pesquisaTerceiroFormMov(pesquisa):
    controlePesquisa = ControlePesquisa()
    respControle = controlePesquisa.pesquisaTerceiroFormmov(pesquisa.upper().strip())
    return jsonify(respControle)


#Rota para pesquisa de gerente no input
@pesquisaBlue.route('/gerente-pesquisa/<pesquisa>')
def pesquisaGerenteInput(pesquisa):
    controlePesquisa = ControlePesquisa()
    respControle = controlePesquisa.pesquisaGerente(pesquisa.upper().strip())
    return jsonify(respControle)


#Rota para verificar se o gerente que foi informado na entrda não está em um movimento aberto
@pesquisaBlue.route('/gerenteSai-pesquisa-mov/<pesquisa>')
def pesquisaGerSaiFormMov(pesquisa):
    controlePesquisa = ControlePesquisa()
    respControle = controlePesquisa.pesquisaGerenteSaiFormMov(pesquisa.strip())
    return jsonify(respControle)


#Rota para pesquisa de chaves no input para o relatório
@pesquisaBlue.route('/chave-pesquisa-relatorio/<pesquisa>')
def pesquisaChaveInputRelat(pesquisa):
    controlePesquisa = ControlePesquisa()
    respControle = controlePesquisa.pesquisaChaveRelat(pesquisa.upper().strip())
    return jsonify(respControle)


#Rota para pesquisa de gerente no input
@pesquisaBlue.route('/gerente-pesquisa-relatorio/<pesquisa>')
def pesquisaGerenteInputRelat(pesquisa):
    controlePesquisa = ControlePesquisa()
    respControle = controlePesquisa.pesquisaGerenteRelat(pesquisa.upper().strip())
    return jsonify(respControle)