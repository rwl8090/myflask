from flask import Flask
from flask import request
from flask import render_template
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap


app = Flask(__name__)
moment = Moment(app)  #初始化Moment
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = '5583jfisnjjgsinegensdfjienge'


#表单类
class NameForm(FlaskForm):
    name = StringField("能告诉我你的名字吗？", validators=[DataRequired(message='名字忘填了。。。')])
    submit = SubmitField('告知一下！')


@app.route('/')
def hello_world():
    user_agent = request.headers.get('User-Agent')
    return '浏览器版本为：{}'.format(user_agent)


@app.route('/index/')
def index():

    return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user/')
def user():

    return render_template('user.html', name='David')


@app.route('/name/<name>/')
def get_name(name):
    return 'Hello {} ! 欢迎来到Flask！'.format(name)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('login.html', form=form, name=name)


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
    app.run(debug=True, host='127.0.0.1', port=5000)  # debug模式启动，重载器与调试器


