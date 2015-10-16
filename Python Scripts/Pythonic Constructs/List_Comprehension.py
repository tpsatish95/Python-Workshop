sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))
print(word_lengths)
# >> [5, 5, 3, 5, 4, 4, 3]

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(word_lengths)
# >> [5, 5, 3, 5, 4, 4, 3]
