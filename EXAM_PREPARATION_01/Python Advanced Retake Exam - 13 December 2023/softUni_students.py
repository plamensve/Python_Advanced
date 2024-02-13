def softuni_students(*information, **course):
    course_info = {}
    student_info = []
    msg = ''
    for course_id, course_name in course.items():
        course_info[course_id] = course_name

    for passed_course, student_name in information:
        student_info.append((passed_course, student_name))

    sorted_student_info = sorted(student_info, key=lambda x: x[1])
    for sorted_id, sorted_name in sorted_student_info:
        if sorted_id in course_info.keys():
            msg += f"*** A student with the username {sorted_name} has successfully finished the course {course_info[sorted_id]}!\n"

    fist_string = '!!! Invalid course students: '
    invalid_names = []
    for sorted_id, sorted_name in sorted_student_info:
        if sorted_id not in course_info.keys():
            invalid_names.append(sorted_name)

    if invalid_names:
        msg += f"{fist_string}{', '.join(invalid_names)}"

    return msg


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))




