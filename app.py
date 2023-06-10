from flask import Flask
from datetime import datetime


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

if __name__ == '__main__':
    app.run()
