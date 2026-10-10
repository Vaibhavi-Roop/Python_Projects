empty_list = []
mark_list = [49, 31, 71, 68, 55]
print(mark_list)
print(len(mark_list))
print(mark_list[0])
print(mark_list[-1])
print(mark_list[0:3])
print(mark_list[::-1])
sample_marks = [60, 51, 55, 58]* 2
print(sample_marks)
def number_palindrome(grades):
    count = 0
    number_palindrome = []
    for mark in grades:
        mark_text = str(mark)
        if len(mark_text) > 1 and mark_text[0] == mark_text[-1]:
            count += 1 
            number_palindrome.append(mark)
        print(number_palindrome)
        return count
palindrome = number_palindrome([66, 38, 88, 99, 71])
print(palindrome)
total = 0
for mark in mark_list:
    total += mark
average = total / len(mark_list)
print(average)
mark_list.sort()
print(mark_list[0])
print(mark_list[-1])