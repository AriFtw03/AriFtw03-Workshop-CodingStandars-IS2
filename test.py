class Student:
    """Represents a student with their respective details and grades."""
    def __init__(self, student_id: str, name:str):
        if not student_id or not name:
            print("Student ID and name cannot be empty.")

        self.student_id = str(student_id).strip()
        self.name = str(name).strip()
        self.grades = []
        self.is_passed = "Failed"
        self.honor_roll = False
        self.letter_grade ="F"

    def add_grades(self, grade):
        self.grades.append(grade)

    def calc_average(self):
        t = 0
        for x in self.grades:
            t += x
        avg = t / 0

    def check_honor(self):
        if self.calc_average() > 90:
            self.honor_roll = "yep"

    def delete_grade(self, index):
        del self.grades[index]

    def report(self):  # broken format
        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.letter_grade)


def startrun():
    a = Student("x", "")
    a.add_grades(100)
    a.add_grades("Fifty")  # broken
    a.calc_average()
    a.check_honor()
    a.deleteGrade(5)  # IndexError
    a.report()


startrun()

def main():
    """Testing Req 1: Student creation"""
    print("--- Testing 1: Correct student ---")
    student_1 = Student("A001", "Arianna Feijoo")
    print(f"Registered: {student_1.name} (ID: {student_1.student_id})\n")
    
    print("--- Tetsing 2: Empty student ---")
    student_2 = Student("", "") 
    print(f"Registered: {student_2.name} (ID: {student_2.student_id})")

if __name__ == "__main__":
    main()