class Course:
    def __init__(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a positive integer")

        self.capacity = capacity
        self.enrolled_students = []

    def enroll_student(self, student_id):
        if not self._is_valid_student_id(student_id):
            raise ValueError("Invalid student ID")

        if student_id in self.enrolled_students:
            return "Already enrolled"

        if self.is_full():
            return "Course full"

        self.enrolled_students.append(student_id)
        return "Success"

    def drop_student(self, student_id):
        if not self._is_valid_student_id(student_id):
            raise ValueError("Invalid student ID")

        if student_id not in self.enrolled_students:
            return "Student not enrolled"

        self.enrolled_students.remove(student_id)
        return "Dropped"

    def get_enrollment_count(self):
        return len(self.enrolled_students)

    def is_full(self):
        return self.get_enrollment_count() >= self.capacity

    def get_enrolled_students(self):
        return self.enrolled_students.copy()

    def _is_valid_student_id(self, student_id):
        return isinstance(student_id, str) and bool(student_id.strip())