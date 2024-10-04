import json
import os

DB_FILE = 'db.json'

def load_db():
    if not os.path.exists(DB_FILE):
        return {"animals": [], "employees": []}
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_db(db):
    with open(DB_FILE, 'w') as f:
        json.dump(db, f, indent=2)

def get_next_id(items):
    return max([item['id'] for item in items] + [0]) + 1
