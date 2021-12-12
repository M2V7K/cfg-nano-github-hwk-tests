# overriding

#inheritence/polymorphorism

#inheritance
class Car:
    def __init__(self, distance, speed):
        self.distance = distance
        self.speed = speed

    def calc_time(self):
        time = self.distance / self.speed
        return time

# car1 = Car(40, 20)
# print(car1.speed)
# print(car1.distance)
# print(car1.calc_time())

class SportsCar(Car): # inheritance
    def __init__(self, distance, speed):
        self.distance = distance
        self.speed = speed
        Car.__init__(self, self.distance, self.speed) #lets you access all the methods and parameters in the parent class # inherit

    def accelerate(self):
        self.speed *= 2

    def calc_time(self): #to show polymorphorism - already have a method that has the same name as a parent will override it
        time = self.distance / self.speed
        return time + 1

# sportsCar1 = SportsCar(50, 60)
#
# print(sportsCar1.calc_time())
#
# sportsCar1.accelerate()
#
# print(sportsCar1.calc_time())



# overloading
class Student:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def multiply(self, a=None, b=None, c=None): #example of overloading parameters so the function can take into account up to 3
        m = 0

        if a is not None and b is not None and c is not None:
            m = a*b*c
        elif a is not None and b is not None:
            m = a*b
        else:
            m = a

        return m

s1 = Student(78, 91)
print(s1.multiply(2,6))

# inheritance

class Clothes:

    def __init__(self):
        print("Class is initiated")

    def phrase(self):
        print("I am clothes")

class Dress(Clothes): # inherit

    def __init__(self):
        Clothes.__init__(self) # inherit

    def dress1(self):
        print("I am a dress")

# clothes1 = Dress()
# clothes1.phrase()
# clothes1.dress1()





#top three funniest people

employee_names = {}
#each class/instance is an employee so we don't need to have a dictionary with the employee name and their values

class Employee:
    def __init__(self, employee_name):
        employee_names[employee_name] = 0 #votes
        self.voted = False
        self.name = employee_name
        self.nominated = ""

    def vote(self, employee_vote):
        # check if that person has voted or not
        if not self.voted: #(not self.voted) = true
            if employee_vote in employee_names:
                if employee_vote is not self.name:
                    employee_names[employee_vote] += 1
                    self.nominated = employee_vote
                    self.voted = True
                else:
                    print("You can not vote for yourself, please vote for someone else.")
            else:
                print("This person is not in the office please choose someone else.")

    def remove_votes(self):
        if self.voted:
            employee_names[self.nominated] -= 1
            self.voted = False
            print(f'{self.nominated} has {employee_names[self.nominated]} votes.')
            self.nominated = ""


def funniest():
    winner = max(employee_names.values())
    winners = []
    for k,v in employee_names.items():
        if v == winner:
            winners.append(k)
    return winners



# Michael = Employee("Michael")
# Sareena = Employee("Sareena")
# Arooza = Employee("Arooza")
#
#
# Michael.vote("Sareena")
# Arooza.vote("Sareena")
# Sareena.vote("Arooza")
# Michael.remove_votes()
#
#
# print(funniest())

# reduced function with lambda

from functools import reduce

def combine_digits(x,y):
    return (x*10) + y

def digits_to_num(digits):
    return reduce(combine_digits, digits)

print(digits_to_num([3,4,3,2,1]))

digits_to_num([3,4,3,2,1])

li1 = [7,4,8,11,33,55,2]
sum = reduce((lambda x, y: x+y), li1)
print(sum)

# merge sort

def merge_sort(array, left, right):
    if left == right: #keep dividing the array by 2 until it reaches it's single elements -> do the left side first -> then followed by the right side
        return array
    middle = int((left+right)/2)
    array = merge_sort(array, left, middle) #checking left branch
    array = merge_sort(array, middle+1, right) #checking right branch
    return merge(array, left, middle, right)


def merge(array, left, middle, right): #merging the elements
    sorted_list = []
    left_list = array[left:middle+1] #up to not including middle+1
    right_list = array[middle+1:right+1] #up to nit including right+1
    i = 0
    j = 0
    while j < len(right_list) and i < len(left_list):
        if(left_list[i] > right_list[j]):
            sorted_list.append(right_list[j])
            j += 1 #pointer is at the end added all items
        else:
            sorted_list.append(left_list[i])
            i += 1

    while i < len(left_list):   #appending left and right list to the sorted_list
        sorted_list.append(left_list[i])
        i += 1

    while j < len(right_list):
        sorted_list.append(right_list[j])
        j += 1

    for k in range(len(sorted_list)): #changing original unsorted array to copy the sorted array
        array[left+k] = sorted_list[k]
    return array

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)

merge_sort([8,1,3,6,2,9], 0, 6 )

#iterator
myVeg = ("carrot", "celery", "raddish")
it1 = iter(myVeg)

print(next(it1))
print(next(it1))
print(next(it1))

# generators

# def generate(n): #10
#     result = []
#     for i in range(n):
#         result.append(i*2)
#     return result
#
# for i in generate(10):
#     print(i)

def generate2(n): #10
    for i in range(n):
        yield i*2 #yield is what makes it a generator

x = generate2(3)

# decorators?

def new_decorator(func):  #main decorator func
    def wrap_func():      #wrapping func
        print("Start up the function")
        func()
        print("End of the function")

    return wrap_func  #return the wrap func

@new_decorator #func you want to decorate it with -> can comment out the @ if don't want a decorator
def normal_func():
    print("I am a normal function")

normal_func()

# decorator_func = new_decorator(normal_func)
# decorator_func()

def new_decorator1(func):
    def wrap_func(num1, num2):
        if num2 == 0:
            return func(num1)
        else:
            return [i for i in range(1, num1*2, 2)]
    return wrap_func

@new_decorator1
def num_list(num):
    return [i for i in range(0, num*2, 2)] #try and make it  simple by removing value and using range to it's full capacity range(start_value, end_value, interval)

print(num_list(5,1)) #once added the decorator the parameters of the core function become the parameters of the wrap function

import abc

#abstract classes let the user use what you built without letting the user know how you did it
class Shape1(object):
    __metaclass__ = abc.ABCMeta #a variable that is set -> the user will know what the developer but not how they do it

    @abc.abstractmethod
    def calc_perimeter(self, input):
        print("no perim")
        return


class rectangle1(Shape1):

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def calc_perimeter(self):
        perim = self.a + self.b + self.c + self.d
        print("The perimeter of the rectangle is: ", perim)
        return perim

# r1 = Rectangle1(1,2,4)
# r1.calc_perimeter()
