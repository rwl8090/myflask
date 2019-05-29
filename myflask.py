from flask import Flask, session, redirect, url_for, flash
from flask import request
from flask import render_template
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
moment = Moment(app)  #初始化Moment
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = '5583jfisnjjgsinegensdfjienge'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://python:python@127.0.0.1:3306/python'  # 初始化连接
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 以便在不需要跟踪对象变化时降低内存消耗
db = SQLAlchemy(app)


# 数据库类
class Role(db.Model):
    __tablename__ = 'role'  # 指定表名
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), unique=True)
    user = db.relationship('User', backref='role')
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.role_id'))

    def __repr__(self):
        return '<User %r>' % self.user_name



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
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash("Looks like you have changed your name!")
        session['name'] = form.name.data
        return redirect(url_for('login'))
        #form.name.data = ''
    return render_template('login.html', form=form, name=session.get('name'))


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


