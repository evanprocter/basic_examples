# configuration section
year_to_check = 1999
party_message = "Party like it's %d"

# processing
birth_year = int(input("Birth year? "))
is_classic = birth_year <= year_to_check

if is_classic:
    # print("Party like it's %d" % year_to_check)
    message = party_message % year_to_check
else:
    # print("Party like it's %d" % birth_year)
    message = party_message % birth_year

# output
print(message)