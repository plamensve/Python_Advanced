def gather_credits(credits, *course_info):
    total_credits = 0
    course_names = []

    for el in course_info:
        if total_credits >= credits:
            break
        if el[0] in course_names:
            continue
        else:
            course_names.append(el[0])
            total_credits += int(el[1])
    if total_credits >= credits:
        return f"Enrollment finished! Maximum credits: {total_credits}.\nCourses: {', '.join(sorted(course_names))}"
    return f"You need to enroll in more courses! You have to gather {credits - total_credits} credits more."


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
