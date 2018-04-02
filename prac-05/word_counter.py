string = (input("Enter String of words to be counter:\n>>>")).split()
word_dict = {}
for item in string:
    if item in word_dict:
        word_dict[item] += 1
    else:
        word_dict[item] = 1
print("Words:")
for key, value in word_dict.items():
    print("{}".format(value),":", "{}".format(key))
