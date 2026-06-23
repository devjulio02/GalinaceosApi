from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
import psycopg2

from models.Galinaceo import GalinaceoSchema
from services.GalinaceoService import GalinaceoService
from helpers.logger import logger

# Regista o endpoint principal
galinaceos_bp = Blueprint('galinaceos', __name__, url_prefix='/galinaceos')
service = GalinaceoService()

@galinaceos_bp.get("/")
def getAll():
    logger.info("Controller: Listando todos os registos")
    try:
        registos = service.getAll()
        return jsonify([r.toDict() for r in registos]), 200
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno na base de dados"}, 500

@galinaceos_bp.get("/<int:id>")
def getById(id: int):
    try:
        registo = service.getById(id)
        if registo is None:
            return {"mensagem": "O registo não foi encontrado"}, 404
        return jsonify(registo.toDict()), 200
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno na base de dados"}, 500

@galinaceos_bp.post("/")
def create():
    try:
        data = GalinaceoSchema().load(request.get_json())
        registo = service.create(data)
        return jsonify(registo.toDict()), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno na base de dados"}, 500

@galinaceos_bp.put("/<int:id>")
def update(id: int):
    try:
        data = GalinaceoSchema().load(request.get_json())
        registo = service.update(id, data)
        if registo is None:
            return {"mensagem": "O registo não foi encontrado"}, 404
        return jsonify(registo.toDict()), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno na base de dados"}, 500

@galinaceos_bp.delete("/<int:id>")
def delete(id: int):
    try:
        removido = service.delete(id)
        if not removido:
            return {"mensagem": "O registo não foi encontrado"}, 404
        return {"mensagem": "Registo removido com sucesso!"}, 200
    except psycopg2.Error as e:
        logger.error(e)
        return {"erro": "Erro interno na base de dados"}, 500
    