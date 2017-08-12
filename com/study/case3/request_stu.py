# 
# @Author: QinYong by 2017/6/26
# @Desc: 



from flask import Flask,request

app = Flask(__name__)


with app.test_request_context("/hello"):
    assert request.path == "/hello"
# with app.request_context(environ):
#     assert request.method == 'POST'


if __name__ == '__main__':
    app.run()

