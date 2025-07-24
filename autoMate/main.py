from flask import Flask, render_template
from findr import findr_bp

def create_app():
    app = Flask(__name__)
    
    # Register blueprint for Findr
    app.register_blueprint(findr_bp, url_prefix='/findr')

    # Define the homepage route
    @app.route("/")
    def home():
        return render_template("home.html")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
