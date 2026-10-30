import student

marks = []

for i in range(5):
    mark = float(input("Enter marks: "))
    marks.append(mark)

total = student.total_marks(marks)
percent = student.percentage(marks)
grade = student.grade(percent)

print("Total Marks:", total)
print("Percentage:", percent)
print("Grade:", grade)