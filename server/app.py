import flask

app = flask.Flask(__name__)

@app.route("/hello")
def hello():
    return flask.render_template('hello.html')
