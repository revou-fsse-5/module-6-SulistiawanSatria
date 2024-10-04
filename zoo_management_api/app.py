import sys
sys.path.append('/app')

from flask import Flask, jsonify, request
from auth import register_blueprint, login_blueprint
from routes import animals_blueprint, employees_blueprint
from db import users

import logging
from config import config
import os

app = Flask(__name__)

# Konfigurasi aplikasi
app.config.from_object(config[os.environ.get('FLASK_ENV') or 'default'])

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Register blueprints
app.register_blueprint(register_blueprint, url_prefix='/api')
app.register_blueprint(login_blueprint, url_prefix='/api')
app.register_blueprint(animals_blueprint, url_prefix='/api')
app.register_blueprint(employees_blueprint, url_prefix='/api')

@app.route('/')
def home():
    return jsonify({
        "message": "Selamat datang di API Manajemen Kebun Binatang!",
        "endpoints": {
            "animals": "/api/animals",
            "employees": "/api/employees",
            "register": "/api/register",
            "login": "/api/login"
        }
    })

@app.before_request
def log_request_info():
    logger.info('Headers: %s', request.headers)
    logger.info('Body: %s', request.get_data())

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found", "message": "The requested resource was not found on this server"}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error('Server Error: %s', str(error))
    return jsonify({"error": "Internal server error", "message": "An unexpected error occurred"}), 500

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
