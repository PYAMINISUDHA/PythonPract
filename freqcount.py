import string
from collections import Counter
def analyze_text_file(filename, stop_words):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' was not found.")
        return
    except OSError as error:
        print(f"Error reading file: {error}")
        return

    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split()
    filtered_words = []
    for word in words:
        if word not in stop_words:
            filtered_words.append(word)
    word_counts = Counter(filtered_words)

    top_words = word_counts.most_common(15)
    print("\nWORD FREQUENCY REPORT")
    print("-" * 25)
    print(f"{'Word':<18}{'Count':>7}")
    print("-" * 25)

    if not top_words:
        print("No words found after filtering.")
        return

    for word, count in top_words:
        print(f"{word:<18}{count:>7}")


def main():
    stop_words = {"is", "a", "and", "i", "the"}

    filename = "sample.txt"
    analyze_text_file(filename, stop_words)


if __name__ == "__main__":
    main()
