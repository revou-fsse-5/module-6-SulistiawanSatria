from flask import Flask, jsonify
import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load .env file
load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# Membuat koneksi ke Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)

@app.route("/data")
def get_data():
    data = supabase.table('your_table_name').select('*').execute()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
