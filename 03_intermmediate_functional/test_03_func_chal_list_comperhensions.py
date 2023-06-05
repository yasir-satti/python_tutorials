from chal_03_func_list_comperhensions import get_sum, getSalary, isDeveloper, isNotDeveloper


employees = [{
    'name': 'Jane',
    'salary': 90000,
    'job_title': 'developer'
}, {
    'name': 'Bill',
    'salary': 50000,
    'job_title': 'writer'
}, {
    'name': 'Kathy',
    'salary': 120000,
    'job_title': 'executive'
}, {
    'name': 'Anna',
    'salary': 100000,
    'job_title': 'developer'
}, {
    'name': 'Dennis',
    'salary': 95000,
    'job_title': 'developer'
}, {
    'name': 'Albert',
    'salary': 70000,
    'job_title': 'marketing specialist'
}]


def test_return_developer():
    expectedResponse = True
    response = isDeveloper(employees[0])
    assert response == expectedResponse


def test_return_non_developer():
    expectedResponse = False
    response = isDeveloper(employees[1])
    assert response == expectedResponse


def test_get_emplyee_salary():
    expectedResponse = 90000
    response = getSalary(employees[0])
    assert response == expectedResponse