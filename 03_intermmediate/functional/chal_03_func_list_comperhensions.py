from functools import reduce


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


def isDeveloper(employee):
    return employee['job_title'] == 'developer'


def isNotDeveloper(employee):
    return employee['job_title'] != 'developer'


def getSalary(employee):
    return employee['salary']


developerSalaries = [getSalary(employee) for employee in employees if isDeveloper(employee)]
nonDeveloperSalaries = [getSalary(employee) for employee in employees if isNotDeveloper(employee)]


def get_sum(acc, x):
    return acc + x


totalDeveloperSalaries = reduce(get_sum, developerSalaries)
averageDeveloperSalaries = totalDeveloperSalaries / len(developerSalaries)


totalNonDeveloperSalaries = reduce(get_sum, nonDeveloperSalaries)
averageNonDeveloperSalaries = totalNonDeveloperSalaries / len(nonDeveloperSalaries)


print('Avrage developer salary is ',averageDeveloperSalaries)
print('Avrage non developer salary is ',averageNonDeveloperSalaries)
