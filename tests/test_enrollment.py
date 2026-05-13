import unittest
from app.enrollment import Course

class TestCourseEnrollment(unittest.TestCase):
    def test_enroll_student_when_space_available_then_success(self):
        course = Course(capacity=30)
        student = "student_123"
        result = course.enroll_student(student)
        self.assertEqual(result, "Success")
        self.assertIn(student, course.enrolled_students)

    def test_enroll_student_when_already_enrolled_then_returns_already_enrolled(self):
        course = Course(capacity=30)
        course.enroll_student("student_123")
        result = course.enroll_student("student_123")
        self.assertEqual(result, "Already enrolled")

    def test_enroll_student_when_course_full_then_returns_course_full(self):
        course = Course(capacity=1) 
        course.enroll_student("student_1") 
        result = course.enroll_student("student_2")
        self.assertEqual(result, "Course full")

    def test_enroll_student_when_invalid_id_then_raises_valueerror(self):
        course = Course(capacity=30)
        with self.assertRaises(ValueError):
            course.enroll_student("")

if __name__ == "__main__":
    unittest.main()