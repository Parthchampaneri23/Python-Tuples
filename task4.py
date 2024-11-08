#Write a python program and iterate the given tuples Input: employee1 = ("John Doe", 101, "Human Resources", 60000) employee2 = ("Alice Smith", 102, "Marketing", 55000) employee3 = ("Bob Johnson", 103, "Engineering", 75000)


# Define the employee tuples
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

# Create a list of employees
employees = [employee1, employee2, employee3]

# Iterate through the list of employees and print their information
for employee in employees:
    name, emp_id, department, salary = employee
    print(f"Name: {name}, ID: {emp_id}, Department: {department}, Salary: ${salary}")
