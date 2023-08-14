from flask import Blueprint, render_template, jsonify
import os

indexBlue = Blueprint("indexBlue", __name__)

##############################################################
# Rotas relacionadas ao Index do sistema
##############################################################

#Rota o index do sistema
@indexBlue.route("/")
@indexBlue.route("/index")
def index():
    return render_template("public/index.html")


