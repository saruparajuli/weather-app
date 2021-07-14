
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
import requests
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    city = 'Perth'
    if request.method == 'POST':
        city = request.form.get('city')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=3ce596d15787dfe85882c22fa17da1c2'

    r = requests.get(url.format(city)).json()

    weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    print(weather)

    return render_template('weather.html', weather=weather)