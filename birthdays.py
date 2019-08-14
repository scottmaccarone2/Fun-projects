birthdays = {'Jacob Viega':'Aug 9', 'Scott Maccarone':'Oct 4',
'Kelsey Gorman':'Oct 9'}

# NOTES: I need to insert a some additional statements that handle cases where
# a user inputs a misspelled name and needs to re-type the name. I might also
# want a way of identifying the age of person as well

while True:
    print('Enter a first and last name: (blank to quit)')
    name = input()
    if name == '':
        break

    print('The name you entered is ' + name + ', is that correct? (y/n)')
    correct = input()
    if correct == 'n':
        continue

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
