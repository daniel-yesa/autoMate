from flask import Flask, render_template
from findr import findr_bp

app = Flask(__name__)

# Register the Findr blueprint
app.register_blueprint(findr_bp, url_prefix="/findr")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
