#用来处理mysql  读取  写入  查询 插入 修改  等操作
#  学生信息(1, 'alex', 22, 'male', 88)
import pymysql

class mysqlHandle:
    def __init__(self):
        self.conn = pymysql.connect(host="localhost",user="root",password="123",database="students_info"
                                    ,charset="utf8",autocommit=True)
        self.cursor = self.conn.cursor()
        print("connect success...")

    # 读取所有学生信息
    def read(self):
        sql = "select * from students_info;"
        res = self.cursor.execute(sql)
        students_dt = self.cursor.fetchall()
        return students_dt

    # 读取单个学生信息  返回学生信息元组，没有则返回none
    def read_student(self,id):
        sql = "select * from students_info where id=%s;"
        res = self.cursor.execute(sql,id)
        students_dt = self.cursor.fetchone()
        return students_dt

    #写入一条学生信息
    def write(self,student_info):
        sql = 'insert into students_info(id,name,age,sex,score) values(%s,%s,%s,%s,%s);'
        res = self.cursor.execute(sql,student_info)
        self.conn.commit()
        return res

    #删除一条学生信息
    def delete(self,student_id):
        sql = "delete from students_info where id=%s;"
        res = self.cursor.execute(sql,student_id)
        self.conn.commit()
        return res

    #更新学生
    def update(self,student_info):
        self.delete(student_info[0])
        return self.write(student_info)

#   获取最后一个学生id
    def get_student_num(self):
        sql = "select max(id) from students_info"
        res = self.cursor.execute(sql)
        return self.cursor.fetchone()[0]

    def __del__(self):
        self.cursor.close()
        self.conn.close()

if "__main__" == __name__:
    mh = mysqlHandle()
    # print(mh.read())
    # mh.write((5,"22",11,"male",61))
    # print(mh.delete(5))
    # print(mh.read())
    # print(mh.get_student_num())
    print(mh.read_student(5))