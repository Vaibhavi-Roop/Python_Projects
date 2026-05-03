medical_condition = input("Do you have a medical condition? (Y/N):")
medical_condition = medical_condition.strip().upper()
if medical_condition=='Y':
    print("You are allowed.")
else:
    attendance = int(input("How many days have you been at school:"))
    if attendance > 75:
        print("You are allowed.")
    else:
        print("You are not allowed.")