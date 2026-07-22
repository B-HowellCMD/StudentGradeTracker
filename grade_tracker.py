class Student:
    def __init__(self, name):
        # each student gets their own name and list of grades
        # self is the specific Student object being created
        self.name = name
        self.grades: list[int, float] = []
        
    def add_grade(self, grade: int | float):
        # we validate the grade before adding it 
        # this prevents invalid grades e.g.: -20 or 150
        if not isinstance(grade, int, float):
            print("Grade input must be a number value")
            return
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"{grade} added for {self.name}.")
        else:
            print("Grade must be between 0 and 100.")
            
    def display_grades(self):
        print(f"\nGrades for {self.name}: ")
        
        for grade in self.grades:
            print(grade)
            

student1 = Student("Bryson")
student1.add_grade(90)
student1.add_grade(72)
student1.add_grade(85)