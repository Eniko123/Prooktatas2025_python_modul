#### This is a helper function for the second task ####
def day_of_year(year, month, day):
    months_dic = {
        "january": 31,
        "february": 28,
        "march": 31,
        "april": 30,
        "may": 31,
        "june": 30,
        "july": 31,
        "august": 31,
        "september": 30,
        "october": 31,
        "november": 30,
        "december": 31
    }

    months_dic_leap = {
        "january": 31,
        "february": 29,
        "march": 31,
        "april": 30,
        "may": 31,
        "june": 30,
        "july": 31,
        "august": 31,
        "september": 30,
        "october": 31,
        "november": 30,
        "december": 31
    }

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_counter = 0
        for m in months_dic_leap:
            if m == month:
                break
            leap_counter += months_dic_leap[m]
        leap_counter += day
        return leap_counter
    else:
        normal_counter = 0
        for m in months_dic:
            if m == month:
                break
            normal_counter += months_dic[m]
        normal_counter += day
        return normal_counter
#######################################################

def first_task():
    """
    Calculates the day number within the year for a given date.
    Accounts for leap years when determining the result.
    Returns an integer between 1 and 365 (or 366 for leap years).
    """

    months_dic = {
        "january": 31,
        "february": 28,
        "march": 31,
        "april": 30,
        "may": 31,
        "june": 30,
        "july": 31,
        "august": 31,
        "september": 30,
        "october": 31,
        "november": 30,
        "december": 31
    }
    months_list = list(months_dic.keys())

    for index, month in enumerate(months_list, start=1):
        print(f"{index}: {month}")

    month_asked = int(input("Enter the month number you want to know the length of (1–12): "))
    month_name = months_list[month_asked - 1]
    days = months_dic[month_name]
    print(f'The length of {month_name} month is: {days} days')

    date = input("Enter a date (year month day): ")
    splitted = date.split()

    year = int(splitted[0])
    month = splitted[1].lower()
    day = int(splitted[2])

    func = day_of_year(year, month, day)
    print(f'{date} is the {func}th day of the year')

def second_task():
    """
    This function analyzes a user-provided sentence and counts how many characters
    are letters, digits, and other types.
    """

    sentence = input("Enter here the sentence that you would like to analyze: ")
    results = {
        'letter': 0,
        'digit': 0,
        'etc': 0
    }

    for i in sentence:
        if i.isalpha():
            results['letter'] += 1
        if i.isdigit():
            results['digit'] += 1
        else:
            results['etc'] += 1

    print(results)


def third_task():
    """
    Takes a string of course codes as input and categorizes them by subject group.
    Courses starting with 'I' are classified as Informatics, 'M' as Mathematics, and 'X' as Electives.
    """

    iput = input("Please enter the string that you would like to analyze: ").split(';')
    dic = {}

    dic["info"] = ""
    dic["math"] = ""
    dic["elect"] = ""
    for course in iput:
        if course.startswith("I".upper()):
            dic["info"] += course
        elif course.startswith("M".upper()):
            dic["math"] += course
        elif course.startswith("X".upper()):
            dic["elect"] += course
        else:
            print("Invalid input")
    print(dic)


def forth_task():
    """
    Analyzes a dictionary of filenames provided by the user
    and counts how many files have specific extensions: .py, .java, and .mp4.
    """

    stat = input('Enter the dictionary here, that you would like to analyze: ').split(',')
    file_list = {'py' : 0, 'java': 0, 'mp4': 0}

    for file in stat:
        file = file.strip(" '\"") # it removes quotation marks and spaces.
        if '.' in file:
            extension = file.rsplit('.', 1)[-1].lower()
            if extension in file_list:
                file_list[extension] += 1
            else:
                continue
    print(file_list)