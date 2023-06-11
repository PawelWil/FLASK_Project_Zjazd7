from flask import Flask
from datetime import datetime
import random

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/date')
def current_date():
    return f'Response time:{str(datetime.now())}'

@app.route('/date2')
def current_date_two():
    return 'sadasasdasd'



counter = 0
@app.route ('/counter')
def counter_view():
    global counter
    counter += 1
    return f'Counting of opening:{counter} '



@app.route ('/color')
def random_color():
    colors = ['red', 'blue', 'green']
    return colors [random.randint(0, 2)]


@app.route ('/hello-world') # podstawowy sposów
def hello_world_html():
    return"""
    <h1>Pierwszy HTML!</h1>
    <div><b>Hello</b>world</div>
    """

@app.route ('/hello-world') # na bazie szablonu - po prostu szybciej, podtsawienie danych przez nas jest robiony w folderze TEMPLATES
def hello_world_html():
    return"""
    <h1>Pierwszy HTML!</h1>
    <div><b>Hello</b>world</div>
    """

print(app.url_map) #dostajemy na konsole mapę naszych zdefiniowanych end-pointów


if __name__ == '__main__':
    app.run()
