import os
from dotenv import dotenv_values

# Junta as variáveis do arquivo .env com as do sistema operacional
enviroment = {
    **dotenv_values(".env"),
    **os.environ
}