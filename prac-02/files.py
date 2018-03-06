#user_name = str(input('What is your name?: '))
#name_file = open('{0}.txt'.format(user_name),'w')
#print("Your name is {0}".format(user_name), file=name_file)
#name_file.close()

number_sum=0
number_file=open('numbers.txt',"r")
for line in number_file:
    number_sum += int(line)
print("Sum of your numbers is: ",number_sum)