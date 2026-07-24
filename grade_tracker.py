from collections import defaultdict

class Student:
    def __init__(self, name):
        # each student gets their own name and list of grades
        # self is the specific Student object being created
        self.name = name
        self.grades = defaultdict(list) # map takes in a student as a key : then a grade per student
        
    def add_grade(self, grade: int):
        # we validate the grade before adding it 
        # this prevents invalid grades e.g.: -20 or 150
        while True:
            std_name = input("Enter Student's name: ").strip().title()
            if std_name == "exit":
                break 
            
            grade_input = input(f"Enter {std_name}'s grades: ").strip()
            
            try:
                grade = float(grade_input)
                self.grades[std_name].append(grade)
                print(f"Grades for {std_name} has been added: {grade}")
            except ValueError:
                print("Please enter a proper value")
            
    def display_grades(self):
        print(f"\nGrades for {self.name}: ")
        
        for grade in self.grades:
            print(grade)
            
    def average_grade(self):
        total = 0;
        for grade in self.grades:
            total += grade
        if len(self.grades) == 0:
            return 0
        total_avg = total / len(self.grades)
        print(f"Average Grade: {total_avg}")
        return total_avg

    def highest_grade(self):
        if len(self.grades) == 0:
            return
        highest_score = max(self.grades)
        return highest_score

        
<<<<<<< HEAD
        print(f"Average Grade:")
        


# we should make a way to have each student have its own entry 
# a student can be added in at any time with input
# make a menu with options to add, delete, and edit students and their grades
=======

student1 = Student("Bryson")
student1.add_grade(90)
student1.add_grade(72)
student1.add_grade(85)
print(f"Average Grade: {student1.average_grade()}")
print(f"Highest Grade: {student1.highest_grade()}")
# make sure figure out a way to print out the averaged total of student grade
>>>>>>> 586f0b0104e3be6f67d470b1e52dfde81c4eddcd
