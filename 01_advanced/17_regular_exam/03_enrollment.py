def gather_credits(cred, *args):
    credits_needed = int(cred)
    courses = list(args)

    credits_gathered = 0
    courses_enrolled = []

    for index in courses:
        if credits_gathered >= credits_needed:
            break

        course = index[0]
        current_credits = int(index[1])
        if course not in courses_enrolled:
            credits_gathered += current_credits
            courses_enrolled.append(course)

    result = ""

    if credits_gathered >= credits_needed:
        result += f"Enrollment finished! Maximum credits: {credits_gathered}.\n"
        result += f"Courses: {', '.join(sorted(courses_enrolled))}"
    else:
        result = f"You need to enroll in more courses! You have to gather {credits_needed - credits_gathered} credits more."

    return result


print(gather_credits(
    80,
    ("Basics", 27),
))


print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
