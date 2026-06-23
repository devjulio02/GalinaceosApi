from helpers.database import get_conn
from helpers.logger import logger

class GalinaceoRepository():
    def getAll(self):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tb_galinaceos")
        return cursor.fetchall()

    def getById(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tb_galinaceos WHERE id=%s", (id,))
        return cursor.fetchone()

    def insert(self, sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, gal_total):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO tb_galinaceos(sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, gal_total) 
               VALUES(%s, %s, %s, %s, %s, %s) RETURNING id""",
            (sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, gal_total)
        )
        conn.commit()
        return cursor.fetchone()[0]

    def update(self, id, sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, gal_total):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE tb_galinaceos 
               SET sist_cria=%s, niv_terr=%s, cod_terr=%s, nom_terr=%s, cl_gal=%s, gal_total=%s 
               WHERE id=%s""",
            (sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, gal_total, id)
        )
        conn.commit()
        return cursor.rowcount

    def delete(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tb_galinaceos WHERE id=%s", (id,))
        conn.commit()
        return cursor.rowcount