from flask import Flask
import random
app = Flask(__name__)
facts_list =["Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.",
            "Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время."]

@app.route("/")
def halo():
    return'''<h1>Здесь секретик!</h1>
    <a href="/randoms">Кликай</a>'''

@app.route("/randoms")
def noting():
    return'''
    <html>
        <head>
            <title>Полезная информация!</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
        <img src="https://media3.giphy.com/media/26BGGxgsEh42ABHFe/giphy.gif?cid=ecf05e47fewnmm2h6vijgpd1768vz8zxo441mpec89684gtw&rid=giphy.gif&ct=g" alt="Image 1">
        </body>
    </html>
    '''
@app.route("/")
def hello_world():
    return '''<h1>Информация о технологической зависимости</h1>
              <a href="/random_fact">Посмотреть случайный факт!</a>'''

@app.route("/random_fact")
def facts_random():
    return f"<p>{random.choice(facts_list)}</p>"

app.run(debug=True)
