from helpers.logger import logger
from repositories.GalinaceoRepository import GalinaceoRepository
from models.Galinaceo import Galinaceo

def rowToGalinaceo(row):
    return Galinaceo(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])

class GalinaceoService:
    def __init__(self):
        self.repository = GalinaceoRepository()

    def getAll(self, filtros=None):
        rows = self.repository.getAll(filtros)
        logger.info(f"Serviço: Retornando {len(rows)} registos de galináceos com filtros: {filtros}")
        return [rowToGalinaceo(r) for r in rows]

    def getById(self, id):
        row = self.repository.getById(id)
        return rowToGalinaceo(row) if row is not None else None