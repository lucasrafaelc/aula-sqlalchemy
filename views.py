from flask import Blueprint, request, make_response, jsonify, abort
from models import Perfil
from app import db

rotas_usuario = Blueprint("minhas_rotas", __name__)

@rotas_usuario.route("/perfis", methods=['GET', 'POST'])
def usuarios():
    if request.method == "GET":
        query = db.select(Perfil)
        perfis = db.session.execute(query).all()
        resultado = []
        for perfil in perfis:
            perfil = {"id": perfil[0].id, "nome": perfil[0].nome}
            resultado.append(perfil)
        return make_response(jsonify(resultado))

    elif request.method == "POST":
        pass
        dados = request.get_json()
        perfil_novo = Perfil(nome=dados['nome'])
        db.session.add(perfil_novo)
        db.session.commit()
        return make_response(jsonify("Perfil inserido com sucesso"), 200)

    else:
        abort(404)

@rotas_usuario.route('/perfil/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def tarefa(id):
    # Obtém o perfil no banco
    query = db.select(Perfil).where(Perfil.id == id)
    perfil = db.session.execute(query).scalar()
    if perfil is None:
        return make_response(jsonify("Perfil não encontrado!"), 400)
    else:
        if request.method == "GET":
            return make_response(jsonify({"id": perfil.id, "nome": perfil.nome}))

        elif request.method == "PUT":
            dados = request.get_json()
            novo_nome = dados['nome']

            perfil.nome = novo_nome
            db.session.add(perfil)
            db.session.commit()
            return make_response(jsonify("Perfil Editado com sucesso"), 200)

        elif request.method == "DELETE":
            db.session.delete(perfil)
            db.session.commit()
            return make_response(jsonify("Perfil Apagado com sucesso"), 200)
        else:
            abort(400)