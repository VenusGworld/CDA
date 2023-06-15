from flask import Blueprint, jsonify
import json

filtros = Blueprint("filtros", __name__)

@filtros.app_template_filter("json")
def jinja2FiltroJson(dict, fmt=None):
    jsonResp = json.dumps(dict, indent=4, ensure_ascii=False)
    return jsonResp