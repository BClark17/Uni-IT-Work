from prac_07.guitar import Guitar

my_guitars = []
while True:
    name = input('Name:')
    if name == '':
        break
    year = input('Year:')
    cost = input('cost:')
    temp_guitar = Guitar(name, year, cost)
    my_guitars.append(temp_guitar)
    print(temp_guitar, ' added.')
print("        ... snip ...        ")
print('These are my guitars:')

guitar_counter = 1
for guitar in my_guitars:
    if guitar.is_vintage is True:
        print('Guitar {}: {} ({}), worth ${} (vintage)'.format(guitar_counter, guitar.name, guitar.year, guitar.cost))
    else:
        print('Guitar {}: {} ({}), worth ${}'.format(guitar_counter, guitar.name, guitar.year, guitar.cost))
    guitar_counter += 1
