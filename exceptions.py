# try:
#     age = int(input("Age : "))
#     print(age)
# except ValueError as ex:
#     print("Type valid data")
#     print(ex)
#     print(type(ex))
# else:
#     print("No exception thrown")
# print("Execution Continuoues >......!!!")



######## Zero division error

# try:
#     age = int(input("enter ur age"))
#     xfactor = 10 /age
# except ZeroDivisionError as zero:
#     print("You can not divided age ")
# else:
#     print(xfactor)





########## Cleaning Up code file open and close

# try:
#     file = open("app.py")
#     age = int(input("enter ur age"))
#     xfactor = 10 /age
# except (ValueError,ZeroDivisionError) as ex:
#     print(ex)
# else:
#     print(xfactor)
#
# finally:
#     file.close()



#######   With state ment  exception handaling


# try:
#  with open("machinelearning.py") as file:
#   print("File opened")
#
# except (ValueError,ZeroDivisionError) as ex:
#  print(ex)
# else:
#  print("NO excepiton")

########### Rais Exception

# def xfactot(age):
#  if age <= 0 :
#   raise ValueError("Age can'nt be les or 0")
#  return 10/age
#
#
# try:
#  xfactot(-1)
# except ValueError as value:
#  print(value)



###### Cost of rising exception
# from timeit import timeit
#
# code1= """
# def xfactot(age):
#  if age <= 0 :
#   raise ValueError("Age can'nt be les or 0")
#  return 10/age
#
#
# try:
#  xfactot(-1)
# except ValueError as value:
#  pass
#  """
#
# print("Add",timeit(code1,number=1000))
