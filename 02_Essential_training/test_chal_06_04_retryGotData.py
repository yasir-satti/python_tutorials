import chal_06_04_retryGotData

def test_getData50_gotData():
    chal_06_04_retryGotData.servicesAreUp = True
    result = chal_06_04_retryGotData.getWithRetry(chal_06_04_retryGotData.getData50)
    assert result == 'You got the data! that only happens 50% of the time.'
    
def test_getData25_gotData():
    result = chal_06_04_retryGotData.getWithRetry(chal_06_04_retryGotData.getData25)
    assert result == 'You got the data! that only happens 25% of the time.'
    
def test_getData10_gotData():
    result = chal_06_04_retryGotData.getWithRetry(chal_06_04_retryGotData.getData10)
    assert result == 'You got the data! that only happens 10% of the time.'
    
def test_getData50_None():
    chal_06_04_retryGotData.servicesAreUp = False
    result = chal_06_04_retryGotData.getWithRetry(chal_06_04_retryGotData.getData50)
    assert result == None
    
def test_getData25_None():
    result = chal_06_04_retryGotData.getWithRetry(chal_06_04_retryGotData.getData25)
    assert result == None
    
def test_getData10_None():
    result = chal_06_04_retryGotData.getWithRetry(chal_06_04_retryGotData.getData10)
    assert result == None
    
def test_optimised_getData50_gotData():
    chal_06_04_retryGotData.servicesAreUp = True
    result = chal_06_04_retryGotData.getWithRetryOptimised(chal_06_04_retryGotData.getData50)
    assert result == 'You got the data! that only happens 50% of the time.'
    
def test_optimised_getData25_gotData():
    chal_06_04_retryGotData.servicesAreUp = True
    result = chal_06_04_retryGotData.getWithRetry(chal_06_04_retryGotData.getData25)
    assert result == 'You got the data! that only happens 25% of the time.'
    
def test_optimised_getData10_gotData():
    chal_06_04_retryGotData.servicesAreUp = True
    result = chal_06_04_retryGotData.getWithRetryOptimised(chal_06_04_retryGotData.getData10)
    assert result == 'You got the data! that only happens 10% of the time.'
    
def test_optimised_getData50_None():
    chal_06_04_retryGotData.servicesAreUp = False
    result = chal_06_04_retryGotData.getWithRetry(chal_06_04_retryGotData.getData50)
    assert result == None
    
def test_optimised_getData25_None():
    chal_06_04_retryGotData.servicesAreUp = False
    result = chal_06_04_retryGotData.getWithRetry(chal_06_04_retryGotData.getData25)
    assert result == None
    
def test_optimised_getData10_None():
    chal_06_04_retryGotData.servicesAreUp = False
    result = chal_06_04_retryGotData.getWithRetry(chal_06_04_retryGotData.getData10)
    assert result == None