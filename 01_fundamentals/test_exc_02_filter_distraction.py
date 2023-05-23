import exc_02_filter_distraction

distractionKeywords = ['Dog', 'pet', 'music', 'Funny meme', 'Listen to this']
DISTRACTION = 'NO!'
SAFE_WATCHING = 'Safe watching!'

def test_isDistraction_Dog():
    sentence = 'You need to walk the dog.'
    result = exc_02_filter_distraction.isDistraction(sentence, distractionKeywords)
    assert result == DISTRACTION
    
def test_isDistraction_pet():
    sentence = 'This pet food is the best quality in the market.'
    result = exc_02_filter_distraction.isDistraction(sentence, distractionKeywords)
    assert result == DISTRACTION
    
def test_isDistraction_Funny_meme():
    sentence = 'This is funny meme!'
    result = exc_02_filter_distraction.isDistraction(sentence, distractionKeywords)
    assert result == DISTRACTION
    
def test_notDistraction():
    sentence = 'This is short Java course.'
    result = exc_02_filter_distraction.isDistraction(sentence, distractionKeywords)
    assert result == SAFE_WATCHING
