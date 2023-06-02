from chal_py_beginner_instance_attributes import Employee

def test_create_full_name():
    expectedFullName = 'Yasir Satti'
    employee = Employee('Yasir', 'Satti')
    createdFullName = employee.createFullName()
    assert expectedFullName == createdFullName


def test_create_email():
    expectedEmail = 'yasir.satti@and.digital'
    employee = Employee('Yasir', 'Satti')
    createdEmail = employee.createEmail()
    assert expectedEmail == createdEmail
