try:
    age = int(input("Age : "))
    print(age)
except ValueError as ex:
    print("Type valid data")
    print(ex)
    print(type(ex))
else:
    print("No exception thrown")
print("Execution Continuoues >......!!!")