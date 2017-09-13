# __author: Lambert
# __date: 2017/9/13 14:41
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN_DB = '%s/db/main_dict' % BASE_DIR
TEACHER_DB = '%s/db/teachers_dict' % BASE_DIR
DATA_DIR = {
    'courses': 'courses',
    'students': 'students',
    'teachers': 'teachers'
}
