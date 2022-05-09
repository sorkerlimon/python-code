##### Function  start

# def greet():
#     print("Hi there")
#     print("Hi there... I am limon")
#     print("Hi there & I am sorker ")
#
# greet()



################# function with formate account
# def greet(name):
#     print(f"Hi there {name}")
#     print(f"Hi there... I am limon {name}")
#     print(f"Hi there & I am sorker {name}")
#
# greet("Bangladehs")



########### function with arg

# def greet(first_name,last_name):
#     print(f"Hi there {first_name} {last_name}")
#     print(f"Hi there... {first_name} {last_name}")
#     print(f"Hi there & I am {first_name} {last_name}")
# try:
#     greet("Bangladehs", "lizel")
# except TypeError as tp:
#     print(tp ,"Missing 1 argument")
# else:
#     print("Keep Going......................")



######### Function 2 type 1(Perform a task ) 2(return a value)

# def get_greet(name):
#     return f"hello {name}"
#
# messege = get_greet("Limon")
# print(messege)
#
# file = open("content.txt","w")
# file.write(messege)
# print("messege write done")
#
# with open("C:/Users/Sorker Limon/Desktop/cont.txt") as f:
#     contents = f.read()
#     print(contents)




####### Keyword Arguments

# def increment(number ,by):
#     return number + by
#
# result = increment(2 , 1)
# print(result)
#
# def increment(number ,by=2):
#     return number + by
#
# result = increment(2)
# print("Pass Argument : ",result)




########## xarg argumnet

# def multiply(x,y):
#     return x * y
#
# result = multiply(2,3)
# print(result)



# def multiply(*numbres):
#     total = 1
#     for number in numbres:
#         total  = total * number
#     return total
#
# result = multiply(2,3,5,4,3,)
# print(result)




#################### ** arg  function   (amra key:value pear hiseba patha te pari)


# def save_user(**user):
#     print(user)
#
# save_user(id=1,name="Limon",year=1998)






############# Scope Function

# m = "b"
#
# def greet(name):
#     global m
#     m = "d"
#
# print(m)




########## FIzz Buzz problem solution

# def fizzBuzz(input):
#     if(input % 3 == 0) & (input % 5 == 0):
#         return "FizzBuzz"
#     elif input % 3 == 0:
#         return "Fizz"
#     elif input % 5 == 0:
#         return "Buzz"
#     return input
#
# result = fizzBuzz(1.5)
# print(result,"It's not divisiable")

