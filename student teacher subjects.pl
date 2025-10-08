
teacher(alice, math).
teacher(bob, physics).
teacher(clara, chemistry).

student(john, math).
student(sue, physics).
student(mike, chemistry).
student(anna, math).
student(tom, physics).

teacher_of_student(Student, Teacher) :-
    student(Student, Subject),
    teacher(Teacher, Subject).

students_of_subject(Subject, Student) :-
    student(Student, Subject).

