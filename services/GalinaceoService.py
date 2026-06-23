from helpers.logger import logger
from repositories.GalinaceoRepository import GalinaceoRepository
from models.Galinaceo import Galinaceo

def rowToGalinaceo(row):
    # Mapeia as 7 colunas devolvidas pelo PostgreSQL
    return Galinaceo(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

class GalinaceoService:
    def __init__(self):
        self.repository = GalinaceoRepository()

    def getAll(self):
        rows = self.repository.getAll()
        logger.info(f"Retornando {len(rows)} registos de galináceos")
        return [rowToGalinaceo(r) for r in rows]

    def getById(self, id):
        row = self.repository.getById(id)
        return rowToGalinaceo(row) if row is not None else None

    def create(self, data):
        # O cod_terr usa .get() porque definimos que pode ser nulo (allow_none=True)
        id = self.repository.insert(
            data["sist_cria"], data["niv_terr"], data.get("cod_terr"),
            data["nom_terr"], data["cl_gal"], data["gal_total"]
        )
        logger.info(f"Registo criado com id: {id}")
        return Galinaceo(id, data["sist_cria"], data["niv_terr"], data.get("cod_terr"), data["nom_terr"], data["cl_gal"], data["gal_total"])

    def update(self, id, data):
        affected = self.repository.update(
            id, data["sist_cria"], data["niv_terr"], data.get("cod_terr"),
            data["nom_terr"], data["cl_gal"], data["gal_total"]
        )
        if affected == 0:
            return None
        logger.info(f"Registo {id} atualizado")
        return Galinaceo(id, data["sist_cria"], data["niv_terr"], data.get("cod_terr"), data["nom_terr"], data["cl_gal"], data["gal_total"])

    def delete(self, id):
        affected = self.repository.delete(id)
        logger.info(f"Registo {id} removido: {affected > 0}")
        return affected > 0