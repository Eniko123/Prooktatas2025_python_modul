#### These are the helper functions of task one ####
import datetime
import random
def random_generator():
    pass
    dates = []
    start_date = datetime.datetime.strptime("2024-11-12", "%Y-%m-%d")
    end_date = datetime.datetime.strptime("2024-12-12", "%Y-%m-%d")
    day = start_date
    while day <= end_date:
        dates.append(day.strftime("%Y-%m-%d"))
        day += datetime.timedelta(days=1)

    for date in dates:
        with open("data.txt", "a", encoding="utf-8") as file:
            weather_options = ["windy", "sunny", "rainy", "foggy", "nothing weather"]
            file.write(f'Date: {date}\n')
            file.write(f'Weather: {random.choice(weather_options)}\n')
            file.write(f'Degrees: {round(random.uniform(0, 20), 2)} C\n')
            file.write(f'Rain probability: {round(random.uniform(0, 100), 2)} %\n')
####################################################
def task_one():
    """
    This function generates random weather data and allows users to retrieve reports and statistics by date.
    """

    start = input("For asking down the data enter 'start':")
    data = {}
    try:
        if start == 'start':
            random_generator()

            with open ('data.txt', "r", encoding='utf-8') as file:
                act_dict = {}
                for line in file:
                    line = line.strip()
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip()
                    if key == "Date":
                        current_date = value
                        day_date = {}
                    else:
                        day_date[key] = value
                    if key == "Rain probability":
                        data[current_date] = day_date
                        day_date = {}
        print(data)

    except ValueError:
        print('Invalid input!')

    answer = input('What would you like to do?\nTo get a daily/monthly report press: 1\nTo get a statistics between two dates press: 2\nTo quit program press: end, q, quit\n')
    while answer.lower() not in ['end', 'q', 'quit']:
        if answer == "1":
            day_or_month = input('Are you interested in day or month report?')
            if day_or_month == "day":
                day = input("Please enter a date (YYYY-MM-DD): ")
                if day in data:
                    print(f"The whether in {day}: \n{data[day]}")
                else:
                    print("Invalid input date")
                answer = input('What would you like to do?\nTo get a daily/monthly report press: 1\nTo get a statistics between two dates press: 2\nTo quit program press: end, q, quit\n')
            elif day_or_month == "month":
                month = input("Please enter the month (YYYY-MM): ")
                month_days = []
                for d in data:
                    if d.startswith(month):
                        month_days.append((d, data[d]))
                if month_days:
                    print(f"Weather report for {month}:")
                    for day, info in month_days:
                        print(f"{day}: {info}")
                else:
                    print("Invalid input date")
                answer = input('What would you like to do?\nTo get a daily/monthly report press: 1\nTo get a statistics between two dates press: 2\nTo quit program press: end, q, quit\n')
            else:
                print("Invalid input!")

        elif answer == "2":
            starter = input("Please enter the first date (YYYY-MM-DD)")
            finisher = input("Please enter the second date (YYYY-MM-DD)")

            start_date = datetime.datetime.strptime(starter, "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(finisher, "%Y-%m-%d").date()

            current = start_date
            degrees = []
            max_temp = None
            rainy_days = 0
            nothing_days = 0

            while current <= end_date:
                date_str = current.strftime("%Y-%m-%d")
                if date_str in data:
                    temp = float(data[date_str]["Degrees"].replace("C", "").strip())
                    degrees.append(temp)
                    if max_temp is None or temp > max_temp:
                        max_temp = temp

                    weather = data[date_str]["Weather"].lower()
                    if "rain" in weather:
                        rainy_days += 1
                    elif "nothing" in weather:
                        nothing_days += 1
                else:
                    print("One or both dates are not found in the data.")
                current += datetime.timedelta(days=1)
            print(f"Statistics between {start_date} and {end_date}"
                    f"Average degrees: {round(sum(degrees)/len(degrees), 2)}"
                    f"Number of rainy days: {rainy_days}"
                    f"Number of nothing days: {nothing_days}")
            answer = input(
                'What would you like to do?\nTo get a daily/monthly report press: 1\nTo get a statistics between two dates press: 2\nTo quit program press: end, q, quit\n')

        else:
            print ("Invalid input. Try again.")


def task_two():
    """
    This function analyzes coin toss results from a file and calculates basic statistics.
    """

    with open ("kiserlet.txt", "r", encoding='utf-8') as file:
        counter = 0
        counter_head = 0
        counter_tail = 0
        prev = ''
        counter_two_head = 0
        for line in file:
            counter += 1
            if line.strip() == "F":
                counter_head += 1
            elif line.strip() == "I":
                counter_tail += 1
            if prev == "F" and line.strip() == "F":
                counter_two_head += 1
            prev = line.strip()
        print(f"The original experiment consisted of {counter} tries.")
        print(f"From the experiment {counter_head} was head and {counter_tail} was tail.")
        print(f"From the experiment {counter_two_head} times only two heads came after each other.")


def task_three():
    """
    This function finds the base systems in which two different representations refer to the same decimal number.
    """

    num1 = '110a10101'
    num2 = '223313020003'

    # the first number at least base 11 (because a)
    for base1 in range(11,17):
        try:
            solution1 = int(num1, base1)
        except ValueError:
            continue

    # the second form at least base 4 (because 3)
        for base2 in range(4,17):
            try:
                solution2 = int(num2, base2)
            except ValueError:
                continue

            if solution1 == solution2:
                print(f"{num1} in base {base1} = {solution1}")
                print(f"{num2} in base {base2} = {solution2}")
                return

