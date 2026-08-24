
# from collections import Counter
# arr=[1,2,4,4,5,6]
# print(Counter(arr))

# import sqlite3
# connection = sqlite3.connect("students.db")
# cursor=connection.cursor()
# cursor.execute(""" create table if not exists student(id integer,name text)""")
# connection.commit()
# connection.close()


# file=open("data.txt","r")
# # content=file.read()  
# # content=file.readline()  
# content=file.readlines()  
# print(content)
# file.close()

# file=open("data.txt","w")
# file.write("this is for testing purpose!\n")
# file.close()

# file=open("data.txt","r")
# content=file.read()
# print(content)
# file.close()

file=open("data1.py","w")
# import datetime
# now=datetime.datetime.now()
file.write("import datetime\nnow=datetime.datetime.now()\nprint(now)")
file.close()
file=open("data1.py","r")
content=file.read()
print(content)
file.close()
exec(content)



