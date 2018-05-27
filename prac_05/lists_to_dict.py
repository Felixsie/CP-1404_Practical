#CP1404 Practical Week 5.

NUMBER_OF_PEOPLE = 1
names_of_people = []
dobs = []


for i in range(NUMBER_OF_PEOPLE):
    name_input = input("Enter {} name: ".format(i + 1))
    names_of_people.append(name_input)
    dob_input = input("Enter {} date of birth (d/m/y): ".format(i + 1))
    parts = dob_input.split("/")
    one_dob = tuple([int(part) for part in parts])
    dobs.append(dob_input)



print("{} = {}".format(names_of_people, dobs))