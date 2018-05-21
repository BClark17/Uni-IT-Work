from prac_07.guitar import Guitar

Guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
Guitar2 = Guitar("Another Guitar", 2012, 500)

print("Gibson L-5 CES get_age() - Expected 95, got {}".format(Guitar1.get_age()))
print("Another Guitar get_age() - Expected 5, got {}".format(Guitar2.get_age()))

print("Gibson L-5 CES is_vintage() - Expected True. Got {}".format(Guitar1.is_vintage()))
print("Another Guitar is_vintage() - Expected False. Got {}".format(Guitar2.is_vintage()))