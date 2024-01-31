number_of_students = int(input())
students = {}

for student in range(number_of_students):
    information = input().split()
    name, grade = information[0], float(information[1])
    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

for k, v in students.items():
    avg_result = sum(v) / len(v)
    formatted_grade = f"{' '.join([f'{g:.2f}' for g in v])}"
    print(f"{k} -> {formatted_grade} (avg: {avg_result:.2f})")
