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

    def test_drop_student_when_enrolled_then_dropped(self):
        course = Course(capacity=30)
        course.enroll_student("student_123")

        result = course.drop_student("student_123")

        self.assertEqual(result, "Dropped")
        self.assertNotIn("student_123", course.enrolled_students)

    def test_drop_student_when_not_enrolled_then_returns_student_not_enrolled(self):
        course = Course(capacity=30)

        result = course.drop_student("student_999")

        self.assertEqual(result, "Student not enrolled")

    def test_get_enrollment_count_returns_correct_count(self):
        course = Course(capacity=30)
        course.enroll_student("student_1")
        course.enroll_student("student_2")

        result = course.get_enrollment_count()

        self.assertEqual(result, 2)

    def test_is_full_when_capacity_reached_then_true(self):
        course = Course(capacity=2)
        course.enroll_student("student_1")
        course.enroll_student("student_2")

        self.assertTrue(course.is_full())

    def test_get_enrolled_students_returns_copy(self):
        course = Course(capacity=30)
        course.enroll_student("student_1")

        students = course.get_enrolled_students()
        students.append("fake_student")

        self.assertNotIn("fake_student", course.enrolled_students)

    def test_course_when_invalid_capacity_then_raises_valueerror(self):
        with self.assertRaises(ValueError):
            Course(capacity=0)

    def test_drop_student_when_invalid_id_then_raises_valueerror(self):
        course = Course(capacity=30)

        with self.assertRaises(ValueError):
            course.drop_student("")


if __name__ == "__main__":
    unittest.main(verbosity=2)