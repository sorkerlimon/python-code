#############list start

# letters = ["a","b","c"]
# print(letters)
# matrix = [[1,2],[3,4]]
# print(matrix)
#
# zeros = [0] * 10
# print(zeros)
# zeros = 0 * 10
# print(zeros)
#
# zeros = [0] * 5
# combined = zeros + letters
# print(combined)
#
#
# number = list(range(20))
# print(number)
#
#
# chars = list("hello world")
# print(chars)
# print(len(chars))


# letters = ["r","g","v"]
# print(letters)
# matrix = [[1,2],[3,4]]
# print(matrix)
#
# zeros = [1] * 5
# print(
#     zeros
# )
#
#
# combined = letters + zeros
# print(combined)
# print(len(combined))
#
# number = list(range(10))
# print(number)

######### List item acces

# letters = ["r","g","v","f","g","g"]
# print(letters[0:2])
# letters[1]="B"
# print(letters)
# print(letters[::2])
#
# number = list(range(20))
# print(number[::2])


###### unpacking method

# numbers = [1,2,3,4,5,6,7,8,9]
# first, second,*all ,last= numbers
#
# print(first)
# print(second)
# print(all)
# print(last)

## Looping over the lisit

# letters = ["a","b","c"]

# letter = [letter for letter in enumerate(letters)]
# print(letter)

# for letter in enumerate(letters):
#     print(letter)
#
# for index ,letter in enumerate(letters):
#     print(index,letter)
#
# for index, letter in enumerate(letters):
#     print(f"Index number is :{index} & {letter} this is the letter")

####### list  adding and remove

letters = ["a","b","c"]
letters.append("d")
print(letters)
letters.insert(0,"Limon")
print(letters)
letters.pop()
print(letters)
letters.pop(1)
print(letters)
letters.remove("b")
print(letters)


