import chal_05_04_fast_prime

def test_all_prime_to_10():
    expectedResult = [2, 3, 5, 7]
    result = chal_05_04_fast_prime.allPrimesUpTo(10)
    
    assert result == expectedResult
    
def test_all_prime_to_50():
    expectedResult = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    result = chal_05_04_fast_prime.allPrimesUpTo(50)
    
    assert result == expectedResult