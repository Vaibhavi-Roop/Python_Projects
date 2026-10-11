Books = ["The Naturals", "OUABH", "Shatter Me" "Powerless", "AGGGTM", "PJO"]
Copies = [9, 1, 7, 8, 4, 3 ]
Library = {book: count for book, count in zip(Books, Copies)}
print("All books", Library)
available_books = [book for book in Books if Library[book]> 0]
print("Availible books", available_books)
borrow = input("Which book are you borrowing?")
if borrow not in Library or Library[borrow] ==0:
    print("The book is not available!")
    exit()
late_fee = [ 5, 8, 2, 6, 7]
extra_fee = int(input("Enter the late fee of $8 (enter 8):"))
total_fee = list(map(lambda fee: fee + extra_fee, late_fee))
print("The total fee is $", total_fee)
book_index = Books.index(borrow)
chosen_fee = total_fee[book_index]
print("Late fee for", borrow, "after the update", chosen_fee)
Library[borrow] = Library[borrow] - 1
print(borrow, "is borrowed, the remaining copies are:", Library[borrow])

