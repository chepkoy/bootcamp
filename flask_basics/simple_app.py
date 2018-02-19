from flask import Flask;

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from Allans house"

app.run(debug=True, port=5000)
