from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.User import User
# Models
from models.UserModel import UserModel

main = Blueprint('user_blueprint', __name__)


@main.route('/')
def get_users():
    try:
        users = UserModel.get_users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_user(id):
    try:
        user = UserModel.get_user(id)
        if user != None:
            return jsonify(user)
        else:
            return jsonify({'message': "Este usuario no existe"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_user():
    try:
        id = request.json['id']
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        rut = request.json['rut']
        cargo = request.json['cargo']
        descripcion = request.json['descripcion']
        pais = request.json['pais']
        ciudad = request.json['ciudad']
        postal = int(request.json['postal'])
        celular = request.json['celular']
        correo = request.json['correo']

        user = User(str(id), nombre, apellido, rut, cargo,
                    descripcion, pais, ciudad, postal, celular, correo)

        affected_rows = UserModel.add_user(user)
        if user != None:
            return jsonify(user.id)
        else:
            return jsonify({'message': "Error al insertar datos"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_user(id):
    try:
        id = request.json['id']
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        rut = request.json['rut']
        cargo = request.json['cargo']
        descripcion = request.json['descripcion']
        pais = request.json['pais']
        ciudad = request.json['ciudad']
        postal = int(request.json['postal'])
        celular = request.json['celular']
        correo = request.json['correo']
        user = User(id, nombre, apellido, rut, cargo, descripcion,
                    pais, ciudad, postal, celular, correo)

        affected_rows = UserModel.update_user(user)

        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({'message': "Ninguna pelicula actualizada"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User(id)

        affected_rows = UserModel.delete_user(user)

        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({'message': "Ningún usuario borrado"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
