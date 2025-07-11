import random
def elso_feladat():
    """
    This quiz tests your knowledge of historical terms by asking for their definitions.
    Type 'q', 'end', or 'quit' to exit the game.
    """

    term = ['majorság', 'hűbéres', 'jobbágy', 'nemes', 'tized', 'kilenced', 'robot', 'szügyhám', 'vetésforgó', 'ugar', 'lovag']
    definition = ['Egy-egy nagybirtok vagy valamely részének igazgatási központja.', 'Aki örökletes használatra megkapja a földet.', 'Telkes paraszt, aki a földesúrtól kapott földön gazdálkodik.', 'Kiváltságos réteg.', 'Egyházi adó.', 'Földesúrnak beszolgáltatott adó.', 'Ötvenkét igás, vagy 104 kézimunka nap kötelezettség.', 'Igavonási találmány, melynek köszönhetően nem az állat nyakában van a húzó eszköz.', 'A termőföld használata évszakonként más és más.', 'Művelés alá nem vont terület.', 'Vagyonos katonai szolgálattevő lóval, páncéllal.']

    dictionary = dict(zip(term, definition))
    print(dictionary)

    copy = dict(zip(term, definition))
    key = random.choice(list(copy))
    answer = input(f'Mi a {key} meghatározása?')
    while answer.lower() not in ['q', 'end', 'quit']:
        if answer.strip().lower() == copy[key].strip().lower():
            print("Helyes válasz! Csak így tovább :)")
            del copy[key]
            key = random.choice(list(copy))
            answer = input(f'Mi a {key} meghatározása?')
        else:
            print("Most nem sikerült, a helyes válasz: ")
            print(copy[key])
            key = random.choice(list(copy))
            valasz = input(f'Mi a {key} meghatározása?')


def masodik_feladat():
    """
    This program determines the class of an IP address.
    It prompts the user for an IP address and prints whether it belongs to class A, B, C, D, or E.
    """

    ranges = [(1, 126), (128, 191), (192, 223), (224, 239), (240, 255)] #Így megfelelő a formátum ha ez egy intervallum?
    descriptions = ["Nagy hálózatok", "Közepes hálózatok", "Kis hálózatok", "Multicast", "Kísérleti címek"]
    class_labels = ["A", "B", "C", "D", "E"]

    ip_classes = dict(zip(class_labels, zip(ranges, descriptions)))

    iput = input("Add meg az IP címet amit vizsgálni szeretnél (X.X.X.X/X formátumban): ")
    first_section = int(iput.split('.')[0])

    if 1 <= first_section <= 126:
        print('A megadott email cím osztálya: A')
    elif 127 <= first_section <= 191:
        print('A megadott email cím osztálya: B')
    elif 192 <= first_section <= 223:
        print('A megadott email cím osztálya: C')
    elif 224 <= first_section <= 239:
        print('A megadott email cím osztálya: D')
    elif 240 <= first_section <= 255:
        print('A megadott email cím osztálya: E')
    else:
        print("Helytelen IP cím!")




##### Ezek a harmadik feladata segíd függvényei ####
def list_compression():
    """
    This function creates multiple lists from a string.
    """
    data_list_string_format = "Németh Kamilla; 19; Debrecen; Fekete Géza; 18; Pécs; Kovács Péter; 27; Budapest; Kiss Tibor; 20; Debrecen; Szabó Erzsébet; 21; Budapest; Szilágyi Ede; 18; Pécs; Agárdi Pál; 26; Budapest; Pálosi Richárd; 23; Budapest; Budai Máté; 19; Debrecen; Karácsony Antal; 20; Budapest; Aradi Márta; 27; Pécs; Piros Adél; 29; Debrecen; Bíró Zsolt; 16; Budapest; Szabados Attila; 25; Debrecen; Román Sarolta; 24; Budapest; Virág Bertalan; 22; Pécs; Varga Imre; 18; Budapest; Tóth Sándor; 22; Debrecen; Nagy Ibolya; 23; Pécs; Horváth Ferenc; 17; Budapest; Balogh Edina; 26; Budapest"
    data_list = data_list_string_format.split(';')
    global name, age, city
    name = []
    age = []
    city = []
    list_format = [data.strip() for data in data_list]
    for i in list_format:
        if i in ["Debrecen", "Pécs", "Budapest"]:
            city.append(i)
        elif i.isdigit():
            age.append(i)
        else:
            name.append(i)
    print(
        name, age, city
    )

def list_to_dict():
    """
    This function takes lists as input and converts them into a dictionary.
    """
    global data
    data = [
        {'name': name[i], 'age': int(age[i]), 'city': city[i]}
        for i in range(len(name))
    ]
    print(data)

def custom_print(name=True, age=True, city=True):
    """
    This function prints your dictionary of names, ages, and cities as desired.
    """
    for person in data:
        output =[]
        if name == True:
            output.append(f"Név: {person['name']},")
        if age == True:
            output.append(f"Kor: {person['age']}, ")
        if city == True:
            output.append(f"Város: {person['city']}")
        print(output)

def order_by_age():
    """
    This function sorts your dictionary into age groups.
    """

    age_dic = {"12-20": [], "21-25": [], "26-32": [], "33+": []}
    for i in data:
        age = i['age']
        if 12 <= age <= 20:
            age_dic["12-20"].append(i['name'])
        elif 21 <= age <= 25:
            age_dic["21-25"].append(i['name'])
        elif 26 <= age <= 32:
            age_dic["26-32"].append(i['name'])
        else:
            age_dic["33+"].append(i["name"])
    print(age_dic)

def most_frequent_city():
    """
    This function shows which city appears most frequently in your dictionary.
    """

    citys = ["Budapest", "Pécs", "Debrecen"]
    counter = [0] * 3

    for c in data:
        city = c['city']
        index = citys.index(city)  # Megkeressük, hányadik a város a listában
        counter[index] += 1

    max_index = counter.index(max(counter))
    most_frequent_city = citys[max_index]
    print(f"Az szótárból a legtöbben {most_frequent_city}-en élnek")

def age_mean():
    """
    This function calculates the mean age of the people in the list.
    """
    ages = [person['age'] for person in data]
    age_mean = sum(ages) / len(ages)
    print(f'Az átlag életkor a szótárban:{age_mean:.2f}')

def same_city():
    """
    This function shows which people live in the same cities from your dictionary.
    """
    city_dic = {"Budapest": [], "Pécs": [], "Debrecen": []}

    for c in data:
        city = c['city']
        name = c['name']  # vagy ha kulcsot váltasz: c['nev']
        parts = name.split()
        if len(parts) >= 2:
            first_name = parts[0]
            first_letter = parts[1][0]
            short_name = f"{first_name} {first_letter}."

        if city == "Budapest":
            city_dic["Budapest"].append(short_name)
        elif city == "Pécs":
            city_dic["Pécs"].append(short_name)
        else:
            city_dic["Debrecen"].append(short_name)

    print(f"{city}-en élők: {city_dic}")
###################################################

def harmadik_feladat():
    list_compression()
    list_to_dict()
    custom_print(name=True, age=True, city=True)
    order_by_age()
    most_frequent_city()
    age_mean()
    same_city()




    







