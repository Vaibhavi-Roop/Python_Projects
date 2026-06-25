unclosed_work = input("Have you closed any unclosed work? Enter Yes or No:")
if unclosed_work == 'Yes':
    updates = input("Are there any updates your computer needs to go through? Enter Yes or No:")
    if updates == 'Yes':
        print("Ready to shutdown.")
    elif updates == 'No':
        print("Run updates before shutting down.")
    else:
        print("Sorry, did not understand.")
elif unclosed_work == 'No':
    print("Close work before shutting down.")
else:
    print("Sorry, did not understand.")