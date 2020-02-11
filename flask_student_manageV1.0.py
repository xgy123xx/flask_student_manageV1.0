from flask import Flask,session,render_template,request,redirect
from student_add import stu_add
from student_del import stu_del
from student_edit import stu_edit
from models import mysqlHandle
import time
app = Flask(__name__)
app.secret_key = "hello world!"
mh = mysqlHandle()

# students_info = [
#     {'id':1,'name':'alex','age':22,'sex':'male','score':88},
#     {'id':2,'name':'egon','age':18,'sex':'male','score':87},
#     {'id':3,'name':'xiaoming','age':16,'sex':'female','score':60},
#     {'id':4,'name':'wangwei','age':31,'sex':'male','score':13},
# ]
#  学生信息(1, 'alex', 22, 'male', 88)
#导入蓝图
#添加学生
app.register_blueprint(stu_add.stu_add)
#学生删除
app.register_blueprint(stu_del.stu_del)
#编辑学生
app.register_blueprint(stu_edit.stu_edit)

#  中间件
@app.before_request
def is_login():
    white_list = ['/login',]
    if request.path in white_list:
        return None
    if session.get("is_login") and session["is_login"] + 3000*60 > time.time():
        return None
    else:
        return redirect('/login')


@app.route('/')
def hello_world():
    return 'Hello World!'

#登录视图
@app.route("/login",endpoint="login",methods=("GET","POST"))
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # 这里日后使用数据库存储管理员信息
        if username == "alex" and password == "123":
            session["is_login"] = time.time()
            return redirect("/students_manage")
        else:
            msg = "用户名或密码错误"
            return render_template("login.html",msg=msg)

#学生管理视图
@app.route("/students_manage")
def students_manage():
    #读取数据库信息
    students_info = mh.read()
    print(students_info)
    return render_template("students_manage.html",students=students_info)

@app.errorhandler(404)
def error(*args):
    return "没有找到当前页面"


if __name__ == '__main__':
    app.run(debug=True)
