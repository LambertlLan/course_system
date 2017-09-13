# __author: Lambert
# __date: 2017/9/13 11:36
from modules.school import School, Grades
from modules.course import Course
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
    def __init__(self, main_dict, current_school):
        self.main_dict = main_dict
        self.current_school = current_school
        menu = '''
            =================欢迎进入【%s】学院================
            1.创建班级
            2.招聘讲师
            3.创建课程
            ''' % self.current_school
        menu_dict = {
            '1': self.creat_grades,
            '2': self.creat_teacher,
            '3': self.creat_teacher
        }
        print(menu)
        choise = input('选择要进入的模式>>>')
        if choise in menu_dict:
            menu_dict[choise]()
            # admin_menu_dict[admin_inp]()

    def creat_course(self):
        Flag = True
        while Flag:
            course_name = input('请输入课程名称>>>')
            if self.main_dict[self.current_school][getattr(self.main_dict[self.current_school], course_name)]:
                print('当前课程已存在')
                continue
            time_cycle = input('请输入课程时间周期>>>')
            price = input('请输入价格>>>')
            course_obj = Course(course_name, self.current_school, time_cycle, price)
            self.main_dict[self.current_school] = {course_obj: {'students': [], 'teachers': []}}
            db_hander.write_data(setting.MAIN_DB, self.main_dict)
            print('创建课程成功即将返回上一级')
            time.sleep(1)
            self.__init__()

    def creat_teacher(self):
        pass

    def creat_grades(self):
        pass


def teacher_center():
    pass


def student_center():
    pass


def init_db():
    bj = School('北京')
    sh = School('上海')
    if not os.path.exists(setting.MAIN_DB):
        main_dic = {bj: {}, sh: {}}
        db_hander.write_data(setting.MAIN_DB, main_dic)
    if not os.path.exists(setting.TEACHER_DB):
        teacher_dic = {}
        db_hander.write_data(setting.TEACHER_DB, teacher_dic)


def run():
    init_db()
    meun = '''
    1.管理员登录
    2.老师登录
    3.学生登录
    '''
    print(meun)
    inp = input('请输入操作编号>>>')
    main_dict = db_hander.read_data(setting.MAIN_DB)

    if inp == '1':
        for key in main_dict:
            key.cat_school()
        school_inp = input('请输入学校名称>>>')
        for key in main_dict:
            if hasattr(key, school_inp):
                current_school = key
                obj = School_center(main_dict, current_school)
                break
