print("1. Land animal")
print("2. Sea animal")
animal = input("Which type of animal do you like from the options above:")
if animal== '1':
    print("1. Wild animal")
    print("2. Pet")
    animal_2 = input("Which type of animal do you like from the options above:")
    if animal_2 == '1':  
        print("You like wild land animals.")
    elif animal_2 == '2':
        print("You like land animals which are pets.")
    else:
        print("I don't understand.")
elif animal== '2':
    print("1. Big sea animal ")
    print("2. Small sea animal")
    animal_2 = input("Which type of animal do you like from the options above:")
    if animal_2 == '1':  
        print("You like big sea animals.")
    elif animal_2 == '2':
        print("You like small sea animals which are pets.")
    else:
        print("I don't understand.")