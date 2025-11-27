"""
Student Grade Analyzer
---------------
Program that manage and analyze student grades
"""

# 1. Student Data (The Starting Point)
students =  [] # list of dictionaries to store data


# Show Menu function
def show_menu():
    """Function to show the menu options to the user

    return: None
    """
    print(
        f'---Student Grade Analyzer---\n'
        f'1. Add a new student\n'
        f'2. Add a grades for a student\n'
        f'3. Show report (all students)\n'
        f'4. Find top performer\n'
        f'5. Exit'
    )


# 3. Implement the Menu Options
# Option 1: Add a new student
def add_student(students, name):
    """Function to add a new student to the student list if not present

    args:
        students (list): list of dictionaries
        name (str): student name to add

    return:
        bool -> True if student was added, False otherwise
    """
    if any(student['name'] == name for student in students):
        return False
    students.append({"name": name, "grades": []})
    return True


# Option 2: Add a grade for a student
def add_grade(students, name):
    """Function for adding a new grade to the student list

    Prompts user to enter a name and if it exists ask for a grades.
    Only integers in range [0,100] accepted.
    Type "done" to exit the program.

    args:
        student(dict): student dictionary with grades list
    return:
        None
    """
    for student in students:
        if student["name"] == name:
            while True:
                grade_input = input("Enter a grade for this student (or 'done' to exit): ".format(name)).strip()
                if grade_input.lower() == 'done':
                    break

                try:
                    grade = int(grade_input)
                except ValueError:
                    print("Invalid input, please enter a number between 0 and 100, or 'done'")
                    continue

                if 0 <= grade <= 100:
                    student['grades'].append(grade)
                    print(f'Added grade {grade} for {name}')
                else:
                    print("Grade must be between 0 and 100")
            break
    else:
        print(f"Student '{name}' not found")


# Option 3: Show report (all students)
def show_report(students):
    """Show text report of student's grades

    Students sorted by average grade in descending order
    Students with no grades (N/A) showed at the end

    args:
        students(list): list of dictionaries
    return:
        list(str): printed report of student's grades
    """
    if not students:
        return ['There are no students']

    have_grades = []
    no_grades = []
    averages = []

    for student in students:
        if student['grades']:
            try:
                average = sum(student['grades']) / len(student['grades'])
            except ZeroDivisionError:
                average = 0

            have_grades.append((student['name'], average))
            averages.append(average)
        else:
            no_grades.append(student['name'])
    # Sort students that have grades by average descending
    have_grades.sort(key=lambda x: x[1], reverse=True)

    output = ["--- Student Report ---"]
    for name, average in have_grades:
        output.append(f"{name}'s average grade is {average:.1f}")
    for name in no_grades:
        output.append(f"{name}'s average grade is N/A")

    if averages:
        output.extend([
            '-' * 26,
            f'Max Average: {max(averages):.1f}',
            f'Min Average: {min(averages):.1f}',
            f'Overall Average: {sum(averages) / len(averages):.1f}',
        ])

    return output


# Option 4: Find top performer
def find_top_performer(students):
    """Find the student with the highest average grade

    args:
        students (list): list of dictionaries
    return:
        tuple or None: (name: str, average: float) or None if no grades
    """
    valid = [student for student in students if student['grades']]
    if not valid:
        return None
    best = max(valid, key=lambda s: sum(s['grades']) / len(s['grades']))
    avg = sum(best['grades']) / len(best['grades'])
    return best['name'], avg


# 2. Main Program Loop (The Menu)
def main():
    """Function to run the program

    Runs infinite loop till "5" option is entered.
    Connects all functions and collections

    return: none
    """
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice: ").strip())
        except ValueError:
            print("Please enter a number from 1 to 5")
            continue
        # Выбор 1
        if choice == 1:
            new_name = input("Enter new student name:").strip()
            if not new_name:
                print("Field can not be empty")
                continue
            name = new_name.title()
            if add_student(students, name):
                print(f'Student {name} added')
            else:
                print(f'Student {name} already exists')
        # Выбор 2
        elif choice == 2:
            new_name = input("Enter the student's name:").strip()
            if not new_name:
                print("Field can not be empty")
                continue
            name = new_name.title()
            add_grade(students, name)
        # Выбор 3
        elif choice == 3:
            report_lines = show_report(students)
            for line in report_lines:
                print(line)
        # Выбор 4
        elif choice == 4:
            top = find_top_performer(students)
            if top:
                name, avg = top
                print(f'The Student with the highest average is {name} with a grade of {avg:.1f}')
            elif not students:
                print("No students found")
            else:
                print("No student grades were found")
        # Выбор 5
        elif choice == 5:
            print("Exiting program.")
            break

        else:
            print("Invalid input, please enter a number from 1 to 5")


if __name__ == "__main__":
    main()