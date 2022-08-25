
# 将字典结构数据保存为 .json 格式文件，并打开
import json

#读写json格式文件数据
def wr_json(data:dict=None,#字典格式数据
            path_file:str=None,#数据保存路径
            type:str=None#读写方式
            ):
    if type=='write':
        dict_json = json.dumps(data)  # 转化为json格式文件
        with open(path_file, 'w+') as file:
            file.write(dict_json)
    elif type=='read':
        # 读取.json格式文件的内容
        with open(path_file, 'r+') as file:
            content = file.read()
            content = json.loads(content)  # 将json格式文件转化为python的字典文件
        return content
    elif type == 'add':#同键修改，异键添加
        # 读取.json格式文件的内容
        with open(path_file, 'r+') as file:
            content = file.read()
            content = json.loads(content)  # 将json格式文件转化为python的字典文件

        for key in data.keys():
            content[key]=data[key]

        content = json.dumps(content)  # 转化为json格式文件
        with open(path_file, 'w+') as file:
            file.write(content)

if __name__=='__main__':
    pass

    #1.写入数据，没有文件则创建
#     wr_json(data = {
#     'TOEFL':0,
#     'GMAT':5,
#     'Japanese':10
# },# 代保存字典文件
#             path_file='book.json',
#             type='写入'# 读写方式
#             )

    #2.读取数据
    # content = wr_json(
    #                 path_file='数据文件/基础数据.json',
    #                 type='读取'  # 读取方式
    #                 )

    #3.添加修改数据，同键修改，异键添加
    # wr_json(data={'c': 4, 'd': [2, 6, 4, 3, 2], 'e': {'d': 4, 'e': 5}},# 代保存字典文件
    #         path_file='数据文件/基础数据.json',
    #         type='修改添加'# 读写方式
    #         )


