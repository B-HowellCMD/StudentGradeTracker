class Student:
    def __init__(self, name):
        # each student gets their own name and list of grades
        # self is the specific Student object being created
        self.name = name
        self.grades: list[int] = []
        
    def add_grade(self, grade: int):
        # we validate the grade before adding it 
        # this prevents invalid grades e.g.: -20 or 150
        if not isinstance(grade, int):
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

        

student1 = Student("Bryson")
student1.add_grade(90)
student1.add_grade(72)
student1.add_grade(85)
print(f"Average Grade: {student1.average_grade()}")
print(f"Highest Grade: {student1.highest_grade()}")
# make sure figure out a way to print out the averaged total of student grade