from tkinter import *
from Student import Student

def StartStudentCheck():
    name = student_name.get()
    surname = student_surname.get()
    grades_dict = {}
    grades_dict[subject_1.get()] = [int(subject_percentage_1.get()), subject_level_1.get()]
    grades_dict[subject_2.get()] = [int(subject_percentage_2.get()), subject_level_2.get()]
    grades_dict[subject_3.get()] = [int(subject_percentage_3.get()), subject_level_3.get()]
    grades_dict[subject_4.get()] = [int(subject_percentage_4.get()), subject_level_4.get()]
    grades_dict[subject_5.get()] = [int(subject_percentage_5.get()), subject_level_5.get()]
    grades_dict[subject_6.get()] = [int(subject_percentage_6.get()), subject_level_6.get()]

    subject_list = list(grades_dict.keys())
    percentage_and_level_list = list(grades_dict.values())

    for i in range(6):
        cao_points = 0

        if percentage_and_level_list[i][1].lower() == "ordinary level":
            if percentage_and_level_list[i][0] >= 90:
                cao_points = 56
            elif percentage_and_level_list[i][0] >= 80 and percentage_and_level_list[i][0] <= 89:
                cao_points = 46
            elif percentage_and_level_list[i][0] >= 70 and percentage_and_level_list[i][0] <= 79:
                cao_points = 37
            elif percentage_and_level_list[i][0] >= 60 and percentage_and_level_list[i][0] <= 69:
                cao_points = 28
            elif percentage_and_level_list[i][0] >= 50 and percentage_and_level_list[i][0] <= 59:
                cao_points = 20
            elif percentage_and_level_list[i][0] >= 40 and percentage_and_level_list[i][0] <= 49:
                cao_points = 12
            else:
                cao_points = 0
        elif percentage_and_level_list[i][1].lower() == "higher level":
            if percentage_and_level_list[i][0] >= 90:
                cao_points = 100
            elif percentage_and_level_list[i][0] >= 80 and percentage_and_level_list[i][0] <= 89:
                cao_points = 88
            elif percentage_and_level_list[i][0] >= 70 and percentage_and_level_list[i][0] <= 79:
                cao_points = 77
            elif percentage_and_level_list[i][0] >= 60 and percentage_and_level_list[i][0] <= 69:
                cao_points = 66
            elif percentage_and_level_list[i][0] >= 50 and percentage_and_level_list[i][0] <= 59:
                cao_points = 56
            elif percentage_and_level_list[i][0] >= 40 and percentage_and_level_list[i][0] <= 49:
                cao_points = 46
            elif percentage_and_level_list[i][0] >= 30 and percentage_and_level_list[i][0] <= 39:
                cao_points = 37
            else:
                cao_points = 0

        if subject_list[i] == "maths" and percentage_and_level_list[i][1].lower() == "higher level" and (percentage_and_level_list[i][0] >= 40 and percentage_and_level_list[i][0] <= 100):
            cao_points += 25

        grades_dict[subject_list[i]] = cao_points

    course_cao_points_list = []
    for course_points in [int(course_points_1.get()), int(course_points_2.get()), int(course_points_3.get()), int(course_points_4.get()), int(course_points_5.get()), int(course_points_6.get()), int(course_points_7.get()), int(course_points_8.get()), int(course_points_9.get()), int(course_points_10.get())]:
        course_cao_points_list.append(course_points)

    student = Student(name, surname, grades_dict, course_cao_points_list)

    approved_course_label.config(text=CheckCourseApproval(student))

def CheckCourseApproval(student):
    total_student_grade = 0
    for i in range(6):
        total_student_grade += list(student.grades_dict.values())[i]

    for i in range(10):
        if total_student_grade >= student.course_cao_points_list[i]:
            return f"Student {student.name} {student.surname} was approved for the course number {i+1}"

    return f"Student {student.name} {student.surname} was not approved for any of the courses"

window = Tk()
window.title("Course Approval")
window.geometry("950x840")
window.resizable(False, False)
window.config(bg="#141724")

student_info = LabelFrame(text="Student Info", bg="#141724", fg="white", font="Courier 15")
student_info.grid(column=0, row=0, padx=20, pady=20, columnspan=2)

student_name_label = Label(student_info, text="Student name", bg="#141724", fg="white", font="Courier 10")
student_name_label.grid(column=0, row=0, padx=5, pady=5)
student_name = Entry(student_info, borderwidth=5, width=30)
student_name.grid(column=0, row=1, padx=10, pady=10)

student_surname_label = Label(student_info, text="Student surname", bg="#141724", fg="white", font="Courier 10")
student_surname_label.grid(column=1, row=0, padx=5, pady=5)
student_surname = Entry(student_info, borderwidth=5, width=30)
student_surname.grid(column=1, row=1, padx=10, pady=10)


student_grades = LabelFrame(text="Student Grades", bg="#141724", fg="white", font="Courier 15")
student_grades.grid(column=0, row=1, padx=20, pady=20)

subject_label = Label(student_grades, text="Subject", bg="#141724", fg="white", font="Courier 10")
subject_label.grid(column=0, row=0, padx=5, pady=5)

