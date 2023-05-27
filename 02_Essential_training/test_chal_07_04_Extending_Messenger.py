import chal_07_04_Extending_Messenger
import re
from io import StringIO
from contextlib import redirect_stdout

dateTimeRegex = r'[0-1][1-9][-][0-3][0-9][-][1-2][0-9][0-9][0-9][ ][0-2][0-9][:][0-5][0-9][:][0-5][0-9]'

def test_send_one_message():
    message = 'one message!'
    listener = chal_07_04_Extending_Messenger.SaveMessages()
    sender = chal_07_04_Extending_Messenger.Messenger([listener])
    sender.send(message)
    response = listener.messages[0]['Message']
    assert response == message
    
def test_send_one_message_with_timestamp():
    message = 'one message!'
    listener = chal_07_04_Extending_Messenger.SaveMessages()
    sender = chal_07_04_Extending_Messenger.Messenger([listener])
    sender.send(message)
    responseMessage = listener.messages[0]['Message']
    responseTime = listener.messages[0]['Time']
    isDateTime = re.search(dateTimeRegex, responseTime)
    assert responseMessage == message
    assert isDateTime
    
def test_print_one_message_with_timestamp():
    message = 'one message!'
    expectePrintedMessage = 'Hello, there! This is the first message" Time: "05-27-2023 19:28:47'   
    capturedOutputString = StringIO()
    redirect_stdout(capturedOutputString)
    listener = chal_07_04_Extending_Messenger.SaveMessages()
    sender = chal_07_04_Extending_Messenger.Messenger([listener])
    sender.send(message)
    listener.printMessages()
    assert capturedOutputString.getvalue() == expectePrintedMessage