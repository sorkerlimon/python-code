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
