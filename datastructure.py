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

# for index,letter in enumerate(letters):
#     print(index ,letter)
#
# index  = [index  for index ,letter in enumerate(letters)]
# print(index)


####### list  adding and remove

# letters = ["a","b","c"]
# letters.append("d")
# print(letters)
# letters.insert(0,"Limon")
# print(letters)
# letters.pop()
# print(letters)
# letters.pop(1)
# print(letters)
# letters.remove("b")
# print(letters)


#### finding the itemes

# letters = ["a","b","c"]
# letters.index("a")
# print(letters.index("b"))

# if "f" in letters:
#     print(letters.index("f"))
# if "v" in letters:
#     print(letters.index("v"))


####### Sorting list
#
# numbers = [2,5,1,5,7,2,7,2,54,7,923,4]
# # numbers.sort(reverse=True)
# print(sorted(numbers))
# print(numbers)

# numbers.sort(reverse=False)
# print(numbers)
#
# print(sorted(numbers))

# items = [
#     ("product 1 ",10),
#     ("product 2 ",5),
#     ("product 3 ",20)
# ]
# # print(sorted(items))
#
# def sorted_item(item):
#     return item[1]
#
# items.sort(key=sorted_item,reverse=True)
# print(items)



# items_list = [
#     ("Nawshin",20),
#     ("Nawshin",10),
#     ("Nawshin",5)
# ]
#
#
# def sort_item(item):
#     return item[1]
# items_list.sort(key=sort_item)
# print(items_list)



################### sort Use lambda function



items_list = [
    ("Nawshin",20),
    ("Nawshin",10),
    ("Nawshin",5)
]
# #mbda item: item[1] )
# print(items_list)


# items_list.sort(key=lambda newitem:newitem[1] )
# print(items_list)


# items_list.sort(key=lambda new:new[1])
# print(items_list)

# items_list.sort(key=lambda new:new[1])
# print(items_list)
#
# items_list.sort(reverse=True)
# print(items_list)

########## map functon

# items_list = [
#     ("Nawshin",20),
#     ("Nawshin",10),
#     ("Nawshin",5)
# ]

#
# prices = []
#
# for item in items_list:
#     prices.append(item[1])
# print(prices)
#
# x = map(lambda item:item[1],items_list)
# print("x :",list(x))


# prices = []
#
# for item in items_list:
#     prices.append(item[1])
# print(prices)
#
#
# x = list(map(lambda item:item[1],items_list))
# print(x)


################# Filter  functiuon

# items_list = [
#     ("Nawshin",20),
#     ("Limon",10),
#     ("Sorker",5)
# ]
#
# filer =  list(filter(lambda item:item[1]>=10,items_list))
# print(filer)

# filter = list(filter(lambda item:item[1] >= 10 , items_list))
# print(filter)

# filter = list(filter(lambda item:item[1]>10,items_list))
#
# print(filter)

# filter = list(filter(lambda item:item[1]>=10,items_list))
# print(filter)




############ list comprehensive


# items_list = [
#     ("Nawshin",20),
#     ("Limon",10),
#     ("Sorker",5)
# ]
#
#
# prices  = list(map(lambda item:item[1],items_list))
# print(prices)
# prices = [item[1] for item in items_list]
# print(prices)
#
# filter = list(filter(lambda item:item[1]>=10,items_list))
# print(filter)
# filter = [item for item in items_list if item[1]>=10 ]
# print(filter)


######## zip function prazctice

# a = [1,2,3,4,5]
# b = [6,7,8,9,0]
#
# result = list(zip(a,b))
# print(result)
#
# result = []
# for  a,b in zip(a,b):
#     r = a+b
#     result.append(r)
# print(result)




###########  Stacks problem LIFO
# browssing_sessiion =  []
# browssing_sessiion.append(1)
# browssing_sessiion.append(2)
# browssing_sessiion.pop()
#
# if not browssing_sessiion:
#     browssing_sessiion[-1]
#
# print(browssing_sessiion)

