from flask import Flask, render_template
from findr import findr_bp  # Now this will work

app = Flask(__name__)

# Register blueprint
app.register_blueprint(findr_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)