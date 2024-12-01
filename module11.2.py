import inspect
from pprint import pprint

def introspection_info(obj):
    info_dic: dict = {}
    print('type:', type(obj))
    info_dic['type'] = type(obj)
    print('attributes:', dir(obj))
    info_dic['attributes'] = dir(obj)
    print('module:', inspect.getmodule(obj))
    info_dic['module'] = inspect.getmodule(obj)

    return info_dic


info = introspection_info(42)
print()
pprint(info)





