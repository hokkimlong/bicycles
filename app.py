#\app.py
from bottle import route,run

@route('/')
def main():
    return "hello World"

@route('/home')
def main():
    return "hi"

@route('/contact')
def main():
    return "apple"

run(host='localhost',port=3000,debug=True,reloader=True)