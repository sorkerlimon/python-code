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


