from helpers.application import app
from controllers.GalinaceoController import galinaceos_bp
from helpers.logger import logger

# Regista as rotas do controlador na aplicação
app.register_blueprint(galinaceos_bp)

if __name__ == '__main__':
    logger.info("Iniciando a GalinaceosApi...")
    app.run(host='0.0.0.0', port=5000, debug=True)