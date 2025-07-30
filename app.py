import os
import traceback
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    try:
        app.logger.info("Received request for /")
        return render_template("index.html")
    except Exception as e:
        app.logger.error("Error rendering /: %s", e)
        traceback.print_exc()
        return f"<h1>Internal Server Error</h1><pre>{traceback.format_exc()}</pre>", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.logger.info(f"Starting Flask debug server on port {port}")
    app.run(host="0.0.0.0", port=port, debug=True)
