# Can You Hear Me Now?
#
# Create a function "getWithRetry" that calls a function until it receives 
# response that is not None, and then returns that response. If it continues 
# to get no response, it should give up after a certain number of tries (to be decided by you)

# After filling out the "getWithRetry" function, run all of the cells in this 
# notebook in order to test the following scenarios:

# All services are up
# All services are down
# All services are down and making a request takes 0.1 seconds to execute
# What is the ideal number of retries before giving up? How do you know whether 
# the service is down or you're just unlucky?

import random

servicesAreUp = False

def getData50():
    if servicesAreUp and random.random() > 0.5:
        return 'You got the data! that only happens 50% of the time.'

def getData25():
    if servicesAreUp and random.random() > 0.25:
        return 'You got the data! that only happens 25% of the time.'
    
def getData10():
    if servicesAreUp and random.random() > 0.10:
        return 'You got the data! that only happens 10% of the time.'


def getWithRetry(dataFunc):
    f'Legacy function'
    maxRetries = 20
    for _ in range(0, maxRetries):
        result = dataFunc()
        if result:
            return result
        
def getWithRetryOptimised(dataFunc, retries=20):
    f'Refactored func'
    if retries == 0:
        return 'The Service is down!'
    else:
        return dataFunc() or getWithRetryOptimised(dataFunc, retries=retries - 1)
    
    

print(getWithRetry(getData50))

print(getWithRetry(getData25))

print(getWithRetry(getData10))

print(getWithRetryOptimised(getData50))

print(getWithRetryOptimised(getData25))

print(getWithRetryOptimised(getData10))


