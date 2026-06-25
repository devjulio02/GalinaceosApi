from flask import Blueprint, request, jsonify
import psycopg2

from services.GalinaceoService import GalinaceoService
from helpers.logger import logger

galinaceos_bp = Blueprint('galinaceos', __name__, url_prefix='/galinaceos')
service = GalinaceoService()

@galinaceos_bp.get("/")
def getAll():
    logger.info("Controller: Listando registos com filtros dinâmicos")
    try:
        filtros = {
            'sist_cria': request.args.get('SIST_CRIA') or request.args.get('sist_cria'),
            'niv_terr': request.args.get('NIV_TERR') or request.args.get('niv_terr'),
            'cod_terr': request.args.get('COD_TERR') or request.args.get('cod_terr'),
            'nom_terr': request.args.get('NOM_TERR') or request.args.get('nom_terr'),
            'cl_gal': request.args.get('CL_GAL') or request.args.get('cl_gal')
        }
        
        filtros_limpos = {k: v for k, v in filtros.items() if v is not None}
        
        registos = service.getAll(filtros_limpos)
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