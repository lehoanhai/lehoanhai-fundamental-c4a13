
alice_file = open("alice.txt")
text = alice_file.read()
alice_file.close()

ignor_words = ["\n", ",",".","!","?"]
for ignor_word in ignor_words:
    text = text.replace(ignor_word, "")
    words = text.split(" ")

word_count = {}

for word in words:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1
print(word_count)
