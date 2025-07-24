from flask import Flask, render_template
from findr import findr_bp

def create_app():
    print("🔧 Creating Flask app...")  # Debug
    app = Flask(__name__)

    try:
        print("🔗 Registering Findr blueprint...")  # Debug
        app.register_blueprint(findr_bp, url_prefix='/findr')
        print("✅ Findr blueprint registered.")
    except Exception as e:
        print("❌ Error registering blueprint:", e)

    @app.route("/")
    def home():
        print("📍 Hit Home Route")  # Debug
        return render_template("home.html")

    return app

if __name__ == "__main__":
    app = create_app()
    print("🚀 Running app in debug mode...")
    app.run(debug=True)
