import pandas as pd
import psycopg2
from helpers.enviroment import enviroment
from helpers.logger import logger

# Nome do arquivo CSV que está na raiz do seu projeto
CSV_PATH = 'GALINACEOS.csv'

try:
    logger.info("Lendo o arquivo CSV com Pandas... Aguarde.")
    
    # Lendo o CSV. O low_memory=False ajuda com arquivos pesados do IBGE
    df = pd.read_csv(CSV_PATH, sep=',', low_memory=False)

    # Selecionando estritamente as colunas exigidas na atividade
    df_filtrado = df[['SIST_CRIA', 'NIV_TERR', 'COD_TERR', 'NOM_TERR', 'CL_GAL', 'GAL_TOTAL']]

    # O Pandas transforma células vazias em 'NaN' (Not a Number). 
    # O Postgres não entende NaN, então precisamos converter para None (nulo) do Python.
    df_filtrado = df_filtrado.where(pd.notnull(df_filtrado), None)

    logger.info("Conectando ao banco de dados...")
    conn = psycopg2.connect(
        database=enviroment.get("DB_NAME"),
        user=enviroment.get("DB_USER"),
        password=enviroment.get("DB_PASSWORD"),
        host=enviroment.get("DB_HOST"),
        port=enviroment.get("DB_PORT")
    )
    cursor = conn.cursor()

    logger.info("Inserindo os dados na tabela tb_galinaceos. Isso pode demorar alguns segundos...")
    
    inseridos = 0
    # iterrows() passa linha por linha do DataFrame
    for index, row in df_filtrado.iterrows():
        cursor.execute(
            """INSERT INTO tb_galinaceos(sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, gal_total) 
               VALUES(%s, %s, %s, %s, %s, %s)""",
            (row['SIST_CRIA'], row['NIV_TERR'], row['COD_TERR'], row['NOM_TERR'], row['CL_GAL'], row['GAL_TOTAL'])
        )
        inseridos += 1

    # Confirma a transação inteira no banco
    conn.commit()
    logger.info(f"Sucesso! {inseridos} registros foram inseridos no banco de dados.")

except Exception as e:
    logger.error(f"Erro ao processar o arquivo CSV: {e}")
finally:
    if 'conn' in locals() and conn:
        conn.close()
        logger.info("Conexão fechada.")