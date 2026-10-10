student_data = {
    "student_1":{"Name": "Catherine", "Class": "7R", "Year": 7}, 
    "student_2":{"Name": "Tahsina", "Class": "7R", "Year": 7},
    "student_3":{"Name": "Enya", "Class": "7R", "Year": 7},
    "student_4":{"Name": "Sana", "Class": "7P", "Year": 7}
    }
print(student_data)
print(student_data.get("student_1", "Not Found"))
print(student_data.get("student_5", "Not Found"))
student_data["student_5"] = {"Name": "Michelle", "Class": "7R", "Year": 7}
print("After adding student 5:", student_data)
student_data["student_5"]["Name"] = "Minji"
print(student_data["student_5"])
cleaned_data = {}
seen_records = []
for student_number, details in student_data.items():
    unique_combination = (details["Name"], details["Class"], details["Year"])
    if unique_combination not in seen_records:
        seen_records.append(unique_combination)
        cleaned_data[student_number] = details
student_data = cleaned_data
print(student_data)
remove = student_data.pop("Student_4", "Student not found")
print(remove)
print(len(student_data))
for student_number, details in student_data.items():
    print(student_number, ":", details)
    