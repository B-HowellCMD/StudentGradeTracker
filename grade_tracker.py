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
        return total / len(self.grades)   
        
        print(f"Average Grade:")
        


# we should make a way to have each student have its own entry 
# a student can be added in at any time with input
# make a menu with options to add, delete, and edit students and their grades