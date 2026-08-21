# Take a string as input and count the number of vowels in it.
String=input("enter the string: ")
vowels=0
reverse=""
for i in String:
    if i in "aeiouAEIOU":
        vowels+=1
print("no.of vowels in string: "+str(vowels))


# Take a string and print it in reverse without using a built-in reverse function.
for i in String:
    reverse=i+reverse
print("reverse a string: "+reverse)

# Take a string and check whether it is a palindrome.
if String!=reverse:
    print("it is not palindrome")
else:
    print("it is palindrome")
    
# Take a sentence and find the longest word in it.
long_string=input("enter the sentence: ")
words=long_string.split(" ")
longest_word=words[0]
for word in words:
    if len(word)>len(longest_word):
        longest_word=word
print("longest word :"+longest_word)