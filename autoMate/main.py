import logging
from flask import Flask, render_template
from findr import findr_bp

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_app():
    logger.info("🔧 Creating Flask app...")
    app = Flask(__name__)

    logger.info("🔗 Registering Findr blueprint...")
    app.register_blueprint(findr_bp, url_prefix="/findr")
    logger.info("✅ Findr blueprint registered.")

    @app.route("/")
    def home():
        logger.info("📄 Rendering home.html")
        return render_template("home.html")

    return app

if __name__ == "__main__":
    logger.info("🚀 Running app via __main__")
    app = create_app()
    app.run(debug=True)
