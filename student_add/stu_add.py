from flask import Blueprint,request,render_template,redirect
from models import mysqlHandle
stu_add = Blueprint("stu_add",__name__)
mh = mysqlHandle()
#(1, 'alex', 22, 'male', 88)    id 0 name 1    age 2   sex 3   score 4
@stu_add.route("/student_add",methods=("GET",'POST'))
def student_add():
    if request.method == "GET":
        return render_template("student_add.html")
    else:
        print(request.form)
        user_dict = dict(request.form)
        #读取数据库，获得所有列表，获取最后一个id
        current_id = mh.get_student_num()+1
        user_info = []
        user_info.append(current_id)
        user_info.extend(user_dict.values())
        print(user_info)
        #写入数据库
        mh.write(tuple(user_info))
        return redirect("/students_manage")