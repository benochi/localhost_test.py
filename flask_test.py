from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "You should see this message if your VENV is working."
if __name__ == '__main__':
    app.run(debug=True)
