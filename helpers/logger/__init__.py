import logging

logger = logging.getLogger('GalinaceosApi')
logger.setLevel(logging.INFO)

formatacao = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatacao)

file_handler = logging.FileHandler('api.log', encoding='utf-8')
file_handler.setFormatter(formatacao)

logger.addHandler(console_handler)
logger.addHandler(file_handler)