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

