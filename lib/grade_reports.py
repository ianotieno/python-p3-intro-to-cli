import os

def create_grade_report(student_grades):
    # Ensure the 'reports' directory exists
    if not os.path.exists('reports'):
        os.makedirs('reports')

    with open('reports/grade_report.txt', 'w') as gr:
        for student_info in student_grades:
            student_name, grade = student_info.split(', ')
            gr.write(f"Student name: {student_name}\nGrade: {grade}\n")

if __name__ == '__main__':
    student_grades = []

    grade = input("Student name, grade: ")
    while grade:
        student_grades.append(grade)
        # end when no grade is entered
        grade = input("Student name, grade: ")

    create_grade_report(student_grades)
