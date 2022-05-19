# class Point:
#     def draw(self):
#         print("draw")
#
# point = Point()
# point.draw()
#
# print(isinstance(point,Point))


#
# class Point:
#     def draw(self):
#         print("Draw a python code !!!")
#
#     def art(self):
#         print("Art function called..!!!")
# point = Point()
# point.draw()
# point.art()


# class Person:
#     def st_behaviour(self):
#         print("Age 22")
#         print("Name : Limon")
#         print("Colur : Dark & white")
#
#     def second_behaviour(self):
#         print("Age 22")
#         print("Name : Nawshin")
#         print("Colur :  white")
#
#
# person = Person()
# person.st_behaviour()
# person.second_behaviour()



# class Person:
#     def st_behaviour(self, age, name, colur):
#         print(f"Age {age}")
#         print(f"Name : {name}")
#         print(f"Colur : {colur}")
#
#     def university(self, u_name,id, batch,):
#         print(f"University name {u_name}")
#         print(f"Student ID {id}")
#         print(f"Batch {batch}")
#
#
# person1 = Person()
# person1.st_behaviour(12,"Limon","Black & white")
# person1.university("World university of Bangladesh",2749,"43/A")
#
# person2 = Person()
# person2.st_behaviour(13,"nawshin","white")
# person2.university("World university of Bangladesh",2745,"43/A")

################# Constructor


# class Addition:
#     first = 0
#     second = 0
#     answer = 0
#
#     # parameterized constructor
#     def __init__(self, f, s):
#         self.first = f
#         self.second = s
#
#     def display(self):
#         print("First number = " + str(self.first))
#         print("Second number = " + str(self.second))
#         print("Addition of two numbers = " + str(self.answer))
#
#     def calculate(self):
#         self.answer = self.first + self.second
#
#
# # creating object of the class
# # this will invoke parameterized constructor
# obj = Addition(1000, 2000)
#
# # perform Addition
# obj.calculate()
#
# # display result
# obj.display()


# class Point:
#     def __init__(self, x, y):
#         self.first = x
#         self.second = y
#
#     def draw(self):
#         print("draw ",self.first,self.second)
#
# obj = Point(1000,2000)
# obj.draw()


# class Person:
#
#     def __init__(self,u_name,name,id,batch,totall_payment, due):
#         self.u_name = u_name
#         self.name = name
#         self.id = id
#         self.batch = batch
#         self.totall_payment = totall_payment
#         self.due = due
#
#     def student_detils(self):
#         print(f"University Name : {self.u_name}")
#         print(f"Student Name : {self.name}")
#         print(f"Student ID : {self.id}")
#         print(f"Student batch : {self.batch}")
#
#
#     def costMaintain(self):
#         self.answer = self.totall_payment - self.due
#         print("toatall main ",self.answer)
#
#
# toatal_amount = int(input("enter your totall amount :"))
# totall_due = int(input("enter your due amount :"))
# obj=Person("World university of Banglades","Limon",2749,"43/A",toatal_amount,totall_due)
# obj.student_detils()
# obj.totall_payment()



# class Sum:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def additon(self):
#         answer = self.x + self.y
#         print(answer)
#
# onj = Sum(12,10)
# onj.additon()



# ########## Class Vs Instance Attribute
#
# class Point:
#     default_colour = "Black"  ########## etar mane hocce sob sobar default bhave ei Attributer ta thakbe
#
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#
#     def draw(self):
#         print(f"point {self.x} {self.y}")
#
#
# point = Point(1,2)
# print(Point.default_colour)
# point.draw()


########## Class Vs Instance Method

# class Point:
#
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     @classmethod ######## eta hocce class level method
#     def zero(cls):
#         try:
#             first = int(input("First intput : "))
#             second = int(input("Second intput : "))
#             return cls(first,second)
#         except ValueError as typeerror:
#             print("Please input your valid Nu2mber ")
#         else:
#             print("Keep going")
#
#     def draw(self):
#         print(f"point {self.x} {self.y}")
#
#
# point = Point.zero()
# point.draw()





############### Magic method

# class Point:
#
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"{self.x} {self.y}"
#
#
#     def draw(self,z):
#         print(f"point {self.x} {self.y} {z}")
#
#
# point = Point(1,2)
# print(point)
# point.draw(4)



######### Comparing obj

# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y
#
#     def __gt__(self, other):
#         return self.x < other.x and self.y < other.y
#
# point = Point(1,2)
# other = Point(6,2)
#
# print(point == other)



########## Making custom container

# class Cloud:
#     def __init__(self):
#         self.tags = {}
#
#     def add(self,tag):
#         self.tags[tag.lower()] = self.tags.get(tag.lower(),0) + 1
#
#
#     def __getitem__(self, tag):
#         return self.tags.get(tag.lower(),0)
#
#     def __setitem__(self, tag, count):
#         self.tags[tag.lower()] = count
#
#     def __len__(self):
#         return len(self.tags)
#
#     def __iter__(self):
#         return iter(self.tags)
#
#
# cloud = Cloud()
# cloud["python"] = 10
# cloud.add("Limon")
# cloud.add("LImon")
# cloud.add("Limon")
# print(cloud.tags)



