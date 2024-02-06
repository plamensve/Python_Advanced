def students_credits(*strings):
    diploma_credits = 240
    student_credits = 0
    final_msg = []
    exam_results = {}

    for info in strings:
        course_name, total_credits, total_points, student_points = info.split("-")
        result = int(student_points) / int(total_points)
        credits_part = result * int(total_credits)
        exam_results[course_name] = credits_part
        student_credits += credits_part

    if diploma_credits > student_credits:
        diff = diploma_credits - student_credits
        final_msg.append(f'Diyan needs {diff:.1f} credits more for a diploma.')

    elif diploma_credits <= student_credits:
        final_msg.append(f"Diyan gets a diploma with {student_credits:.1f} credits.")

    sorted_exam_results = sorted(exam_results.items(), key=lambda kvp: -kvp[1])
    for name, result in sorted_exam_results:
        final_msg.append(f"{name} - {float(result):.1f}")

    return '\n'.join(final_msg)


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)


