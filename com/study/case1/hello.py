# 
# @Author: QinYong by 2017/6/22
# @Desc: 


from flask import Flask,render_template

app = Flask(__name__,root_path="D:/git/rabbit/")

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

if __name__ == '__main__':
    print (app.static_folder)
    print (app.static_url_path)
    app.run()





