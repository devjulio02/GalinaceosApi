from helpers.database import get_conn

class GalinaceoRepository:
    def getAll(self, filtros=None):
        conn = get_conn()
        cursor = conn.cursor()
        
        query = "SELECT id, sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, nom_cl_gal, gal_total FROM tb_galinaceos"
        
        condicoes = []
        valores = []
        
        if filtros:
            campos_filtráveis = ['sist_cria', 'niv_terr', 'cod_terr', 'nom_terr', 'cl_gal']
            
            for campo in campos_filtráveis:
                valor = filtros.get(campo)
                if valor: 
                    condicoes.append(f"{campo} = %s")
                    valores.append(valor)
        
        if condicoes:
            query += " WHERE " + " AND ".join(condicoes)
            
        cursor.execute(query, tuple(valores))
        return cursor.fetchall()

    def getById(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, nom_cl_gal, gal_total FROM tb_galinaceos WHERE id=%s", 
            (id,)
        )
        return cursor.fetchone()