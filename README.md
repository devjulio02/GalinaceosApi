# GalinaceosApi - Atividade 2

Interface de Programação de Aplicações (API) desenvolvida com o microframework Flask para extração, persistência e filtragem de dados demográficos sobre a avicultura nacional.

## Funcionalidades do Projeto

- **Processo de ETL:** Script automatizado (`extracao_csv.py`) que consome dados brutos diretamente do arquivo `GALINACEOS.csv` do IBGE, realizando a limpeza de caracteres nulos, tratamento de strings e formatação numérica usando Pandas e NumPy.
- **Persistência Relacional:** Armazenamento robusto estruturado em banco de dados PostgreSQL executado em container isolado via Docker.
- **Camada de Dados Dinâmica:** Repositório construído para realizar consultas parametrizadas com concatenação SQL limpa e segura.
- **Filtros Dinâmicos por Query Parameters:** Endpoint principal `/galinaceos` preparado para processar requisições HTTP aplicando filtros simultâneos ou isolados na URL pelos campos: `SIST_CRIA`, `NIV_TERR`, `COD_TERR`, `NOM_TERR` e `CL_GAL`.