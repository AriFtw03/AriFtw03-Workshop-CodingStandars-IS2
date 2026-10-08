"""
Student Grade Management System
"""

class Student:
    """Represents a student with their respective details and grades."""
    def __init__(self, student_id: str, name:str):
        if not student_id or not name:
            print("Student ID and name cannot be empty.")
            self.student_id = "Unknown"
            self.name = "Unknown"
        else:
            self.student_id = str(student_id).strip()
            self.name = str(name).strip()
            
        self.grades = []
        self.is_passed = "Failed"
        self.honor_roll = False
        self.letter_grade ="F"

    def add_grade(self, grade):
        """Adds a numeric grade between 0 and 100"""
        try:
            numeric_grade = float(grade)
        except (ValueError, TypeError):
            print(f"Error: '{grade}' is not valid number.")
            return

        if 0.0 <= numeric_grade <= 100.0:
            self.grades.append(numeric_grade)
            print(f"Grade {numeric_grade} added.")
            self.update_status()
        else:
            print(f"Error: Grade {numeric_grade} must be between 0 and 100.")

    def calculate_average(self):
        """Calculates and returns the average of all of the grades."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def determine_letter_grade(self, average):
        """Converts grade (average) into a letter grade."""
        if average >= 90: return "A"
        if average >= 80: return "B"
        if average >= 70: return "C"
        if average >= 60: return "D"
        return "F"

    def update_status(self):
        """Updates all student statuses based on grades."""
        avg = self.calculate_average()
        self.letter_grade = self.determine_letter_grade(avg)
        self.is_passed = "Passed" if avg >= 60.0 else "Failed"
        self.honor_roll = avg >= 90.0

    def remove_grade_by_index(self, index: int):
        """Removes a grade by its list index gracefully."""
        try:
            removed = self.grades.pop(index)
            print(f"Success: Grade {removed} removed from index {index}.")
            self.update_status()
        except IndexError:
            print(f"Error: Index {index} is out of bounds.")

    def remove_grade_by_value(self, value: float):
        """Removes a grade by its specific numeric value gracefully."""
        try:
            self.grades.remove(value)
            print(f"Success: Grade {value} removed.")
            self.update_status()
        except ValueError:
            print(f"Error: Grade {value} does not exist.")

    def generate_report(self):
        """Generates a formatted summary report for the student."""
        avg = self.calculate_average()
        print("\n--- Student Summary Report ---")
        print(f"Student ID       : {self.student_id}")
        print(f"Student Name     : {self.name}")
        print(f"Number of Grades : {len(self.grades)}")
        print(f"Average Grade    : {avg:.2f}")
        print(f"Letter Grade     : {self.letter_grade}")
        print(f"Pass/Fail Status : {self.is_passed}")
        print(f"Honor Roll       : {self.honor_roll}")
        print("------------------------------\n")


def main():
    """Testing Req 1: Student creation"""
    print("--- Testing 1: Correct student ---")
    student_1 = Student("A001", "Arianna Feijoo")
    print(f"Registered: {student_1.name} (ID: {student_1.student_id})\n")
    
    print("--- Tetsing 2: Empty student ---")
    student_2 = Student("", "") 
    print(f"Registered: {student_2.name} (ID: {student_2.student_id})\n")

    """Testing Req 2 & 6: Adding grades and validation"""
    print("--- Creating student ---")
    student = Student("A001", "Arianna Feijoo")
    
    print("\n--- Testing grades ---")
    student.add_grade(95)       # Valid
    student.add_grade(88.5)     # Valid
    student.add_grade("Fifty")  # Invalid (graceful fail)
    student.add_grade(150)      # Invalid (graceful fail)
    
    print(f"\nFinal grades: {student.grades}")

    """Testing Req 3, 4, 5, 7: Calculations and states"""
    print("\n--- Adding grades ---")
    student = Student("A001", "Arianna Feijoo")
    student.add_grade(95)
    student.add_grade(85)
    
    print("\n--- Calculation Results ---")
    print(f"Average: {student.calculate_average()}")
    print(f"Letter Grade: {student.letter_grade}")
    print(f"Status (Pass/Fail): {student.is_passed}")
    print(f"Honor Roll (>=90): {student.honor_roll}")
    
    """Testing Req 8: Removing grades"""
    print("\n--- Testing graceful removal ---")
    student.add_grade(60) 
    print(f"Current grades: {student.grades}")
    
    student.remove_grade_by_index(0)    
    student.remove_grade_by_value(60)   
    student.remove_grade_by_index(10)   # Invalid index
    student.remove_grade_by_value(100)  # Invalid value
    
    """Testing Req 9: Final Report"""
    student.generate_report()


if __name__ == "__main__":
    main()