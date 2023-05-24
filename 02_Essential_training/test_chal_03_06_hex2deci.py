import chal_03_06_hex2deci

# def test_input_not_hex_number():
#     assert 'A' == A

def test_hex_A_to_deci_10():
    hexNum = 'A'
    expectedResult = '10'
    result = chal_03_06_hex2deci.hexToDec(hexNum)
    
    assert result == expectedResult
    
def test_hex_zero_to_deci_zero():
    hexNum = '0'
    expectedResult = '0'
    result = chal_03_06_hex2deci.hexToDec(hexNum)
    
    assert result == expectedResult
    
def test_hex_1B_to_deci_27():
    hexNum = '1B'
    expectedResult = '27'
    result = chal_03_06_hex2deci.hexToDec(hexNum)
    
    assert result == expectedResult
    
def test_hex_3C0_to_deci_960():
    hexNum = '3C0'
    expectedResult = '960'
    result = chal_03_06_hex2deci.hexToDec(hexNum)
    
    assert result == expectedResult
    
def test_hex_A6G_to_deci_None():
    hexNum = 'A6G'
    expectedResult = 'None'
    result = chal_03_06_hex2deci.hexToDec(hexNum)
    
    assert result == expectedResult
    
def test_hex_ZZTOP_to_deci_None():
    hexNum = 'ZZTOP'
    expectedResult = 'None'
    result = chal_03_06_hex2deci.hexToDec(hexNum)
    
    assert result == expectedResult
    
def test_hex_int_2_to_deci_None():
    hexNum = 2
    expectedResult = 'None'
    result = chal_03_06_hex2deci.hexToDec(hexNum)
    
    assert result == expectedResult