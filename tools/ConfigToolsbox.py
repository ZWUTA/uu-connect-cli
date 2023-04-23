# from Src.FileToolsbox import filemgr
from .FileToolsbox import filemgr
import json


class cfgmgr:
    """简单的配置文件工具，保存配置信息采用字典..."""

    # json_val = ""
    # object_val = ""

    # path_full = ""
    # json_object = ""
    # 只是列一下可能会用到的变量

    def __init__(self, file_path, file_name):
        self.path_full = file_path + file_name
        self.json_object = filemgr(file_path, file_name)
        # 拼合路径，并实例化文件管理器
        # 注意 此处路径不是完整的
        # 文件管理模块会在最后加上 /

    def load(self):
        if self.json_object.size != 0:
            # 当json对象不为空时读取，否则返回空值
            self.json_val = self.json_object.load()
            self.object_val = json.loads(self.json_val)
            return self.object_val
        else:
            return {}
            # 返回空字典

    def write(self, input_object):
        self.json_val = json.dumps(input_object,
                                   sort_keys=True, indent=4,
                                   separators=(',', ':'))
        # 设置了Json格式化
        self.json_object.write(self.json_val)

    def cache_init(self):
        self.cache = self.load()

    def cache_commit(self):
        self.write(self.cache)
