# __author: Lambert
# __date: 2017/9/13 11:44


class School:
    def __init__(self, name, address):
        self.school_name = name
        self.school_address = address
        self.school_course = {}  # 学校所有的课程实例
        self.school_class = {}
        self.school_teacher = {}

    def cat_school(self):
        print('学校名称：【%s】' % self.school)

    def creat_course(self, course_name, course_time, course_price):
        course_obj = Course(course_name, course_time, course_price)
        self.school_course[course_name] = course_obj

    def creat_grade(self, grade_name, grade_course):
        grade_obj = Grades(grade_name, grade_course)
        self.school_class[grade_name] = grade_obj

    def creat_teacher(self, teacher_name, teacher_salary):
        teacher_obj = Teacheres(teacher_name, teacher_salary)
        self.school_class[teacher_name] = teacher_obj


class Grades():
    def __init__(self, grade_name, grade_course):
        self.grade_course = grade_course
        self.grade_name = grade_name
        self.grade_student = {}


class Teacheres():
    def __init__(self, teacher_name, teacher_salary,teacher_grade):
        self.teacher_name = teacher_name
        self.teacher_salary = teacher_salary
        self.teacher_grades = [teacher_grade]


class Course:
    def __init__(self, n, t, p):
        self.name = n
        self.time_cycle = t
        self.price = p
