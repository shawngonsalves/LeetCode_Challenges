# group data and fn and built on this
# attributes and methods

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        #instead of setting employee deets manually we can use automatic setup using __init__
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() +'.' +last.lower() + '@company.com'

    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def initials(self):
        return '{}{}'.format(self.first[:1], self.last[:1])
    
    def apply_raise(self):
        #Lecture 2: 
        #self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)


# CLASS vs instance of class
emp_1 = Employee("Corey", "Doe", 50000) #emp_1 is instance of class Employee
emp_2 = Employee("Hey", "Bro", 20) #emp_2 is instance of class Employee

# emp_1.first = 'Corey'
# emp_1.last = 'Doe'

print(emp_2.email) #Doe

#option one for full name
output = emp_2.full_name()
print(output)
#option two for full name
print("Option 2: ",Employee.full_name(emp_2))


initials_emp = emp_1.initials()
print(initials_emp)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

#Lecture 2: 

