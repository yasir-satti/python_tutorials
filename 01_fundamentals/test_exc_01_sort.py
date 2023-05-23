import exc_01_sort

def test_sort_names_list():
    testNamesDict = dict(andi1 = 'Terry', andi2 = 'John', andi3 = 'Xavier', andi4 = 'Zeid')
    expectedResult = ['John', 'Terry', 'Xavier', 'Zeid']
    result = exc_01_sort.sortAlphabetically(testNamesDict)
    assert result == expectedResult