from unittest import TestCase
import unittest

from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("Pesho")
        self.student_with_courses = Student("Alex", {"Math": ["Algebra"]})

    def test_student_correct_initialization(self):
        self.assertEqual("Pesho", self.student.name)
        self.assertEqual({}, self.student.courses)

        self.assertEqual("Alex", self.student_with_courses.name)
        self.assertEqual({"Math": ["Algebra"]}, self.student_with_courses.courses)

    def test_enroll_and_add_notes_to_existing_course(self):
        result = self.student_with_courses.enroll("Math", ["Math is hard"])

        self.assertEqual(["Algebra", "Math is hard"],
                         self.student_with_courses.courses["Math"])

        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_and_add_notes_to_nonexisting_course_wihtout_third_param(self):
        result = self.student.enroll("Java", ["Java sucks"])

        self.assertEqual(["Java sucks"], self.student.courses["Java"])

        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_and_add_nots_to_nonexisting_course_with_third_param(self):
        result = self.student.enroll("Java", ["Java sucks"], "Y")

        self.assertEqual(["Java sucks"], self.student.courses["Java"])

        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_and_add_new_course_without_adding_the_notes(self):
        result = self.student.enroll("Java", ["Java sucks"], "n")

        self.assertEqual([], self.student.courses["Java"])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_on_existing_course(self):
        result = self.student_with_courses.add_notes("Math", "Math still sucks")

        self.assertEqual(["Algebra", "Math still sucks"],
                         self.student_with_courses.courses["Math"])

        self.assertEqual("Notes have been updated", result)

    def test_add_notes_on_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_courses.add_notes("Stars", "Math still sucks")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        result = self.student_with_courses.leave_course("Math")

        self.assertEqual({}, self.student_with_courses.courses)

        self.assertEqual("Course has been removed", result)

    def test_leave_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Math")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    unittest.main()