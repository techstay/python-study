from werkzeug.utils import secure_filename
from flask import *

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '加密Session所需的密钥'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/greet/<name>')
def greet(name=None):
    return render_template('greet.html', name=name)


@app.route('/greet')
def greet2():
    name = request.args['name']
    return render_template('greet.html', name=name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


@app.route('/form', methods=['get'])
def get_form():
    return render_template('form.html')


@app.route('/form', methods=['post'])
def submit_form():
    form = request.form
    file = request.files['file']
    if file:
        app.logger.debug(f'filename:{file.filename}')
        app.logger.debug(f'secure_filename:{secure_filename(file.filename)}')
        file.save(f'uploaded_files/{file.filename}')

    return render_template('form-result.html', data=form)


@app.route('/redirect_to_index')
def redirect_to_index():
    return redirect(url_for('index'))


@app.route('/get_request_data')
def get_request_data():
    data = request.values
    return render_template('form-result.html', data=data)


@app.route('/add_cookie')
def add_cookie():
    return render_template('add-cookie.html')


@app.route('/show_cookies', methods=['post', 'get'])
def show_cookies():
    name = request.values.get('cookie_name')
    value = request.values.get('cookie_value')
    if name is None:
        name = ''
    if value is None:
        value = ''

    cookies = request.cookies
    template = render_template('show-cookies.html', cookies=cookies)
    resp = make_response(template)
    resp.set_cookie(name, value)
    return resp


@app.route('/files')
def get_uploaded_file():
    filename = request.args['filename']
    return send_file(filename)


def before_request():
    import glob
    files = glob.glob('uploaded_files/*')
    flist = []
    for f in files:
        flist.append(f)
    session['files'] = flist


if __name__ == '__main__':
    app.before_request(before_request)
    app.run(host='0.0.0.0')
