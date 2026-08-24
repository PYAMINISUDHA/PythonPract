file=open("data.py","w")
file.write("from datetime import datetime\n" "date_today=datetime.now()\n" "print(date_today)")
file.close()
file=open("data.py","r")
content=file.read()
print(content)
exec(content)
# print(file)
file=open("data.py","a")
file.write("add a new line")

file.close()
file=open("data.py","r")
content=file.read()
print(content)
# print(file)
file.close()


