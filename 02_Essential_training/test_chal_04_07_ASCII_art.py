import chal_04_07_ASCII_art

def test_art():
    
    art='''
                eeeeeeee
        rrrrrrrr        rrrrrrr
    '''
    encodeString = chal_04_07_ASCII_art.encodeString(art)
    decodeString = chal_04_07_ASCII_art.decodeString(encodeString)
    
    assert decodeString == art