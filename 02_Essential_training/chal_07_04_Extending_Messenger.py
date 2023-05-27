# Extending the Messenger
# Create a class "SaveMessages" that extends the Messenger class that does the following things:

# 1. Add any messages it receives to a list, along with the time the message was received
# 2. Use the provided "getCurrentTime" function so that the received message time is a string
# 3. Contains a method called "printMessages" that prints all collected messages when it's called.
# 4. You might also consider clearing the message list when "printMessages" is called.

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
        # Must be implemented by extending classes
        pass


class SaveMessages(Messenger):
    def __init__(self, listeners=[]):
        super().__init__(listeners)
        self.messages = []
        
    def receive(self, message):
        self.messages.append({'Message': message, 'Time': getCurrentTime()})
        
    def printMessages(self):
        for message in self.messages:
            print(f'Message: "{message["Message"]}" Time: "{message["Time"]}"')
        self.messages = []
            
# Run this cell after you've written your solution
listener = SaveMessages()

sender = Messenger([listener])

sender.send('Hello, there! This is the first message')

listener.printMessages()