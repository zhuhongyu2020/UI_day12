import json,os
class Data:
    @classmethod
    def get_json_data(cls,file):
        """
        解析json数据
        :param file:在data文件夹下的文件
        :return:
        """
        # 打开文件
        with open("./Data" + os.sep + file, "r", encoding="utf-8") as f:
            return json.load(f)