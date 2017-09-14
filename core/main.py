# __author: Lambert
# __date: 2017/9/13 11:36
from modules.school import School, Grades
from db import db_hander
from conf import setting
import os, time


class School_center:
    def __init__(self, curr_school_obj):
        self.school = curr_school_obj

    def add_course(self):
        Flag = True
        while Flag:
            course_name = input('请输入课程名称>>>')
            time_cycle = input('请输入课程时间周期>>>')
            price = input('请输入价格>>>')
            self.school.creat_course(course_name, time_cycle, price)
            db_hander.update_data(self.school)
            print('创建课程成功即将返回上一级')
            Flag = False

    def add_teacher(self):
        teacher_name = input('请输入讲师名称>>>')
        teacher_salary = input('请输入讲师薪资>>>')
        teacher_grade = input('请输入需要关联的班级>>>')
        if teacher_name in self.school.school_teacher:
            self.school.school_teacher[teacher_name].teacher_salary = teacher_salary
            self.school.school_teacher[teacher_name].teacher_grade.append(teacher_grade)
            print('该讲师已经存在，更新完成')
        else:
            self.school.creat_teacher(teacher_name, teacher_salary, teacher_grade)
        db_hander.update_data(self.school)
        print('创建讲师成功即将返回上一级')

    def add_grades(self):
        grade_name = input('请输入班级名称>>>')
        grade_course = input('请输入要关联的课程>>>')
        self.school.creat_grade(grade_name, grade_course)
        db_hander.update_data(self.school)
        print('创建班级成功即将返回上一级')

    def show_course(self):
        for key in self.school.school_course:
            value = self.school.school_course[key]
            course = '''
            课程名称【%s】,时间周期【%s】,价格【%s】
            ''' % (value.name, value.time_cycle, value.price)
            print(course)

    def show_teacher(self):
        for key in self.school.school_teacher:
            value = self.school.school_teacher[key]
            teacher = '''
            老师姓名【%s】，薪资【%s】，班级【%s】
            ''' % (value.teacher_name, value.teacher_salary, value.teacher_grades)
            print(teacher)

    def show_grades(self):
        for key in self.school.school_class:
            value = self.school.school_class[key]
            students = []
            for students_key in value.grade_student:
                students.append(students_key)
            grades = '''
            班级【%s】，课程【%s】，学生【%s】
            ''' % (value.grade_name, value.grade_course, students)
            print(grades)


class Teacher_center:
    def __init__(self, curr_school_obj):
        self.school = curr_school_obj

    def show_teacher(self, teacher_name):
        if teacher_name in self.school.school_teacher:
            self.curr_teacher = teacher_name
            value = self.school.school_teacher[teacher_name]
            teacher = '''
            登录成功！
            老师姓名【%s】，薪资【%s】，班级【%s】
            ''' % (value.teacher_name, value.teacher_salary, value.teacher_grades)
            print(teacher)
            return True
        else:
            return False

    def show_grades(self):
        grade_inp = input('请输入要查看的班级的名称>>>')
        value = self.school.school_class[grade_inp]
        students = []
        for students_key in value.grade_student:
            students.append(students_key)
        grades = '''
            班级【%s】，课程【%s】，学生【%s】
            ''' % (value.grade_name, value.grade_course, students)
        print(grades)

    def show_student(self):
        grade_inp = input('请输入学生所属班级>>>')
        for key in self.school.school_class[grade_inp].grade_student:
            value = self.school.school_class[grade_inp].grade_student[key]
            grades = '''
                姓名【%s】，年龄【%s】
                ''' % (key, value.student_age)
            print(grades)


class Student_center:
    def __init__(self, curr_school_obj):
        self.school = curr_school_obj

    def add_student(self):
        student_name = input('请输入学生姓名>>>')
        student_age = input('请输入学生年龄>>>')
        student_grade = input('请输入选择的班级>>>')
        self.school.creat_student(student_name, student_age, student_grade)
        db_hander.update_data(self.school)


def init_db():
    if not os.path.exists(setting.DB_PATH):
        bj = School('北京', '北京市')
        sh = School('上海', '上海市')
        main_data = {'北京': bj, '上海': sh}
        db_hander.write_data(main_data)


def run():
    init_db()
    while True:
        meun = '''
        1.管理员登录
        2.老师登录
        3.学生登录
        '''
        print(meun)
        inp = input('请输入操作编号>>>')
        main_data = db_hander.read_data()
        for key in main_data:
            print(key)
        school_inp = input('请输入学校名称>>>')
        if school_inp in main_data:
            curr_school_obj = main_data[school_inp]
        if inp == '1':
            Flag = True
            while Flag:
                menu = '''
                    =================欢迎进入【%s】学院 管理员模式================
                    1.创建课程
                    2.创建班级
                    3.招聘讲师
                    4.查看课程
                    5.查看班级
                    6.查看讲师
                    0.选择学院
                    ''' % school_inp
                menu_dict = {
                    '1': 'add_course',
                    '2': 'add_grades',
                    '3': 'add_teacher',
                    '4': 'show_course',
                    '5': 'show_grades',
                    '6': 'show_teacher',
                    '0': 'back'
                }
                print(menu)
                choise = input('选择要进入的模式>>>')
                if choise in menu_dict:
                    if choise == '0':
                        break
                    else:
                        obj = School_center(curr_school_obj)
                        getattr(obj, menu_dict[choise])()

        elif inp == '2':
            teacher_flag = True
            while teacher_flag:
                teacher_admin = input('请输入讲师姓名>>>')
                obj = Teacher_center(curr_school_obj)
                has_teacher = obj.show_teacher(teacher_admin)
                if not has_teacher:
                    print('无该讲师')
                else:
                    teacher_flag = False
                    Flag = True
                    while Flag:
                        menu = '''
                            =================欢迎进入【%s】学院 讲师模式================
                            1.查看教授班级
                            2.查看学生信息
                            0.选择学院
                            ''' % school_inp
                        menu_dict = {
                            '1': 'show_grades',
                            '2': 'show_student',
                            '0': 'back'
                        }
                        print(menu)
                        choise = input('选择要进入的模式>>>')
                        if choise in menu_dict:
                            if choise == '0':
                                break
                            getattr(obj, menu_dict[choise])()
        elif inp == '3':
            Flag = True
            while Flag:
                menu = '''
                    =================欢迎进入【%s】学院 学生模式================
                    1.注册
                    2.查看班级
                    0.选择学院
                    ''' % school_inp
                menu_dict = {
                    '1': 'add_student',
                    '2': 'show_grades',
                    '0': 'back'
                }
                print(menu)
                choise = input('选择要进入的模式>>>')
                if choise in menu_dict:
                    if choise == '0':
                        break
                    elif choise == '2':
                        obj = School_center(curr_school_obj)
                    else:
                        obj = Student_center(curr_school_obj)
                    getattr(obj, menu_dict[choise])()
