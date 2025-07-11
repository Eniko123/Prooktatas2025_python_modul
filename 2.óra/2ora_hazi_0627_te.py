def vowel_counter():
    """
    This function counts how many vowel a sentence has.
    """

    iput = "Hello vilag!"
    oput = ""
    vowel = "A, a, E, e, I, i, O, Ö, ö. U, u, Ü, ü"

    for i in iput:
        if i in vowel:
            oput +=i
        else:
            continue

    print(len(oput))



def sum_of_digits():
    """
    This function adds up digits of a number.
    """

    number = "753"
    sum = 0

    for i in str(number):
        sum += int(i)

    print(sum)



def sentence_backwards():
    """"
    This function reverses the order of words in a sentence.
    """

    sentence = "Szeretem a Python nyelvet"
    word = sentence.split()
    word.reverse()

    print(word)



def most_frequent_number():
    """
    This function gives you the most frequent number from a list of numbers.
    """

    point = []
    iput = input("Result? ")

    while iput != "":
        point.append(int(iput))
        iput =input("Results?")

    counts = []

    for i in range(0, 11):
        item = 0
        for c in point:
            if c == i:
                item +=1
        counts.append(item)

    most = max(counts)
    most_frequent = counts.index(most)

    print(f'A leggyakoribb szám {most_frequent} ({most} db)')



def password_check():
    """
    This function checks whether your password is strong enough.
    """

    password = "eL0F3y43"

    if len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isupper() for c in password) and any(c.islower() for c in password):
        print("A jelszó megfelelő")
    else:
        print("A jelszó hibás")



