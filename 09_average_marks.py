def calculate_average(marks):

    total = sum(marks)

    average = total / len(marks)

    return average


marks = [70, 80, 90, 85, 95]

result = calculate_average(marks)

print("Average Marks:", result)