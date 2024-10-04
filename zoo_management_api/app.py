import os
from flask import Flask, jsonify, request
from routes.animals_blueprint import animals_blueprint
import logging
from config import config
import json

app = Flask(__name__)

# Konfigurasi aplikasi
app.config.from_object(config[os.environ.get('FLASK_ENV') or 'default'])

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Register blueprints
logger.info("Registering blueprints...")
app.register_blueprint(animals_blueprint, url_prefix='/api')
logger.info("Blueprints registered successfully")

# Pastikan path ke db.json benar
DB_FILE = os.path.join(os.path.dirname(__file__), 'db.json')

@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Unhandled exception: {str(e)}", exc_info=True)
    return jsonify({"error": "Internal server error", "message": str(e)}), 500

@app.route('/')
def home():
    return jsonify({
        "message": "Selamat datang di API Manajemen Kebun Binatang!",
        "endpoints": {
            "animals": "/api/animals"
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

@app.route('/api/debug/db')
def debug_db():
    try:
        with open(DB_FILE, 'r') as f:
            data = json.load(f)
        return jsonify({"db_content": data, "db_path": DB_FILE})
    except Exception as e:
        return jsonify({"error": str(e), "db_path": DB_FILE})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
