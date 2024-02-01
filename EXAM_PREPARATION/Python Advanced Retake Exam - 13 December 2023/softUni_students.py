def softuni_students(*information, **students):
    course_passed = {}
    not_student_info = []
    for info in information:
        student_id = info[0]
        student_name = info[1]

        if student_id not in students.keys():
            not_student_info.append(student_name)
        else:
            for id, course in students.items():
                if student_id == id:
                    if student_name not in course_passed:
                        course_passed[student_name] = [course]
                    else:
                        course_passed[student_name].append(course)

    res_stud = dict(sorted(course_passed.items(), key=lambda kvp: kvp[0]))
    res_not_inf = sorted(not_student_info, key=lambda x: x)

    result = []
    for k, v in res_stud.items():
        result.append(f"*** A student with the username {k} has successfully finished the course {''.join(v)}!")

    if not_student_info:
        invalid_message = f"!!! Invalid course students: {', '.join(res_not_inf)}"
        result.append(invalid_message)

    return '\n'.join(result)


print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))

