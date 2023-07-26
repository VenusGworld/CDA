from flask import Blueprint, render_template, jsonify
import os

indexBlue = Blueprint("indexBlue", __name__)

#Rota o index do sistema
@indexBlue.route("/")
@indexBlue.route("/index")
def indeX():
    return render_template("public/index.html")


