class Student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    #should break up into smaller functions for class Courses
    def studentRecord(self, grades):
        [grade.upper() for grade in grades]
        self.grades = grades
        self.credits = len(grades) * 4
        if self.credits < 30:
            self.standing = "Freshman"
        elif self.credits < 60: # do i need an and here?
            self.standing = "Sophomore"
        elif self.credits < 90:
            self.standing = "Junior"
        elif self.credits < 120:
            self.standing = "Senior"
        else:
            self.standing = "Graduated"
        points = 0.0
        for grade in self.grades:
            if grade == "A":
                points += 4.0
            elif grade == "B":
                points += 3.0
            elif grade == "C":
                points += 2.0
            elif grade == "D":
                points += 1.0
            else:
                points += 0.0
        self.GPA = points/len(self.grades)



    def __str__(self):
        return "Name: " + self.name + "\nID: " + self.ID + "\nGrades: " + str(self.grades) + "\nCredits: " + str(self.credits) + "\nGPA: " + str(self.GPA) + "\nStanding: " + self.standing



student1 = Student("Max Smelly", "G000")
student1.studentRecord(["A", "A", "B", "A"])
student2 = Student("Alex Butts", "G001")
student2.studentRecord(["F", "F", "F"]*4)
student3 = Student("Stephanie Spears", "G002")
student3.studentRecord(["A", "A", "A", "A", "A", "B", "B", "A"]*2)

class Course():
    def __init__(self, name, cnumber, max_seats, students):
        self.name = name
        self.cnumber = cnumber
        self.max_seats = max_seats
        self.students = students

    def __str__(self):
        printSelf = "COURSE: " + self.name + "\nCNUM: " + self.cnumber + "\nMAX SEATS: " + str(self.max_seats) + "\nAVERAGE GPA: " + str(self.avg_gpa) + "\nSTUDENT LIST:\n"
        for student in self.students:
            printSelf += "\n" + str(student) + "\n"
        return printSelf

    def add_student(self, student):
        if len(self.students) < self.max_seats:
            student.studentRecord(["D"])
            self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def avg_gpa(self, students):
        self.avg_gpa = 0
        for student in students:
            self.avg_gpa += student.GPA
        self.avg_gpa = self.avg_gpa / len(students)
        return self.avg_gpa

course = Course("LC101", "CRN-101", 4, [student1, student2, student3])
course.add_student(Student("Tim Green", "G003"))
#course.remove_student(student1)
course.avg_gpa(course.students)

print(course)


