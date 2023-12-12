import csv
from collections import Counter

# Task 1
with open('lorem_ipsum.txt') as file:
    count = Counter(word for line in file for word in line.split())
print(count.most_common(3))

# Task 2
def top_students(file_path):
    students = []
    with open(file_path) as file_obj:
        file_obj_data = csv.reader(file_obj, delimiter=',')
        next(file_obj_data)
        for row in file_obj_data:
            students.append(row)
        return students

perform_students = top_students('students.csv')
for row in perform_students:
    if row[2] > str(90):
        print((row[0]))


