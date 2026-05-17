import unittest
from app.enrollment import Course

class TestCampusConnectFunctional(unittest.TestCase):

    # 1. Normal Case / Equivalence Partitioning (Valid Input)
    def test_functional_enroll_valid_user_returns_success(self):
        course = Course(capacity=10)
        actual_result = course.enroll_student("student_abc")
        self.assertEqual(actual_result, "Success")

    # 2. Error Handling / Equivalence Partitioning (Invalid Input)
    def test_functional_enroll_empty_string_raises_validation_error(self):
        course = Course(capacity=10)
        with self.assertRaises(ValueError):
            course.enroll_student("   ")

    # 3. State Transition Testing (System Memory/Rules)
    def test_functional_enroll_duplicate_user_returns_already_enrolled(self):
        course = Course(capacity=10)
        course.enroll_student("student_abc") # Initial state change
        
        # Test transition rule: User tries to do it again
        actual_result = course.enroll_student("student_abc")
        self.assertEqual(actual_result, "Already enrolled")

    # 4. Boundary Value Analysis (BVA)
    def test_functional_enroll_below_capacity_boundary_returns_success(self):
        # We test the exact boundary by setting capacity to 2
        course = Course(capacity=2)
        
        # Course is below the boundary
        actual_result = course.enroll_student("student_1")
        self.assertEqual(actual_result, "Success")

    def test_functional_enroll_at_capacity_boundary_returns_success(self):
        # We test the exact boundary by setting capacity to 2
        course = Course(capacity=2)
        course.enroll_student("student_1")
        
        # Course is now at exact boundary
        actual_result = course.enroll_student("student_2")
        self.assertEqual(actual_result, "Success")

    def test_functional_enroll_above_capacity_boundary_returns_course_full(self):
        # We test the exact boundary by setting capacity to 2
        course = Course(capacity=2)
        course.enroll_student("student_1")
        course.enroll_student("student_2") # Course is now at exact boundary
        
        # Action just above the boundary
        actual_result = course.enroll_student("student_3")
        self.assertEqual(actual_result, "Course full")    

if __name__ == "__main__":
    unittest.main(verbosity=2)