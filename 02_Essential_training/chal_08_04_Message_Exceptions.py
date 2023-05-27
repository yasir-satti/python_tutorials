# Message Exceptions

# The SaveMessages class now has limited memory and should only be able
# to hold a maximum of 10 messages at once.

# This challenge has three parts, outlined in comments below.

# # 1. Finish creating the TooManyMessagesException class

# Fill in the TooManyMessagesException class. Add a custom message!

# # 2. Raise a TooManyMessagesException exception here

# Make sure that the SaveMessages class doesn't get over-full and raises an
# Exception if the max_messages limit is reached.

# # 3. Catch a TooManyMessagesException and print the messages

# Modify this code so that, if an exception is raised when the message is sent, the
# messages are printed out (emptying the message list) and the message is re-sent. Make sure to print out any remaining messages at the end!

from datetime import datetime


def getCurrentTime():
    return datetime.now().strftime("%m-%d-%Y %H:%M:%S")


class Messenger:
    def __init__(self, listeners=[]):
        self.listeners = listeners

    def send(self, message):
        for listener in self.listeners:
            listener.receive(message)

    def receive(self, message):
        pass


class TooManyMessagesException(Exception):
    def __init__(self, message):
        super().__init__(
            f'Cannot save {message}! Reached number of messages that can be saved. Please clear existing messages first.')


class SaveMessages(Messenger):
    def __init__(self, listeners=[]):
        super().__init__(listeners)
        self.messages = []
        self.max_messages = 10


    def receive(self, message):
        if len(self.messages) >= self.max_messages:
            raise TooManyMessagesException(message)
        self.messages.append({'message': message, 'time': getCurrentTime()})


    def printMessages(self):
        for m in self.messages:
            print(f'Message: "{m["message"]}" Time: {m["time"]}')
        self.messages = []


listener = SaveMessages()
sender = Messenger([listener])

for i in range(0, 30):
    try:
        sender.send(f'This is message {i}')
    except TooManyMessagesException:
        listener.printMessages()
        sender.send(f'This is message {i}')
listener.printMessages()
