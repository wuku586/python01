# save this as app.py
import flask
app = flask.Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello():
    return "Hello, World 123456 !"

if __name__ == '__main__':
    app.run()