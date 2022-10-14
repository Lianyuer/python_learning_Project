"""
文件相关的类
"""

import json
from data_define import Record


class FileReader:

    def data_reader(self, path) -> list[Record]:
        pass


class TextReader(FileReader):

    def __init_(self, path):
        self.path = path

    def data_reader(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()
            record = Record(record_list[0], record_list[1], int(record_list[2]), record_list[3])
            record_list.append(record)
        f.close()
        return record_list
