# 
# @Author: QinYong by 2017/6/23
# @Desc: 


from flask import Markup


if __name__ == '__main__':
    s = Markup('<em>Marked up</em> &raquo; HTML').striptags()
    print (s.__repr__())
