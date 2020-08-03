# code originally from https://techdevguide.withgoogle.com/paths/foundational/find-longest-word-in-dictionary-that-subsequence-of-given-string#code-challenge
# edited by mikie Reed 8.3.2020

def find_longest_word_in_string(letters, words):
    # by sorting you ensure you have the longest word with first match
    for word in sorted(words, key=lambda w: len(w), reverse=True):
        word_index = 0
        letters_index = 0
        match = False
        while (word_index < len(word)):
            if (word[word_index] == letters[letters_index]):
                word_index += 1
                letters_index += 1
                match = True
            else:
                letters_index += 1
                match = False

            if (letters_index >= len(letters)):
                break

        if (match):
            return word


if __name__ == '__main__':
    letters = "abppplee"
    words = ["able", "ale", "apple", "bale", "kangaroo"]
    word = find_longest_word_in_string(letters, words)
    print(f"Longest Word: {word}")
