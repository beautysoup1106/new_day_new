def initial():  # 初始化
    global _global_dict
    _global_dict = {}


def set_value(key, value):
    """ 定义一个全局变量 """
    _global_dict[key] = value


def get_value(key, defvalue='test,t1'):
    try:
        return _global_dict[key]
    except KeyError:
        return defvalue


initial()
if __name__ == '__main__':
    a = get_value('env', defvalue='test,t1')


