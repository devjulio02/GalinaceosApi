CREATE TABLE IF NOT EXISTS tb_galinaceos(
    id SERIAL PRIMARY KEY,
    sist_cria TEXT NOT NULL,
    niv_terr TEXT NOT NULL,
    cod_terr TEXT,
    nom_terr TEXT NOT NULL,
    cl_gal TEXT NOT NULL,
    gal_total INTEGER NOT NULL
);