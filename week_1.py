"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""

class CashRegister:

    def __init__(self):

        self.total_items = dict() #None # {'item': 'price'}
        self.total_price = 0
        self.discount = 0 #in terms of percent

    def add_item(self, item, price):
        self.total_items[item] = price

    def remove_item(self, item):
        self.total_items.pop(item)
        return self.total_items

    def apply_discount(self, discount, item): #applied discount to the items
        discount_item = int(self.total_items[item] * ((100-discount)/100))
        self.total_items[item] = discount_item
        self.show_items()

    def get_total(self): #add all the values in the dictionary to get a total
        self.total_price = sum(self.total_items.values())
        print(f'The total of your receipt is £{self.total_price}.')

    def show_items(self): #print all the items in the dictionary
        for key, values in self.total_items.items():
            print(key, values)

    def reset_register(self): #reset the register means reset the total_price to 0
        self.total_items = {}  # None # {'item': 'price'}
        self.total_price = 0
        self.discount = 0
        print(f'The total items are: {self.total_items}\nThe total_price is: {self.total_price}\nThe discount is: {self.discount}')

    def calc_loyalty_points(self): #work out loyalty points
        loyalty_points = round(self.total_price / 5)
        return loyalty_points

    def show_loyalty_points(self): #print loyalty points
        loyalty_points1 = self.calc_loyalty_points()
        print(f'The number of loyalty points you have are: {loyalty_points1}')

    def calc_loyalty_discount(self): #calc prices using loyalty points
        discount_price = round(self.total_price - (self.calc_loyalty_points() * 0.2))
        print(f'The discount price using loyalty points is: £{discount_price}')

# cr = CashRegister()
# cr.add_item("t-shirt", 5)
# cr.add_item("shoes", 10)
# cr.add_item("socks", 15)
# cr.show_items()
# print("\n")
# cr.remove_item("t-shirt")
# cr.show_items()
# print("\n")
# cr.apply_discount(20, "socks")
# print("\n")
# cr.get_total()
# print("\n")
# cr.show_loyalty_points()
# print("\n")
# cr.calc_loyalty_discount()
# print("\n")
# cr.reset_register()


# EXAMPLE code run:

# ADD


"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict() #{} #subject:grade

class CFGStudent(Student):

    def __init__(self, name, age, id, specialisation, attendance): #specialisation
        self.name = name
        self.age = age
        self.id = id
        self.specialisation = specialisation
        self.attendance = attendance
        Student.__init__(self, self.name, self.age, self.id) #only the attributes from above

    def add_subject(self, subject, grade):
        self.subjects[subject] = grade
        return self.subjects

    def remove_subject(self, subject):
        self.subjects.pop(subject)
        return self.subjects

    def show_items(self): #show all the subjects and grades
        for grades, subjects in self.subjects.items():
            print(grades, subjects)

    def show_subjects(self): #show subjects only
        for subjects in self.subjects.keys():
            print(subjects)

    def calculate_grade(self): #calculate average grades
        overall_grade = sum(self.subjects.values())
        average_grade = round(overall_grade / len(self.subjects))
        if average_grade > 70:
            print(f'Congratulations you have achieved {average_grade} are a first class student!')
        elif (average_grade > 60) and (average_grade < 71):
            print(f'Fantastic you scored {average_grade} and achieved a 2:1!')
        elif (average_grade > 50) and (average_grade < 61):
            print(f'Well done you scored {average_grade} and achieved a 2:2!')
        elif (average_grade > 40) and (average_grade < 51):
            print(f'Good you you scored {average_grade} and passed!')
        else:
            print(f'Unfortunately you scored {average_grade} and failed :(')

    def __str__(self): #use with print function
        return f'Their name is: {self.name}\nTheir age is: {self.age} years\nTheir student id is: {self.id}\nTheir specialisation chosen: {self.specialisation}\nTheir attendance is: {self.attendance}%'

# student1 = CFGStudent("Vani", 26, 78, "Data Engineering", 70)
# print(student1)
# print("\n")
# print(student1.specialisation)
# print("\n")
# student1.add_subject("Statistics", 40)
# student1.add_subject("Visualization", 50)
# student1.add_subject("Deep Learning", 60)
# student1.add_subject("Machine Learning", 70)
# student1.add_subject("Data Analysis", 80)
# student1.show_items()
# print("\n")
# student1.remove_subject("Data Analysis")
# student1.show_subjects()
# print("\n")
# student1.calculate_grade()

# student2 = CFGStudent("Riri", 25, 58, "Software Engineering", 90)
# print(student2)
# print("\n")
# print(student2.specialisation)
# print("\n")
# student2.add_subject("Computer Architecture", 70)
# student2.add_subject("Data Structures", 30)
# student2.add_subject("Algorithms", 90)
# student2.add_subject("Operating systems", 65)
# student2.add_subject("Coding", 44)
# student2.show_items()
# print("\n")
# student2.remove_subject("Data Structures")
# print("\n")
# student2.show_subjects()
# print("\n")
# student2.calculate_grade()


