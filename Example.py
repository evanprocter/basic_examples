try:
    how_many =int(input("How many sushi rolls? "))
    too_many = 20
    if how_many > too_many:
        print("Ugh. Need a nap...and pepto")
    else:
        print("Order more rolls!")
except:
    print("You didn't enter a number.")