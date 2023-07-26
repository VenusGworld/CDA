from flask import Blueprint, jsonify
import json
from datetime import datetime
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