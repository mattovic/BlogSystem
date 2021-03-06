#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask
from flask import request
from flask import send_from_directory
from flask import url_for
from flask import redirect

class BlogServer:

    def __init__(self):
        pass

    def decorate(self,app):
        
        @app.route('/blog')
        def blog_index():
            return send_from_directory('/home/linaro/BlogSystem/html', 'index.html')

        @app.route('/blog/<filename>')
        def blog_article(filename):
            return send_from_directory('/home/linaro/BlogSystem/html', filename)

        @app.route('/pic/<filename>')
        def pic(filename):
            return send_from_directory('/home/linaro/BlogSystem/pic', filename)

        return app
