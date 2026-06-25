import pandas as pd
import numpy as np
from helpers.application import app
from helpers.database import get_conn

def extrair_e_carregar():
    print("1. Lendo e tratando o arquivo GALINACEOS.csv com Pandas...")
    
    df = pd.read_csv('GALINACEOS.csv', sep=';', dtype=str, keep_default_na=False)

    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.replace('X', np.nan)

    if 'GAL_TOTAL' in df.columns:
        df['GAL_TOTAL'] = df['GAL_TOTAL'].str.replace('.', '', regex=False)

    with app.app_context():
        conn = get_conn()
        cursor = conn.cursor()
        
        print("2. Limpando a tabela para evitar duplicatas...")
        cursor.execute("TRUNCATE TABLE tb_galinaceos RESTART IDENTITY;")
        
        print("3. Inserindo os dados no PostgreSQL. Isso pode levar alguns segundos...")
        query_insert = """
            INSERT INTO tb_galinaceos (sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, nom_cl_gal, gal_total)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        
        inseridos = 0
        # Percorre o CSV linha por linha
        for index, row in df.iterrows():
            
            gal_total_val = None
            if pd.notna(row['GAL_TOTAL']):
                try:
                    gal_total_val = int(row['GAL_TOTAL'])
                except ValueError:
                    gal_total_val = None

            valores = (
                str(row['SIST_CRIA']) if pd.notna(row['SIST_CRIA']) else None,
                str(row['NIV_TERR']) if pd.notna(row['NIV_TERR']) else None,
                str(row['COD_TERR']) if pd.notna(row['COD_TERR']) else None,
                str(row['NOM_TERR']) if pd.notna(row['NOM_TERR']) else None,
                str(row['CL_GAL']) if pd.notna(row['CL_GAL']) else None,
                str(row['NOM_CL_GAL']) if pd.notna(row['NOM_CL_GAL']) else None,
                gal_total_val
            )
            
            cursor.execute(query_insert, valores)
            inseridos += 1
            
        conn.commit()
        cursor.close()
        print(f"Sucesso total! {inseridos} registros foram extraídos e salvos no banco.")

if __name__ == "__main__":
    extrair_e_carregar()