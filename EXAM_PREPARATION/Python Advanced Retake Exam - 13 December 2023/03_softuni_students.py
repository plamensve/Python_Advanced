def softuni_students(*args, **kwargs):
    course_students = {}
    invalid_students = set()

    # Process tuple key-value pairs
    for arg in args:
        course_id, username = arg
        if course_id not in kwargs:
            invalid_students.add(username)
        else:
            course_name = kwargs[course_id]
            course_students[username] = course_name

    # Sort the data by student’s username (alphabetically)
    sorted_students = sorted(course_students.items())

    result = []

    # Print valid students
    for student, course_name in sorted_students:
        result.append(f"*** A student with the username {student} has successfully finished the course {course_name}!")

    # Print invalid students
    if invalid_students:
        invalid_message = f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"
        result.append(invalid_message)

    # Return the result as a string
    return '\n'.join(result)
