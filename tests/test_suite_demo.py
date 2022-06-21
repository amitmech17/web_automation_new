import unittest
from tests.LoginPage.Test_login_tests import LoginTests
from tests.RegisterPage.register_tests import RegisterTests
from tests.ForgotPasswordPage.forgot_password_tests import ForgotPasswordTests
# from tests.courses.register_courses_csv_data import RegisterCoursesCSVDataTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
# tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterTests)
# tc3 = unittest.TestLoader().loadTestsFromTestCase(ForgotPasswordTests)
# tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1])

unittest.TextTestRunner(verbosity=2).run(smokeTest)