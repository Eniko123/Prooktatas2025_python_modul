import json
def json_write(path, dictionary): #pl("random_user_data.txt", users}
    """A megadott szótárat JSON fájlba írja."""

    with open(path, "w", encoding="utf-8") as file:
        json.dump(dictionary, file, indent=4, ensure_ascii=True)


def json_export(path, dictionary):
    """Szűrt adatokat külön JSON fájlba ment."""

    with open(path, "w", encoding="utf-8") as file:
        json.dump(dictionary, file, indent=4, ensure_ascii=True)


def json_load(path):
    """Beolvassa a JSON fájl tartalmát és JSON szövegként adja vissza."""

    with open(path, "r", encoding="utf-8") as file:
        json_string = file.read()
    return json_string

####Filters####

def no_worker():
    """Kiszűri a nem dolgozó felhasználókat és menti őket a no_worker.json fájlba."""
    json_string = json_load("random_user_data.txt")
    users = json.loads(json_string)

    no_workers = []
    for user in users:
        if user["workstat"] == False:
            no_workers.append(user)
    json_export("no_worker.json", no_workers)


def over65():
    """Kiszűri a 65 év feletti felhasználókat, és menti őket az over65.json fájlba."""
    json_string = json_load("random_user_data.txt")
    users = json.loads(json_string)

    over65 = []
    for user in users:
        if user["age"] > 65:
            over65.append(user)
    json_export("over65.json", over65)


def HU_cizizen():
    """Kiszűri a magyar állampolgárokat, és menti őket a middle_eu.json fájlba."""
    json_string = json_load("random_user_data.txt")
    users = json.loads(json_string)

    HU_ciziten = []
    for user in users:
        if user["land"] == "HU".upper():
            HU_ciziten.append(user)
    json_export("middle_eu.json", HU_ciziten)

import datetime
def expire180():
    json_string = json_load("random_user_data.txt")
    users = json.loads(json_string)

    expire180 = []
    for user in users:
        date1 = datetime.datetime.now()
        date2 = datetime.datetime.strptime(user["vote"], "%Y-%m-%d")
        difference = (date2 - date1).days
        if 0 <= difference <= 180:
            expire180.append(user)
    json_export("expire180.json", expire180)
