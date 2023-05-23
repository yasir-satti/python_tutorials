import exc_03_string_coder

def test_code_string_hacker_speak():
    string = 'hacker speak'
    result = exc_03_string_coder.string_coder(string)
    expectedResult = 'h4ck3r 5p34k'
    
    assert result == expectedResult
    
def test_code_string_manchester():
    string = 'manchester'
    result = exc_03_string_coder.string_coder(string)
    expectedResult = 'm4nch35t3r'
    
    assert result == expectedResult
    
def test_code_empty_string():
    string = ''
    result = exc_03_string_coder.string_coder(string)
    expectedResult = 'You typed empty string!'
    
    assert result == expectedResult
    
def test_code_not_a_string():
    string = 4
    result = exc_03_string_coder.string_coder(string)
    expectedResult = 'Input is not a string!'
    
    assert result == expectedResult