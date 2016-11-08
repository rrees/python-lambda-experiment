import flask

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return "Hello from the Flask app\n"

if __name__ == "__main__":
    app.run()
