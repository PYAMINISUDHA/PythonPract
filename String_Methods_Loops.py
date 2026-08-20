word=input()
digit=0
vowels=0
consonants=0
for i in word:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        if i.lower() in "aeiou":
            vowels+=1
        else:
            consonants+=1
            
print(digit)
print(vowels)
print(consonants)