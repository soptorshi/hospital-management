def enter_data():
    argument = int(input('Press \'1\' for Patients \n \'2\' for Doctors \n \'3\' for Nurses \n \'4\'for Other staff '))
    if argument == 1:
        name = input('Enter the name:')
        age =  input('Enter age:')
        sex = input('Enter sex:')
        dept = input('Enter the department:')
        bednumber = input('Enter the bed number:')
        doctor = input('Enter the name of the doctor appointment:')
        charges = input('Enter the charge due on patient:')
        
        patients.append(Patient(name,age,sex,dept,bednumber,doctor,charges))

    elif argument ==2:
        name = input('Enter the name:')
        specialisation = input('Enter specialisation:')
        salary = int(input('Enter salary:'))
        emp_id = input('Enter employee ID:')

        doctors.append(Doctor(name,emp_id,specialisation,salary))

    elif argument == 3:
        name = input('Enter name:')
        emp_id = input('Enter employee ID:')
        salary = int(input('Enter salary:'))

        nurses.append(Nurse(emp_id,salary,name))

    elif argument == 4:
        name = input('Enter name:')
        emp_id = input('Enter employee ID:')
        salary = int(input('Enter salary:'))
        dept = input('Enter department:')

        otherstaffs.append(OtherStaffs(emp_id, salary, name, dept))

    else:
        print("Wrong Input..")

def fetch_data():
    argument = int(input('Press \'1\' for Patients \n \'2\' for Doctors \n \'3\' for Nurses \n \'4\'for Other staff '))
    if argument == 1:
        print('You have selected Patients..')
        for patient in patients:
            patient.display()
    elif argument == 2:
        print('You have selected Patients..')
        for doctor in doctors:
            doctor.display()
    elif argument ==3:
        print('You have selected Patients..')
        for nurse in nurses:
            nurse.display()
    elif argument == 4:
        print('You have selected Patients..')
        for otherstaff in otherstaffs:
            otherstaff.display()
    else:
        print('invalid input')
        
    
class Doctor:

    def __init__(self, name, employee_id, specialisation, salary):
        self.name = name
        self.employee_id = employee_id
        self.specialisation = specialisation
        self.salary = salary    
        print('details added')
    
    def display(self):
        print(self.name + ', ' + self.employee_id + ', ' + self.specialisation + ', ' + str(self.salary) )

    
doctors = []

class Patient:
    def __init__(self, name, age, sex, department, bed_number, doctor_appointed, charges_due):
        self.department = department
        self.bed_number = bed_number
        self.doctor_appointed = doctor_appointed
        self.name = name
        self.sex = sex
        self.age = age
        print('details added')

    def display(self):
        print(self.name + ', ' + self.age + ', ' + self.sex + ', ' + self.department + ', ' + self.bed_number + ', ' + self.doctor_appointed )

patients = []

class Nurse:
    def __init__(self, employee_id, salary, name ):
        self.name = name 
        self.employee_id = employee_id
        self.salary = salary
        print('details added')

    def display(self):
        print(self.name + ', ' + self.employee_id + ', ' + str(self.salary) )

nurses = []

class OtherStaffs:
    def __init__(self, employee_id, salary, name, dept):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.dept = dept
        print('details added')
    
    def display(self):
        print(self.name + ', ' + self.employee_id + ', ' + str(self.salary) + ', ' + self.dept)


otherstaffs = []

ans = 'y'

while ans == 'y':
    argument = int(input('Menu:\n Press \'0\' to Enter data. \n Press \'1\' to Fetch data.\n'))
    if argument == 0:
        enter_data()
    elif argument == 1:
        fetch_data()
    else:
        print('Wrong Input..')
    ans = input('Do you want to continue?')

    