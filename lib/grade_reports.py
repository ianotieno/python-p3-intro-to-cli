import os

def create_grade_report(student_grades):
    # Ensure the 'reports' directory exists
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    student_name, grade = student_grades.split(', ')
    with open('reports/grade_report.txt', 'w') as gr:
        gr.write(f"Student name: {student_name}\nGrade: {grade}")

if __name__ == '__main__':
    student_grades = input("Student name, grade: ")
    create_grade_report(student_grades)
