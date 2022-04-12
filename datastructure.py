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

letters = ["a","b","c"]

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



# items_list = [
#     ("Nawshin",20),
#     ("Nawshin",10),
#     ("Nawshin",5)
# ]
# #mbda item: item[1] )
# print(items_list)


# items_list.sort(key=lambda newitem:newitem[1] )
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

a = [1,2,3,4,5]
b = [6,7,8,9,0]
#
# result = list(zip(a,b))
# print(result)
#
# result = []
# for  a,b in zip(a,b):
#     r = a+b
#     result.append(r)
# print(result)




###########  Stacks problem
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


############# Queues problem

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



# from collections import deque
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