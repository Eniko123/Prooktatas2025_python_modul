import random
def first_task():
    """
    This function creates a random list of 42 numbers.
    It multiplies every even number by 3, divides every odd number by 5,
    and skips every fifth element in the original list.
    """

    print("This function creates a random list of 42 numbers. \nIt multiplies every even number by 3, divides every odd number by 5, \nand skips every fifth element in the original list. \n ")

    data = [
        x * 3 if x % 2 == 0 else x // 5
        for i, x in enumerate([random.randint(1,100) for _ in range(42)])
        if (i+1) % 5 != 0
    ]
    print(data)

    data.insert(1, int((input("\nPlease enter a two digit number, that I will put to the second index: "))))
    print(data)

    data.remove(int(input("\nPlease enter which number you would like to delete: ")))
    print(data)

    data.sort()
    print(f'\nThe list in an ordered form: \n{data}')

    data.reverse()
    print(f'The list in a reverse order form: \n{data}')


import random
#### These are the helper functions for the second task ####
def delete(students):
    for i, student in enumerate(students):
        print(f"{i}. {student}")

    deletable = int(input('Which element would you like to delete from the list'))

    answer = input("Are you sure you want to delete this element? Y/N")

    if answer.upper() == 'N':
        print('Redirecting to starter page')
    else:
        del students[deletable]

def modify(students):
    for i, student in enumerate(students):
        print(f"{i}. {student}")

    name = input("Please enter the name of the person whose data you would like to modify: ")
    name_age_class = input("Please enter which data you would like to modify: nev/eletkor/osztaly")

    for student in students:
        if student["nev"] == name:
            if name_age_class == "nev":
                name_modify = input("What would you like to change the name to?")
                student["nev"] = name_modify
            elif name_age_class == "eletkor":
                age_modify = int(input("What would you like to change the age to?"))
                student["eletkor"] = age_modify
            elif name_age_class == "osztaly":
                class_modify = input("What would you like to change the class to?")
                student["osztaly"] = class_modify
            else:
                print("Invalid field selected.")

    print("Modification complete.")

def append(students, classes):
    name = input("Please enter the Student's name:")
    age = int(input("Please enter the Student's age!"))
    clas = random.choice(classes)

    students.append({"nev": name, "eletkor": age, "osztaly": clas})

    print("New student was added.")
##############################################################

def second_task():
    """
    This function manages a student list using a menu system.
    Allows adding, deleting, and modifying student records.
    """

    students = [{"nev": "Teszt Elek", "osztaly": "13I", "eletkor": 19}, {"nev": "Kiss Béla", "osztaly": "12A",
                                                                        "eletkor": 18},
               {"nev": "Nagy Anna", "osztaly": "11B", "eletkor": 17}, {"nev": "Szabó Gergő", "osztaly": "10C",
                                                                       "eletkor": 16},
               {"nev": "Varga László", "osztaly": "9D", "eletkor": 15}, {"nev": "Tóth Zsófia", "osztaly": "12A",
                                                                         "eletkor": 18}]

    classes = ["9A", "10B", "11C", "12D", "13I"]

    print("A jelenlegi tagok:")
    for i, c in enumerate(students, start=1):
        print(f"{i}. {c['nev']} {c['eletkor']} éves és a {c['osztaly']} osztályba jár.")

    while True:
        iput = input("Welcome in the program! \nThis program contains a dictionary that you can edit :) \n New student – newmem | Delete – delete | Modify – modify | Exit – end, Q, quit \n What would you like to do next?")

        if iput.lower() in ["q", "quit", "end"]:
            print("A program leáll")
            break
        elif iput == "newmem":
            append(students, classes)
            print("A jelenlegi tagok:")
            for i, c in enumerate(students, start=1):
                print(f"{i}. {c['nev']} {c['eletkor']} éves és a {c['osztaly']} osztályba jár.")
        elif iput == "delete":
            delete(students)
            print("A jelenlegi tagok:")
            for i, c in enumerate(students, start=1):
                print(f"{i}. {c['nev']} {c['eletkor']} éves és a {c['osztaly']} osztályba jár.")
        elif iput == "modify":
            modify(students)
            print("A jelenlegi tagok:")
            for i, c in enumerate(students, start=1):
                print(f"{i}. {c['nev']} {c['eletkor']} éves és a {c['osztaly']} osztályba jár.")
        else:
            print("Invalid input")



