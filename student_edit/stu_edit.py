from flask import Blueprint,request,render_template,redirect
from models import mysqlHandle
stu_edit = Blueprint("stu_edit",__name__)
mh = mysqlHandle()
#(1, 'alex', 22, 'male', 88)    id 0 name 1    age 2   sex 3   score 4

@stu_edit.route("/edit",methods=("GET","POST"))
def student_edit():
    if request.method == "GET":
        edit_id = int(request.args.get("id"))
        edit_user = mh.read_student(edit_id)
        if not edit_user:
            return "没有找到该用户"
        return render_template("student_edit.html",student=edit_user)
    else:
        user_dict = dict(request.form)   #原始数据
        print(user_dict.values())
        #将后端数据转换为元组，存入mysql
        mh.update(tuple(user_dict.values()))
        return redirect("/students_manage")
