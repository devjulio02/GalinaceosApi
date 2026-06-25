DROP TABLE IF EXISTS tb_galinaceos;

CREATE TABLE IF NOT EXISTS tb_galinaceos (
    id SERIAL PRIMARY KEY,
    sist_cria VARCHAR(100),
    niv_terr VARCHAR(50),
    cod_terr VARCHAR(50),
    nom_terr VARCHAR(150),
    cl_gal VARCHAR(50),
    nom_cl_gal VARCHAR(150),
    gal_total BIGINT
);