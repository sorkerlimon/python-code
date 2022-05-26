# # from pathlib import Path
# # import json
# #
# # movies = [
# #     {"id":1,"name":"limon"},
# #     {"id":2,"name":"sorker"}
# #
# # ]
# #
# # data = json.dumps(movies)
# # Path("movies.json").write_text(data)
# #
# #
# #
# # data2 = Path("movies.json").read_text()
# # movies = json.loads(data2)
# # print(movies[0]["name"])

# #
# import json
# from pathlib import Path
# import sqlite3

# movies_name = [
#     {"Id":1,"Tittle":"Avater","year":222},
#     {"Id":2,"Tittle":"kgf","year":3421},
#     {"Id":3,"Tittle":"mesh","year":342}
# ]

# data = json.dumps(movies_name)
# Path("movies.json").write_text(data)
# #
# #
# # data2 = Path("Movies_name.json").read_text()
# # movies_list = json.loads(data2)
# # print(movies_list[2]["Tittle"])



# #SQLite
# movies = Path("movies.json").read_text()

# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO Movies  VALUES(?, ?, ?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()





import sqlite3


# conn = sqlite3.connect('test1.sqlite3')
# print("Data base Create succesfully ..")

# conn.execute('''CREATE TABLE COMPANY2
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);''')
# print( "Table created successfully")

# conn.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (5, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

# conn.commit()
# print("Records created successfully")

# conn.close()


############ Read data from data base
with sqlite3.connect("test1.sqlite3") as conn:
    command = "SELECT * FROM COMPANY"
    cursor = conn.execute(command)
    for row in cursor:
        print(row)

 
#### Data write  into the data base 
# conn = sqlite3.connect('test1.sqlite3')
# print("Opened database successfully")

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (1, 'Paul', 32, 'California', 20000.00 )");

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

# conn.commit()
# print("Records created successfully")
# conn.close()
