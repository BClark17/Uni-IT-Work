user_name = str(input("Enter Name: "))
print("(H)ello\n(G)oodbye\n(Quit)")
user_choice = str(input(""))
while user_choice != 'Q' and user_choice !='q':
    if user_choice == 'H' or user_choice == 'h':
        print("Hello ",user_name,"!")
    elif user_choice == 'G' or user_choice == 'g':
        print("Goodbye ",user_name,"!")
    else:
        print("Invalid Character")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    user_choice = str(input(""))
print("Simulation Terminated")