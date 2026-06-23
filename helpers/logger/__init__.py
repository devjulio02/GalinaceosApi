import logging

# Cria o logger principal da aplicação
logger = logging.getLogger('GalinaceosApi')
logger.setLevel(logging.INFO)

# Define o formato visual das mensagens
formatacao = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# 1. Configurador para imprimir no Terminal
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatacao)

# 2. Configurador para salvar no arquivo (api.log)
file_handler = logging.FileHandler('api.log', encoding='utf-8')
file_handler.setFormatter(formatacao)

# Adiciona os dois comportamentos ao nosso logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)