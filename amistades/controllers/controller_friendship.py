
from flask import redirect, render_template, request
from amistades.models.model_friendship import Amistad
from amistades import app
from amistades.models.model_user import Usuario

@app.route('/friendship')
def getFriendship():
    amistades = Amistad.listFriendships()
    usuarios = Usuario.getUsuarios()
    return render_template('index.html',amistades=amistades,usuarios=usuarios)

@app.route('/addFriendship',methods=["POST"])
def addFriendship():
    amistad = {
        "usuario_id" : request.form["usuario_id"],
        "amigo_id" : request.form["amistad_id"]
    }
    resultado = Amistad.validateFriendships(amistad)
    if(len(resultado) == 0):
        resultado = Amistad.addFriendships(amistad)
    
    return redirect('/friendship')
