# I'm trying to watch some LinkedIn Learning videos to complete my 
# Python Learning Pathway but I keep getting distracted by meme 
# compilations, music recommendations, pets and more on Slack.
# 
# Your job is to help me create a function that takes a string and 
# checks to see if it contains the following words or 
# phrases: "Dog" , "pet" , "music" , "Funny meme" , "Listen to this"
# If it does, return "NO!" Otherwise, return "Safe watching!"

distractionKeywords = ['Dog', 'pet', 'music', 'Funny meme', 'Listen to this']
DISTRACTION = 'NO!'
SAFE_WATCHING = 'Safe watching!'

def isDistraction(sentence, distractionKeywords):
    result = SAFE_WATCHING
    for word in distractionKeywords:
        if word.lower() in sentence.lower():
            result = DISTRACTION
    return result

print(isDistraction('My dog is running around.', distractionKeywords))
print(isDistraction('My son is running around.', distractionKeywords))