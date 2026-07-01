# ----------------Student details using tpyecasting------------
student_name = "Mine"
marks_english = "88.5"
marks_math = "92"
marks_science = "76.5"
marks_history = "85"
marks_computer = "95.5"
total_subjects = "5"
max_marks_per_subject = "100"
fee_paid = "15000.75"
fee_due = "5000"


student_name = str(student_name)
marks_english =   float(marks_english)
marks_math =   float(marks_math)
marks_science =  float(marks_science)
marks_history =  float(marks_history)
marks_computer =   float(marks_computer)
total_subjects = int(total_subjects)
max_marks_per_subject  = int(max_marks_per_subject)
fee_paid = float(fee_paid)
fee_due = float(fee_due)


total_marks = marks_english + marks_math + marks_science + marks_history + marks_computer 
percentage = (total_marks / (max_marks_per_subject*total_subjects) ) * 100
percentage = int(percentage)
grade = bool(total_marks > 400)
fully_fee_paid = bool(fee_paid - fee_due == 0 )


print(str("____student details____"))
print(str(student_name))
print("Total marks:" + str(total_marks))
print(("Percentage:" + str(percentage)))
print(("Grade:" + str(grade)))
print("Fee status:" + str(fully_fee_paid))

# Output
# ____student details____
# Mine
# Total marks:437.5
# Percentage:87
# Grade:True
# Fee status:False