subject_level_label = Label(student_grades, text="Subject Level", bg="#141724", fg="white", font="Courier 10")
subject_level_label.grid(column=1, row=0, padx=5, pady=5)

subject_percentage_label = Label(student_grades, text="Percentage", bg="#141724", fg="white", font="Courier 10")
subject_percentage_label.grid(column=2, row=0, padx=5, pady=5)

subject_1 = Entry(student_grades, borderwidth=5, width=30)
subject_1.grid(column=0, row=1, padx=10, pady=10)
subject_2 = Entry(student_grades, borderwidth=5, width=30)
subject_2.grid(column=0, row=2, padx=10, pady=10)
subject_3 = Entry(student_grades, borderwidth=5, width=30)
subject_3.grid(column=0, row=3, padx=10, pady=10)
subject_4 = Entry(student_grades, borderwidth=5, width=30)
subject_4.grid(column=0, row=4, padx=10, pady=10)
subject_5 = Entry(student_grades, borderwidth=5, width=30)
subject_5.grid(column=0, row=5, padx=10, pady=10)
subject_6 = Entry(student_grades, borderwidth=5, width=30)
subject_6.grid(column=0, row=6, padx=10, pady=10)

subject_level_1 = Entry(student_grades, borderwidth=5, width=30)
subject_level_1.grid(column=1, row=1, padx=10, pady=10)
subject_level_2 = Entry(student_grades, borderwidth=5, width=30)
subject_level_2.grid(column=1, row=2, padx=10, pady=10)
subject_level_3 = Entry(student_grades, borderwidth=5, width=30)
subject_level_3.grid(column=1, row=3, padx=10, pady=10)
subject_level_4 = Entry(student_grades, borderwidth=5, width=30)
subject_level_4.grid(column=1, row=4, padx=10, pady=10)
subject_level_5 = Entry(student_grades, borderwidth=5, width=30)
subject_level_5.grid(column=1, row=5, padx=10, pady=10)
subject_level_6 = Entry(student_grades, borderwidth=5, width=30)
subject_level_6.grid(column=1, row=6, padx=10, pady=10)

subject_percentage_1 = Entry(student_grades, borderwidth=5, width=30)
subject_percentage_1.grid(column=2, row=1, padx=10, pady=10)
subject_percentage_2 = Entry(student_grades, borderwidth=5, width=30)
subject_percentage_2.grid(column=2, row=2, padx=10, pady=10)
subject_percentage_3 = Entry(student_grades, borderwidth=5, width=30)
subject_percentage_3.grid(column=2, row=3, padx=10, pady=10)
subject_percentage_4 = Entry(student_grades, borderwidth=5, width=30)
subject_percentage_4.grid(column=2, row=4, padx=10, pady=10)
subject_percentage_5 = Entry(student_grades, borderwidth=5, width=30)
subject_percentage_5.grid(column=2, row=5, padx=10, pady=10)
subject_percentage_6 = Entry(student_grades, borderwidth=5, width=30)
subject_percentage_6.grid(column=2, row=6, padx=10, pady=10)


courses_points = LabelFrame(text="Courses Points", bg="#141724", fg="white", font="Courier 15")
courses_points.grid(column=1, row=1, padx=20, pady=20)

cao_points_label = Label(courses_points, text="CAO Points Needed", bg="#141724", fg="white", font="Courier 10")
cao_points_label.grid(column=0, row=0, padx=5, pady=5)

course_points_1 = Entry(courses_points, borderwidth=5, width=30)
course_points_1.grid(column=0, row=1, padx=10, pady=10)
course_points_2 = Entry(courses_points, borderwidth=5, width=30)
course_points_2.grid(column=0, row=2, padx=10, pady=10)
course_points_3 = Entry(courses_points, borderwidth=5, width=30)
course_points_3.grid(column=0, row=3, padx=10, pady=10)
course_points_4 = Entry(courses_points, borderwidth=5, width=30)
course_points_4.grid(column=0, row=4, padx=10, pady=10)
course_points_5 = Entry(courses_points, borderwidth=5, width=30)
course_points_5.grid(column=0, row=5, padx=10, pady=10)
course_points_6 = Entry(courses_points, borderwidth=5, width=30)
course_points_6.grid(column=0, row=6, padx=10, pady=10)
course_points_7 = Entry(courses_points, borderwidth=5, width=30)
course_points_7.grid(column=0, row=7, padx=10, pady=10)
course_points_8 = Entry(courses_points, borderwidth=5, width=30)
course_points_8.grid(column=0, row=8, padx=10, pady=10)
course_points_9 = Entry(courses_points, borderwidth=5, width=30)
course_points_9.grid(column=0, row=9, padx=10, pady=10)
course_points_10 = Entry(courses_points, borderwidth=5, width=30)
course_points_10.grid(column=0, row=10, padx=10, pady=10)

approved_course_label = Label(text="", bg="#141724", fg="white", font="Courier 12")
approved_course_label.grid(column=0, row=2, padx=5, pady=5, columnspan=2)

start_course_approval_button = Button(text="Start Course Approval", width=30, height=2, borderwidth=3, font="Courier 12", command=StartStudentCheck)
start_course_approval_button.grid(column=0, row=3, padx=20, pady=20, columnspan=2)

window.mainloop()