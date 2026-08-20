string="banana apple mango cherry"
s=string.split()
first_word=min(s,key=str.lower)
print(first_word)