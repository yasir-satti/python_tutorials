import chal_08_04_Message_Exceptions
import pytest


def raiseTooManyMessagesException():
    listener = chal_08_04_Message_Exceptions.SaveMessages()
    sender = chal_08_04_Message_Exceptions.Messenger([listener])
    for i in range(0, 30):
        try:
            sender.send(f'This is message {i}')
        except chal_08_04_Message_Exceptions.TooManyMessagesException:
            listener.printMessages()
            sender.send(f'This is message {i}')
    listener.printMessages()


def test_raise_TooManyMessagesException():
    with pytest.raises(chal_08_04_Message_Exceptions.TooManyMessagesException):
        raiseTooManyMessagesException()