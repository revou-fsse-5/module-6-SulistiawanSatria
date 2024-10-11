import pytest
from app import create_app
from supabase import create_client
import os

# Fixture untuk aplikasi Flask
@pytest.fixture
def app():
    app = create_app()  # Menggunakan fungsi untuk membuat instance aplikasi Flask
    app.config.update({
        "TESTING": True,
    })
    yield app

# Fixture untuk client pengujian
@pytest.fixture
def client(app):
    return app.test_client()

# Fixture untuk pengaturan Supabase client
@pytest.fixture
def supabase_client():
    url = os.getenv("SUPABASE_URL")  # Ambil URL Supabase dari environment variable
    key = os.getenv("SUPABASE_KEY")  # Ambil API key Supabase dari environment variable
    supabase = create_client(url, key)  # Membuat instance Supabase client
    return supabase
