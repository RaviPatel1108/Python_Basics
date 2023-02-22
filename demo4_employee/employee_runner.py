from demo4_employee.employee_module import Employee

Employee.company_name = "e Infochips"
Employee.company_location = "Ahmedabad"

emp1 = Employee()
emp2 = Employee()
emp3 = Employee()

emp2.emp_id = 102
emp2.emp_name = "RJ"
emp2.emp_salary = 4000
emp2.emp_performance = "A"

Employee.print_author_name()
emp2.display_employee_record()
emp2.calculate_bonus()
emp2.display_employee_record()

emp1.emp_performance = "C"
emp1.emp_id = 103
emp1.emp_name = "AK"
emp1.emp_salary = 4000

emp1.display_employee_record()
emp1.calculate_bonus()
emp1.display_employee_record()
