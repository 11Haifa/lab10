import unittest
from emp import EmpSystem 

class EmpSystemTests(unittest.TestCase):
    def setUp(self):
        self.e = EmpSystem()

    def tearDown(self):
        pass

    def test_create_employee(self):
        self.e.create("John Doe", 30, 1, "HR")
        self.assertEqual(len(self.e.employees), 1)  

    def test_retrieve_employee_valid_id(self):
        self.e.create("John Doe", 30, 1, "HR")
        employee_info = self.e.retrieveEmp(1)
        self.assertIsNotNone(employee_info)  
        self.assertEqual(employee_info['name'], "John Doe") 

    def test_retrieve_employee_invalid_id(self):
        employee_info = self.e.retrieveEmp(10)
        self.assertIsNone(employee_info)


    def test_delete_employee_valid_id(self):
        self.e.create("John Doe", 30, 1, "HR")
        self.e.deleteEmp(1)
        self.assertEqual(len(self.e.employees), 0)  


    def test_delete_employee_invalid_id(self):
        self.e.create("John Doe", 30, 1, "HR")
        self.e.deleteEmp(2)
        self.assertEqual(len(self.e.employees), 1)  # Check if no employee was deleted for invalid ID



if __name__ == '__main__':
    unittest.main()
