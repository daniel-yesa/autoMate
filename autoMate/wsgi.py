print("🔄 Starting via WSGI...")

from main import create_app

app = create_app()

print("✅ WSGI app created.")
