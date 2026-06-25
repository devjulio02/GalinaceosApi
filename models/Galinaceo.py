from marshmallow import Schema, fields

class Galinaceo:
    def __init__(self, id, sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, nom_cl_gal, gal_total):
        self.id = id
        self.sist_cria = sist_cria
        self.niv_terr = niv_terr
        self.cod_terr = cod_terr
        self.nom_terr = nom_terr
        self.cl_gal = cl_gal
        self.nom_cl_gal = nom_cl_gal
        self.gal_total = gal_total

    def toDict(self):
        return {
            "id": self.id,
            "sist_cria": self.sist_cria,
            "niv_terr": self.niv_terr,
            "cod_terr": self.cod_terr,
            "nom_terr": self.nom_terr,
            "cl_gal": self.cl_gal,
            "nom_cl_gal": self.nom_cl_gal,
            "gal_total": self.gal_total
        }

class GalinaceoSchema(Schema):
    id = fields.Int(dump_only=True)
    sist_cria = fields.Str(required=True)
    niv_terr = fields.Str(required=True)
    cod_terr = fields.Str(allow_none=True)
    nom_terr = fields.Str(required=True)
    cl_gal = fields.Str(required=True)
    nom_cl_gal = fields.Str(required=True)
    gal_total = fields.Int(allow_none=True)