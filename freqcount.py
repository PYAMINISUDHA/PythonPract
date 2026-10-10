import string
from collections import Counter
stop_words = {"is", "a", "and", "i", "the"}
with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()
text = text.lower()
text = text.translate(str.maketrans("", "", string.punctuation))
words = text.split()
filtered_words = []
for word in words:
    if word not in stop_words:
        filtered_words.append(word)
word_counts = Counter(filtered_words)
top_words = word_counts.most_common(15)
print(f"{'Word':<15}{'Count':>5}")
print("-" * 20)
for word, count in top_words:
    print(f"{word:<15}{count:>5}")
