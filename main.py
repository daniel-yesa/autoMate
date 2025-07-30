import os
import logging
from flask import Flask, render_template
from findr import findr_bp

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_app():
    logger.info("🔧 Creating Flask app...")
    app = Flask(__name__)

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
    
    logger.info("🔗 Registering Findr blueprint...")
    app.register_blueprint(findr_bp, url_prefix="/findr")
    logger.info("✅ Findr blueprint registered.")

    @app.route("/")
    def home():
        try:
            logger.info("📄 Rendering home.html")
            return render_template("home.html")
        except Exception as e:
            logger.error(f"❌ Error rendering home.html: {e}")
            return f"Internal error: {e}", 500

    return app


if __name__ == "__main__":
    logger.info("🚀 Running app via __main__")
    app = create_app()
    app.run(debug=True)
