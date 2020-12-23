class Employee:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
emp_1 = Employee("John", "Smith")
print(emp_1.firstname)