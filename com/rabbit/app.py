# 
# @Author: QinYong by 2017/6/16
# @Desc: 

from flask import Flask,url_for,request

# app = Flask(__name__,root_path="D:/git/rabbit/")
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route("/my/<name>")
def hello(name):
    return 'hello world! I am %s'%(name)

with app.test_request_context():
    print (url_for("index"))
    print (url_for("hello",name="zhangsan"))
    print (url_for('static',filename="jquery.js"))

if __name__ == '__main__':
    app.run()


