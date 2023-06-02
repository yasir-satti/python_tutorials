# Create the instance attributes fullname and email in the Employee class.
# Given a person's first and last names:

#     1. Form the fullname by simply joining the first and last name together, separated by a space.

#     2. Form the email by joining the first and last name together with a .  in between, and follow it with @and.digital at the end. Make sure the entire email is in lowercase.

class Employee:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def createFullName(self):
        fullName = self.firstName + ' ' + self.lastName
        return fullName
    
    def createEmail(self):
        email = self.firstName.lower() + '.' + self.lastName.lower() + '@and.digital'
        return email

employee = Employee('Yasir', 'Satti')
print('Employee full name: ', employee.createFullName())
print('Email: ', employee.createEmail())