from app import app
import datetime
import random

@app.route('/')
def index_main():
    return "hello, World!"
''' обращаемся к объекту арр(класса Фласк из файла арр) используем его метод route, '/' -означает корень сайта, домен второго уровня'''
''' и определяем индексную вьюху, которая нам возвратит строку. @ говорит о том что метод роут является декоратором функции index'''

@app.route('/time')
def index_time():
    d = datetime.datetime.today()
    now = str(d.isoformat(" ", "minutes"))
    return now


@app.route('/random')
def index_random():
    r = str(random.randrange(1, 10 ** 6 + 1, 1))
    return r