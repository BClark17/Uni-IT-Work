string = (input("Enter String of words to be counter:\n>>>")).split()
word_dict = {}
longest_word = 0
for item in string:
    if len(item) > longest_word:
        longest_word = len(item)
    if item in word_dict:
        word_dict[item] += 1
    else:
        word_dict[item] = 1
print("Words:")
for key, value in word_dict.items():
    print("{}".format(key), " " * (longest_word - len(key)), ":", "{}".format(value))
