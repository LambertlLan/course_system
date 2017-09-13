# __author: Lambert
# __date: 2017/9/13 14:40
from conf import setting
import pickle


def write_data(path, dic):
    with open(path, 'wb') as f:
        pickle.dump(dic, f)


def read_data(path):
    with open(path, 'rb') as f:
        data = pickle.load(f)
        return data
