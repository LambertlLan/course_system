# __author: Lambert
# __date: 2017/9/13 11:36
from modules.school import School, Grades
from db import db_hander
from conf import setting
import os, time


# def creat_course():
#     course_name = input('请输入课程名称>>>')
#     time_cycle = input('请输入课程时间周期>>>')
#     price = input('请输入价格>>>')
#     print(school)
#     school_inp = input('请选择设置的学校>>>')
#     course_obj = course.course(course_name, school_dict[school_inp], time_cycle, price)
#     db_course = db_hander.write_data(setting.DATA_DIR['courses'], course_obj)
#     return db_course
#
#
# def creat_classes(course_obj, teacher_name, class_name, school_name):
#     classes_obj = school.modules(course_obj, teacher_name, class_name, school_name)
#     db_classes = db_hander.write_data(setting.DATA_DIR['modules'], class_name, classes_obj)
#     return db_classes
#
#
# def creat_teacher(teacher_name, school_name):
#     teacher_obj = school.teacher(teacher_name, school_name)
#     db_teacheres = db_hander.write_data(setting.DATA_DIR['teachers'], teacher_name, teacher_obj)
#     return db_teacheres


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
            print(key)

    def show_grades(self):
        for key in self.school.school_class:
            print(key)


def teacher_center():
    pass


def student_center():
    pass


def init_db():
    if not os.path.exists(setting.DB_PATH):
        bj = School('北京', '北京市')
        sh = School('上海', '上海市')
        main_data = {'北京': bj, '上海': sh}
        db_hander.write_data(main_data)


def run():
    init_db()
    meun = '''
    1.管理员登录
    2.老师登录
    3.学生登录
    '''
    print(meun)
    inp = input('请输入操作编号>>>')
    if inp == '1':
        main_data = db_hander.read_data()
        sch_flag = True
        while sch_flag:
            for key in main_data:
                print(key)
            school_inp = input('请输入学校名称>>>')
            if school_inp in main_data:
                curr_school_obj = main_data[school_inp]
                Flag = True
                while Flag:
                    menu = '''
                        =================欢迎进入【%s】学院================
                        1.创建课程
                        2.创建班级
                        3.招聘讲师
                        4.查看课程
                        5.查看班级
                        6.查看讲师
                        7.选择学院
                        ''' % school_inp
                    menu_dict = {
                        '1': 'add_course',
                        '2': 'add_grades',
                        '3': 'add_teacher',
                        '4': 'show_course',
                        '5': 'show_grades',
                        '6': 'show_teacher'
                    }
                    print(menu)
                    choise = input('选择要进入的模式>>>')
                    if choise in menu_dict:
                        if choise == '7':
                            break
                        else:
                            obj = School_center(curr_school_obj)
                            getattr(obj, menu_dict[choise])()
