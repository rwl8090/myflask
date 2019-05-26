from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    user_agent = request.headers.get('User-Agent')
    return '浏览器版本为：{}'.format(user_agent)

@app.route('/index/')
def index():

    return render_template('index.html')

@app.route('/name/<name>/')
def get_name(name):
    return 'Hello {} ! 欢迎来到Flask！'.format(name)

@app.route('/login/<uname>', methods=['GET', 'POST'])
def login(uname):
    if request.method=='GET':
        return uname
    elif request.method=='POST':
        pass

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post {}'.format(post_id)

@app.route('/template/')
@app.route('/template/<tmp_name>/')
def show_tem_name(tmp_name=None):
    ls = ['java', 'python', 'C', 'C#', 'javascript']
    return render_template('tmp_file.html', name=tmp_name, comments=ls)


# @app.errorhandler(404)
# def not_found(error):
#     resp = Flask.make_response(render_template('error.html'), 404)
#     resp.headers['X-Parachutes'] = 'parachutes are cool'
#     return resp #render_template('error.html'), 404

if __name__ == '__main__':
    app.run(debug=True)  # debug模式启动，重载器与调试器


