def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 40:
        return "D"

    else:
        return "F"


name = input("Enter student name: ")

subjects = ["Python", "SQL", "Statistics", "Machine Learning", "Mathematics"]

marks = []

for subject in subjects:

    mark = float(input(f"Enter marks for {subject}: "))

    if mark < 0 or mark > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        exit()

    marks.append(mark)


total = sum(marks)

percentage = total / len(subjects)

grade = calculate_grade(percentage)

if all(mark >= 35 for mark in marks):
    result = "PASS"
else:
    result = "FAIL"


print("\n======= STUDENT RESULT =======")

print("Name:", name)

print("Total Marks:", total, "/ 500")

print("Percentage:", percentage, "%")

print("Grade:", grade)

print("Result:", result)

print("==============================")