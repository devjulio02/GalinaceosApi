from flask import Flask
from dotenv import load_dotenv
from helpers.cors import cors

app = Flask(__name__)
cors.init_app(app)

# Carrega as variáveis do .env
load_dotenv()