from flask import Flask, render_template, make_response
import json

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secret key'

result = {
    'name': 'yitian',
    'age': 25,
    'nickname': 'leo',
    'birthday': '1993-12-12'
}


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/nocors')
def nocors():
    return json.dumps(result)


@app.route('/cors')
def cors():
    resp = make_response(json.dumps(result))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    app.run()
