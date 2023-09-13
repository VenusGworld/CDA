from flask import Blueprint
import dateutil.parser

filtrosBlue = Blueprint("filtros", __name__)


#Filtro para Data input
@filtrosBlue.app_template_filter('dataInput')
def _jinja2_filter_dataInput(date, fmt=None):
    if type(date) == str:
        date = dateutil.parser.parse(date)

    native = date.replace(tzinfo=None)
    format='%Y-%m-%d'
    return native.strftime(format) 


#Filtro para Data input
@filtrosBlue.app_template_filter('dataLimite')
def _jinja2_filter_dataLimite(date, fmt=None):
    if type(date) == str:
        date = dateutil.parser.parse(date)

    native = date.replace(tzinfo=None)
    format='%d/%m/%Y'
    return native.strftime(format) 


#Filtro para Data input
@filtrosBlue.app_template_filter('horaInput')
def _jinja2_filter_horaInput(date, fmt=None):
    native = date.replace(tzinfo=None)
    format='%H:%M'
    return native.strftime(format) 


#Filtro para CPF/CNPJ
@filtrosBlue.app_template_filter('cpf')
def _jinja2_filter_cpf(cpf, fmt=None):
    if len(cpf) < 11:
        cpf = "--"
    elif len(cpf) == 11:
        cpf = cpf[0:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]

    return cpf


#Filtro para Data input
@filtrosBlue.app_template_filter('dataTime')
def _jinja2_filter_dataTime(date, fmt=None):
    if type(date) == str:
        date = dateutil.parser.parse(date)

    native = date.replace(tzinfo=None)
    format='%d/%m/%Y %H:%M:%S'
    return native.strftime(format) 


#Filtro para Data input
@filtrosBlue.app_template_filter('filtroBoleano')
def _jinja2_filter_boleano(tipo, fmt=None):
    if tipo == True:
        return "SIM"
    else:
        return "NÃO"