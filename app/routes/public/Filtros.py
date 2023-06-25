from flask import Blueprint, jsonify
import json
from datetime import datetime

filtrosBlue = Blueprint("filtros", __name__)

#Filtro para Data input
@filtrosBlue.app_template_filter('dataInput')
def _jinja2_filter_dataInput(date, fmt=None):
    native = date.replace(tzinfo=None)
    format='%Y-%m-%d'
    return native.strftime(format) 


#Filtro para Data input
@filtrosBlue.app_template_filter('horaInput')
def _jinja2_filter_horaInput(date, fmt=None):
    native = date.replace(tzinfo=None)
    format='%H:%M'
    return native.strftime(format) 