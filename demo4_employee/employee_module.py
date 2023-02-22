class Employee:
    company_name = None
    company_location = None

    def __int__(self):
        self.emp_id = None
        self.emp_name = None
        self.emp_salary = None
        self.emp_performance = None

    @staticmethod
    def print_author_name():
        print("Author name is Ravi Patel")

    def display_employee_record(self):
        print(15*'-')
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Performance:", self.emp_performance)
        print("Company name :", Employee.company_name)
        print("Company Location:", Employee.company_location)
        print(15 * '-')

    def calculate_bonus(self):
        if self.emp_performance == "A":
            self.emp_salary += self.emp_salary * 0.1
        elif self.emp_performance == "B":
            self.emp_salary += self.emp_salary * 0.05
        elif self.emp_performance == "C":
            self.emp_salary += self.emp_salary * 0.02