###################### Inharitence

# class Animal:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#
#     def eat(self):
#         print(f"Eat ... {self.x}")
#
# class Mammal(Animal):
#
#     def walk(self):
#         print("Walk ...",self.y)
#
# class Fish(Animal):
#
#
#     def swim(self):
#         print("Swim ... !",self.y)
#
#
# mammal = Mammal(1,2)
# mammal.walk()
# mammal.eat()
#
#
# fish = Fish(1,2)
# fish.eat()
# fish.swim()




###################### Inheritance with real life example

# class Polygon:
#
#     def __init__(self,sides):
#         self.sides = sides
#
#     def display_info(self):
#         print("A polygon is two diamonsolam shape with straight lines")
#
#     def get_perameter(self):
#         perameter = sum(self.sides)
#         return perameter
#
# class Triangle(Polygon):
#     def display_info(self):
#         print("A triangle is polygon with 3 edges ")
#         Polygon.display_info(self)
#
# class Quadrelatral(Polygon):
#     def display_info(self):
#         print("A triangle is polygon with 4 edges ")
#         super().display_info()
#
#
# t = Triangle([2,3,4])
# t.display_info()
# peramemter1 = t.get_perameter()
# print("sum of the triangle :",peramemter1)
#
# t1 = Quadrelatral([2,3,4,5])
# t1.display_info()
# peramemter1 = t.get_perameter()
# print("sum of the Quadrelatral :",peramemter1)



######## Method overridding

# class Animal:
#     def __init__(self):
#         self.age = 1
#
#     def eat(self):
#         print("Eat")
#
#
# class Mamal(Animal):
#
#     def __init__(self):
#         self.weight = 2
#         super(Mamal, self).__init__()
#         # super().__init__()
#
#     def walk(self):
#         print("Walk")
#
#
# m = Mamal()
# print(m.age)
# print(m.weight)


######## Multii level inheritence   (It's bad practice alwys try to use multilevel inheritence )


# class Animal:
#     def eat(self):
#         print("Eat")
# class Bird(Animal):
#     def fly(self):
#         print("fly")



# ############### Multiple inheritance
# class Employee:
#     def greet(self):
#         print("Employee Greet ")
# class Person:
#     def greet(self):
#         print("person  Greet ")
#
# class Manager(Employee,Person):
#     pass




####################  Inheritance example

# class InvalidOperator(Exception):
#     pass
#
# class Stream:
#     def __init__(self):
#         self.opened = False
#
#     def open(self):
#         if self.opened:
#             raise InvalidOperator("Stream is already opened")
#         self.opened = True
#
#
#     def close(self):
#         if self.closed:
#             raise InvalidOperator("Stream is already closed")
#         self.closed = False
#
#
# class FileStram(Stream):
#     def read(self):
#         print("Reading data from a file ")
#
#
# class NetStrem(Stream):
#     def read(self):
#         print("Reading data from a Network ")
#
# netStrem = NetStrem()
# netStrem.opened
# netStrem.read()




############ Abstract Base classes class hocce amon ekta method je ta declear kore dile base classs e  seta protita class e use kora lagbe child class e
# from abc import ABC,abstractmethod
#
# class InvalidOperator(Exception):
#     pass
#
# class Stream(ABC):
#     def __init__(self):
#         self.opened = False
#
#     def open(self):
#         if self.opened:
#             raise InvalidOperator("Stream is already opened")
#         self.opened = True
#
#
#     def close(self):
#         if self.closed:
#             raise InvalidOperator("Stream is already closed")
#         self.closed = False
#
#     @abstractmethod
#     def read(self):
#         pass
#
#
# class FileStram(Stream):
#     def read(self):
#         print("Reading data from a file ")
#
#
# class NetStrem(Stream):
#     def read(self):
#         print("Reading data from a Network ")
#
# class MemoryStream(Stream):
#     def read(self):
#         print("memory stream are reading")
#
# memory = MemoryStream()
# memory.read()


 ##################### Polymorphisom
# Polymorphsiom   e and etar mane ee hoce onk gula form ek sahte  )
# from abc import ABC,abstractmethod
# class UIcontorl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass
#
# class TextBox(UIcontorl):
#     def draw(self):
#         print("Test box")
#
# class DropDownList(UIcontorl):
#     def draw(self):
#         print("Drop Down List..")
#     def art(self):
#         print("Art Down List..")
#
# class Art(UIcontorl):
#     def art(self):
#         print("Drop Down List..")
#     def draw(self):
#         print("art class..")
#
# def draw(controls):
#     for control in controls:
#         control.draw()
#
# ddl = DropDownList()
# ddl.art()
# textbox = TextBox()
# art  = Art()
#
# draw([ddl,textbox,art])




#############################  Buit in class


# class Text(str):
#     def duplicate(self):
#         return self + self
#
# text = Text("PgdsfgYYYGD")
# print(text.lower())



####### CLass name tupple
from collections import namedtuple
Point = namedtuple("Point",["x","y"])
p1 = Point(1,2)
p2 = Point(1,2)
print(p1)
print(p2)