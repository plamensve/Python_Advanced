def gather_credits(needed_credits, *courses_info):
    gathered_credits = 0
    enrolled_courses = []

    for course_name, course_credits in courses_info:
        if gathered_credits >= needed_credits:
            break
        if course_name in enrolled_courses:
            continue
        enrolled_courses.append(course_name)
        gathered_credits += course_credits

    if gathered_credits >= needed_credits:
        return f"""Enrollment finished! Maximum credits: {gathered_credits}.
Courses: {', '.join(sorted(enrolled_courses))}"""
    return f"You need to enroll in more courses! You have to gather {needed_credits - gathered_credits} credits more."

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))





