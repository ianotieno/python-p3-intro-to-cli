
def create_grade_report(student_grades):
    with open('reports/grade_report.txt', 'w') as gr:
        gr.write(student_grades)

if __name__ == '__main__':
    student_grades = input("Student name, grade: ")
    create_grade_report(student_grades)