# browser =  []
# browser.append(1)
# browser.append(2)
# browser.pop()
#
# if not browser:
#     browser[-1]
# print(browser)


############# Queues problem FIFO

# from collections import deque
#
# queue = deque([])
# queue.append(1)
# # queue.append(2)
# # queue.append(3)
# # queue.append(4)
# queue.popleft()
#
# if not queue:
#     print("Empty")
#
# print(queue)



# from collections import deque FIFO
#
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)
#
# queue.popleft()
#
# if not queue:
#     print("Empty")
# print(queue)


############## Tuple started  (Tuple means you cannnot modify vlaues it's unmuteabel)

# point = (1,2) + (3,4)

# print(type(point))
# print(point)
# point = (1,2) * 3
# print(point)
# point = tuple([1,2,5])
# print(point)
#
# point  = (1,2,3,4,5,6)
# print(point[0:2])
#
# x, y, *z = point
# if 2 in point:
#     print("Yes")
# else:
#     print("No")



###########  Swapping Variables

# x = 10
# y = 11
#
# z = x
# x = y
# y = z
#
# print("x",x)
# print("y",y)
#
# m =10
# n =11
# print("m",m)
# print("n",n)
# m,n = n,m
# print("m",m)
# print("n",n)


############ Array  (Array look like list fully)

# from array import array
#
# numbers = array("i",[1,2,4,5])
# print(numbers)
#
# numbers = array("i",[1,2,4,5])
# numbers.append(4)
# print(numbers)
#
# numbers = array("i",[1,2,4,5])
# numbers.pop()
# print(numbers)
#
# numbers = array("i",[1,2,4,5])
# numbers.remove(1)
# print(numbers)
#
# numbers = array("i",[1,2,4,5])
# numbers.insert(0,3)
# print(numbers)
#
# numbers = array("i",[1,2,4,5])
# numbers[2] = 10
# print(numbers)



#########  sets function (it's doesn't provide duplicate item)

# numbers = [1,1,2,3,2,3]
# uniques = set(numbers)
# print(uniques)
#
# second = {1,2,3,4}
# second.add(5)
# print(second)
# second.pop()
# print(second)
#
# second = {1,2,3,4}
# second.remove(1)
# print(second)
# print(len(second))
#
# numbers = [1,2,3,4,5,6]
# first = set(numbers)
# second = {1,7}
# print(first | second)
# print(first & second)
# print(first - second)


################ Dictionaries

# value = {x: x * 2 for x in range(5)}
# print(value)
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])
#
# item = {
#     "Name":"limon",
#     "Age": "22"
# }
# print(item["Name"])
#
# value =list(map(lambda item:item ,item))
#
# print(value)

################# Expression Generator Daata size komanor jonnno use kore thake

# from sys import getsizeof ### Size dekhar jonno kore
#
# # values = [x*2 for x in range(10)]
# # print(values)
# #
# # for x in values:
# #     print(x)
#
# values = (x*2 for x in range(0000))
# print("Gen :",getsizeof(values))
# values = [x*2 for x in range(1000)]
# print("List :",getsizeof(values))


########### Unpacking operator

# numbers = [1,2,3,4]
# # print(
# #     numbers
# # )
#
# print(*numbers)  ######## Jodi individual bhave print krte cai tahole ei bhave unpack krte hoeb
#
# values = list(range(5))
# print(values)
#
# values = [*range(5),*"Hello"]
# print(values)
#
# first = [1,2]
# second = [3,4]
#
# values = [*first,"a",*second,*"Hello"]
# print(values)
#
#
# first = {"x":2}
# second = {"x":25,"y":23}
#
# combined = {**first,**second,"z":1}
# print(combined)

############ Exercise


########## Most repeted character in this sentence
from pprint import  pprint
#
# sentence = "This is my favourite sentece ssss"
#
# char_frequency = {}
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
#
# # pprint(char_frequency,width=1)
# char_frequency_sorted = sorted(char_frequency.items(),key=lambda kv:kv[1],reverse=True)
# print(char_frequency_sorted[0])



