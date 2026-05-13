class Course:
    def __init__(self, capacity):
        self.capacity = capacity
        self.enrolled_students = []

    def enroll_student(self, student_id):
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Invalid student ID")
        if student_id in self.enrolled_students:
            return "Already enrolled"
        if len(self.enrolled_students) >= self.capacity:
            return "Course full"
        self.enrolled_students.append(student_id)
        return "Success"