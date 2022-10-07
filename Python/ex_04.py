#Q4
basic_salary=int(input("Enter you salary:"))

def calcGrossSalary(basic_salary):
    allowances= int((basic_salary*0.22) + (basic_salary*0.18) +(basic_salary*0.10))
    global gross_salary
    gross_salary = basic_salary + allowances
    print("Gross Salary:",gross_salary)
    

def calcNetSalary(basic_salary):
    if basic_salary>8000:
        profit_tax=200
    else:
        profit_tax = 150
    deductions = profit_tax + (0.12*basic_salary) + (0.08*basic_salary)
    net_salary=gross_salary-deductions
    print("Net Salary:",net_salary)


calcGrossSalary(basic_salary)
calcNetSalary(basic_salary)
