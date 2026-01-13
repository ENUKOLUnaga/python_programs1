import unittest
from employee1 import Employee
class test_employee(unittest.TestCase):
    def setUp(self):
        print("initializing....")
        self.emp1=Employee("First","Last",50000)
        self.emp2=Employee("First1","Last1",60000)
    def tearDown(self):
        print("after method execution")
    def test_email(self):
        print("Email")
        self.assertEqual(self.emp1.email,"First.Last@gmail.com")
        self.assertEqual(self.emp2.email,"First1.Last1@gmail.com")
        self.emp1.fn="Ram"
        self.emp2.fn="Laksman"
        self.assertEqual(self.emp1.email,"Ram.Last@gmail.com")
        self.assertEqual(self.emp2.email,"Laksman.Last1@gmail.com")
    def test_name(self):
        print("name")
        self.assertEqual(self.emp1.name,"First.Last")
        self.assertEqual(self.emp2.name,"First1.Last1")
        self.emp1.fn="Ram"
        self.emp2.fn="Lakshmana"
        self.assertEqual(self.emp1.name,"Ram.Last")
        self.assertEqual(self.emp2.name,"Lakshmana.Last1")
    def test_pay(self):
        print("pay")
        self.emp1.apply_raise()
        self.emp2.apply_raise()
        self.assertEqual(self.emp1.pay,52500)
        self.assertEqual(self.emp2.pay,63000)
if __name__=="__main__":
    unittest.main()