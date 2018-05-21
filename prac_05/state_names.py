"""
CP1404/CP5632 Practical
State names in a dictionary
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)

state = input("Enter short state: ")
state = state.upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
        break
    else:
        print("Invalid short state")
    state = input("Enter short state: ")

print("\n\nDICTIONARY:")
for key, value in STATE_NAMES.items():
    print("{}".format(key), " " * (4-len(key)), "is ", "{}".format(value))