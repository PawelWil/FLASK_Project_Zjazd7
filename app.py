from flask import Flask, render_template, abort, url_for
from datetime import datetime
import random
import pycountry_convert

from model.country import db, find_by_name, find_by_index, find_continent_by_cc

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


# @app.route ('/hello-world') # podstawowy sposób. UWAGA poniższy endpoint ma tą samą ścieżkę, więc musi ten być skomentowany, bo jak jest
# aktywny, to dwa razy się do niego odnosi i nie działa
# def hello_world_html():
#     return"""
#     <h1>Pierwszy HTML!</h1>
#     <div><b>Hello</b>world</div>
#     """

@app.route ('/hello-world') # na bazie szablonu - po prostu szybciej, podtsawienie danych przez nas jest robiony w folderze TEMPLATES
def hello_world_html():
    return render_template('welcome.html', message = 'Aplikacje Server Side są super!')



@app.route ('/countries')
def random_country():
    country_index = random.randint(0, 246)
    country = db[country_index]

    return render_template('country.html', country=country)



#Path variable: <typ:nazwa>
@app.route ('/countries/<name>')
def country_by_name(name: str):
    try:
        found_country = find_by_name(name)
    except ValueError as ex:
        abort(404, ex)
    return render_template('country.html', country=found_country)



@app.route('/countries/index/<int:index>')
def country_by_index(index: int):
    try:
        found_country = find_by_index(index)
        found_country['continent'] = find_continent_by_cc(found_country['cc'])
    except IndexError:
        abort(404, f'Country by index {index} can not be found!')
    return render_template('country_index.html', country=found_country, index=index)





print(app.url_map) #dostajemy na konsole mapę naszych zdefiniowanych end-pointów


if __name__ == '__main__':
    app.run()
