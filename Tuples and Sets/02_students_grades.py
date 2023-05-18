from statistics import mean
student_count = int(input())

grades_by_student = {}

for _ in range(student_count):
    student, grade = input().split()
    grade = float(grade)
    if student not in grades_by_student:
        grades_by_student[student] = []
    grades_by_student[student].append(grade)

for student, grades in grades_by_student.items():
    avg = mean(grades_by_student[student])
    print(f"{student} -> {' '.join(str(f'{grade:.2f}') for grade in grades)} (avg: {avg:.2f})")