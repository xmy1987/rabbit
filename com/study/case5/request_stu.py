# 
# @Author: QinYong by 2017/6/26
# @Desc: 

from flask import Flask,request

app = Flask(__name__)

@app.route('/login',methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        pass

def valid_login(username,password):
    print ('check username and password value')
    return True

def log_the_user_in(username):
    return 'user "%s" login successful !'



if __name__ == '__main__':
    app.run()
