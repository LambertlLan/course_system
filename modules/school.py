# __author: Lambert
# __date: 2017/9/13 11:44


class School:
    def __init__(self, name):
        self.school = name

    def cat_school(self):
        print('学校名称：【%s】' % self.school)


class Grades():
    def __init__(self, c, t, n, s):
        self.course = c
        self.teacher = t
        self.name = n
        self.school = s


class Teacheres():
    def __init__(self, n, s):
        self.name = n
        self.school = s
