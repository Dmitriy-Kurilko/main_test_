from flask import Flask, render_template, jsonify
from utils import *

app = Flask(__name__, template_folder='templates')

# роуты для отображения/поиска данных
@app.route("/")
def main_page():
    data = load_dates()
    return render_template("index.html", data=data)


@app.route("/data1.json/<int:number_of_train>")
def post_page(number_of_train):
    dates_from_days = load_dates_from_days(number_of_train)
    return render_template("index.html", dates_from_days=dates_from_days)


@app.route("/data1.json/<int:number_of_train>")
def when_train_arrive_and_depart(number):
    time = when_train_arrive_and_depart(number)
    return render_template("index.html", time=time)


@app.route("/data1.json/<int:number_of_train>")
def where_trains_halts(number):
    halt = when_train_arrive_and_depart(number)
    return render_template("index.html", halt=halt)

# API
@app.route("/api/data1")
def api_main_page():
    data = load_dates()
    return jsonify(data)

# API
@app.route("/api/data1/<int:post_id>")
def api_load_dates_from_days_page(day):
    day_ = load_dates_from_days(day)
    return jsonify(day_)


# обработчик ошибок
@app.errorhandler(404)
def page_error_404(e):
    return '<h1>Error</h1><p>not found(((</p>', 404

# обработчик ошибок
@app.errorhandler(500)
def page_error_500(e):
    return '<h1>Error</h1><p>not found(((</p>', 500


app.run()
