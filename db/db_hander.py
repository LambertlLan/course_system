# __author: Lambert
# __date: 2017/9/13 14:40
from conf import setting
import pickle


def write_data(dic):
    with open(setting.DB_PATH, 'wb') as f:
        pickle.dump(dic, f)


def read_data():
    with open(setting.DB_PATH, 'rb') as f:
        data = pickle.load(f)
        return data


def update_data(obj):
    main_data = read_data()
    main_data[getattr(obj, 'school_name')] = obj
    write_data(main_data)
