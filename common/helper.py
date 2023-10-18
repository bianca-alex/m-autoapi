# 根据var，逐层获取json格式的值
def parse_relation(var, data):
    # 判断变量var是否存在
    if not var:
        # 不存在直接返回data内容
        return data
    else:
        # 存在则获取数组第1个内容
        data = data.get(var[0])

        del var[0]
        
        return parse_relation(var, data)

if __name__ == "__main__":
    json_data = {
        "data": {
            "user": {
                "name": "John",
                "age": 30
            },
            "status": "active"
        }
    }
    # var 用来输入层级关系
    res = parse_relation(['data', 'user'], json_data)
    print(res)