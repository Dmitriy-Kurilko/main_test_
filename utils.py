import json


def load_dates():# создание главной страницы со всеми данными из json-файла
    with open('templates/data1.json', 'r', encoding="utf8") as schedule:
        return json.load(schedule)


def load_dates_from_days(day):# выгрузка данных за текущий день
    list_ = []
    for day_ in load_dates():
        if day_['days'] == day:
            list_.append(day_)
    assert len(list_) != 0, 'В этот день в расписании не поездов'
    return list_


def when_train_arrive_and_depart(number):# фильтровка данных, в какое время прибывает и убывает поезд
    print("Выведется в формате: отправление, прибытие")
    list_with_time = []
    for day in load_dates():
        if number == day["number_train"]:
            list_with_time.append(day["departure"])
            list_with_time.append(day["arrival"])
    assert len(list_with_time) != 0, 'В расписании нет поезда с таким номером'
    return " ".join(list_with_time)


def where_trains_halts(number):# фильтовка данных, через какие станции проезжает тот или иной поезд
    print('Выведется в формате: остановки')
    list_with_halts = []
    for day in load_dates():
        if number == day["number_train"]:
            list_with_halts.append(day["halt"])

    assert len(list_with_halts) != 0, 'В расписании нет поезда с таким номером'
    return " ".join(list_with_halts)
