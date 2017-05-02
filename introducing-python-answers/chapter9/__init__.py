# Q2
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    thing = request.values.get('thing')
    height = request.values.get('height')
    color = request.values.get('color')
    return render_template('home.html', thing=thing, height=height, color=color)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
