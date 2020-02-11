from flask import Blueprint,request,redirect
from models import mysqlHandle
stu_del = Blueprint("stu_del",__name__)
mh = mysqlHandle()

@stu_del.route("/delete",methods=("GET","POST"))
def student_delete():
    #1.获取删除的id
    #2.删除数据
    #3.重定向到学生管理界面
    del_ids = []
    if request.args.get("id"):
        del_id = int(request.args.get("id"))
        del_ids.append(del_id)
    elif request.json:
        del_ids = request.json
    print(del_ids)  #需要删除的元素的id列表，

    #遍历，一个一个删除
    for id in del_ids:
        mh.delete(id)

    return redirect("/students_manage")