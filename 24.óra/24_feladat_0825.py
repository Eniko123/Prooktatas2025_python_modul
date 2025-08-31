class BuiltInFunctions:
    def __init__(self):
        self.list = [4, 5, 8, 2, 9]

    def abs_func(self):
        abs_list = [abs(number) for number in self.list]
        print(abs_list)

    def sum_func(self):
        print(sum(self.list))

    def minmax_func(self):
        print(min(self.list))
        print(max(self.list))

    def round_func(self):
        print(f'The rounded mean of the list is {round(sum(self.list)/len(self.list),2)}')

    def pow_func(self):
        sq_list = [pow(number, 2) for number in self.list]
        print(sq_list)

    def all_func(self):
        if all(number > 3 for number in self.list):
            print("True")
        else:
            print("False")

    def any_func(self):
        if any(number > 3 for number in self.list):
            print("True")
        else:
            print("False")

    def sorted_func(self):
        print(sorted(self.list))

    def len_func(self):
        print(len(self.list))

    def type_func(self):
        type_list = [type(number) for number in self.list]
        print(type_list)