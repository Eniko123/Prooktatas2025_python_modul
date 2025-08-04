import json
def task_one():

    dictionary = {"name": "Anna", "age": 25, "city": "Budapest"}
    with open ("task_one.json", "w", encoding="utf-8") as file:
        json.dump(dictionary, file, indent=4, ensure_ascii=True)

    with open("task_one.json", "r", encoding="utf-8") as file:
        content = json.load(file)
        print(content)


def task_two():

    with open("task_one.json", "r", encoding="utf-8") as file:
        dictionary = json.load(file)

    dictionary["country"] = "Hungary"
    with open("task_one.json", "r+", encoding="utf-8") as file:
        json.dump(dictionary, file, indent=4, ensure_ascii=True)

    with open("task_one.json", "r", encoding="utf-8") as file:
        content = json.load(file)
        print(content)


def task_three():
    with open ("task_three.json", "r", encoding="utf-8") as file:
        number_list = json.load(file)

    sorted_number_list = sorted(number_list)
    print(sorted_number_list)

    with open("task_three.json", "w", encoding="utf-8") as file:
        json.dump(sorted_number_list, file, ensure_ascii=True)


def task_four():
    with open ("task_three.json", "r", encoding="utf-8") as file:
        number_list = json.load(file)

    print(f'A legkisebb elem: {number_list[0]}')
    print(f'A legnagyobb elem: {number_list[4]}')


def task_five():

    with open("task_five.json", "r", encoding="utf-8") as file:
        number_list = json.load(file)

    print(f"The scores on the list: {number_list}")
    print(f"The sum of the scores {sum(number_list)}")
    print(f"The average of the scores: {sum(number_list)/len(number_list)}")


def task_six():
    try:
        with open("task_six.json", "r", encoding="utf-8") as file:
            content = json.load(file)
            print(content)
    except FileNotFoundError:
        text = {"uzenet": "Ez egy alapértelmezett JSON fájl."}
        with open ("task_six.json", "w", encoding="utf-8") as file:
            json.dump(text, file, ensure_ascii=True)


def task_seven():
    try:
        with open("task_seven.json", "r", encoding="utf-8") as file:
            json.load(file)
            print(True)
    except json.JSONDecodeError:
        print(False)


def task_eight():
    pass
    # Írd ki a szótárakat, amelyekben a "kor" értéke nagyobb, mint 30
    # Minta JSON:
    # [
    #  {"név": "Anna", "kor": 25, "város": "Budapest"},
    #  {"név": "Péter", "kor": 35, "város": "Debrecen"},
    #  {"név": "László", "kor": 40, "város": "Szeged"},
    #  {"név": "Júlia", "kor": 28, "város": "Pécs"}
    # ]

    with open ("task_eight.json", "r", encoding="utf-8") as file:
        content = json.load(file)
        over_30 = []
        for person in content:
            if person["kor"] > 30:
                over_30.append(person)
        print(f"The people over 30 are:")
        for person in over_30:
            print(person["név"])


def task_nine():
    # Egy szavak_50.txt fájl minden sora egy szót tartalmaz. Írj egy programot, amely ezeket a
    # szavakat JSON formátumba alakítja, és menti egy fájlba.
    with open ("task_nine.txt", "r", encoding="utf-8") as file:
        content = []
        for line in file:
            content.append(line.strip())


    with open ("task_nine.json", "w", encoding="utf-8") as file:
        json.dump(content, file,  ensure_ascii=False)


import os
def task_ten():
    if not os.path.exists("task_ten_scores.json"):
        print(f'The task_ten_scores.json does not exist.')
        scores = [85, 90, 78, 92, 88, 70, 95]
        with open("task_ten_scores.json", "w", encoding="utf-8") as file:
            json.dump(scores, file, ensure_ascii=False, indent=4)
        print("File created.")

    with open ("task_ten_scores.json", "r", encoding="utf-8") as file:
        scores = json.load(file)
        max_scores = max(scores)
        min_scores = min(scores)
        mean = sum(scores) / len(scores)

    print(f"The highest score: {max_scores}")
    print(f"The lowest score: {min_scores}")
    print(f"Mean: {round(mean, 2)}")


def task_eleven():
    worker_list = [
    {
        "név": "Anna",
        "pozíció": "Mérnök",
        "fizetés": 500000
    },
    {
        "név": "Péter",
        "pozíció": "Fejlesztő",
        "fizetés": 700000
    },
    {
        "név": "László",
        "pozíció": "Projektvezető",
        "fizetés": 600000
    }
]
    with open("task_eleven.json", "w", encoding="utf-8")as file:
        json.dump(worker_list, file, ensure_ascii=False)

    list_sorted= sorted(worker_list, key=lambda dolgozo: dolgozo["fizetés"])
    print(list_sorted)
    least = min(worker_list, key=lambda d: d["fizetés"])
    most = max(worker_list, key=lambda d: d["fizetés"])
    print(f"Worker with the lowest salary: {least}")
    print(f"Worker with the highest salary: {most}")
    salary_average = sum(worker["fizetés"] for worker in worker_list)/len(worker_list)
    print(f"The average salary: {salary_average}")

task_eleven()


def main():
    task_one()
    task_two()
    task_three()
    task_four()
    task_five()
    task_five()
    task_six()
    task_seven()
    task_eight()
    task_nine()
    task_ten()
    task_eleven()
