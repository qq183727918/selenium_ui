# _*_ coding: UTF-8 _*_
# @Time     : 2021/1/14 10:20
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : goods_flask.py
# @Software : PyCharm
import flask
import json

# 实例化api，把当前这个python文件当作一个服务，__name__代表当前这个python文件
api = flask.Flask(__name__)


@api.route('/index', methods=['get'])
# get方式访问
def index():
    goods_price = flask.request.values.get('goods_price')

    ren = {'msg': '成功访问首页', 'msg_code': 200}
    # json.dumps 序列化时对中文默认使用的ascii编码.想输出中文需要指定ensure_ascii=False
    return json.dumps(ren, ensure_ascii=False)


if __name__ == '__main__':
    api.run(port=8228, debug=True, host='0.0.0.0')  # 启动服务
    # debug=True,改了代码后，不用重启，它会自动重启
    # 'host='127.0.0.1'别IP访问地址
