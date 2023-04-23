# import gitpython
import os
# from pathlib import Path


class filemgr:
    """简单的文件读写管理"""
    # path_full = ""
    # output = ""
    # 仅作为提示用

    def __init__(self, file_path, file_name):
        self.path_full = os.path.join(file_path ,file_name)
        # 路径修正 "/"
        self.file_stage = os.path.exists(self.path_full)
        # goal_file = Path(file_path+file_name)
        if self.file_stage is True:
            pass
        else:
            self.file_object = open(self.path_full, mode='x', encoding='utf-8')
            self.file_object.close
        # 如果文件存在就跳过，若不存在则新建
    # init方法

    @property
    def size(self):
        # 获取文件大小
        return os.path.getsize(self.path_full)

    @property
    def data(self):
        # 以只读属性的形式读取文件数据
        return self.load()

    def load(self):
        if self.size != 0:
            # 当文件非空时读取数据
            self.file_object = open(self.path_full, mode='r', encoding='utf-8')
            self.output = self.file_object.read()
            self.file_object.close
            return self.output
        else:
            return ""
            # 当文件为空时返回空值
        # 使用只读模式打开文件，并全部读取

    def write(self, input_object):
        self.file_object = open(self.path_full, mode='w', encoding='utf-8')
        self.file_object.write(input_object)
        self.file_object.close
        # 使用覆写模式打开文件，并覆写
