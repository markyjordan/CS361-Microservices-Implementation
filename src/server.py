# Author:       Mark Jordan
# Course:       CS361 - Software Engineering I - Summer 2022
# Instructors:  L. Letaw, S. Hedaoo
# Project:      7 - Milestone #2 - Microservices Implementation
# Description:  This file contains the server code for the RPyC microservice.
# Reference:    https://rpyc.readthedocs.io/en/latest/tutorial/tut3.html

import rpyc

PORT = 18861    

class StringSplitter(rpyc.Service):
    def on_connect(self, conn):
        # code that runs when a connection is created
        # (to init the service, if needed)
        print("Thread Created")

    def on_disconnect(self, conn):
        # code that runs after the connection has already closed
        # (to finalize the service, if needed)
        print("Thread Closed")

    # Exposed Microservice Methods

    def exposed_splitStringWithHTML(self, input): # this is an exposed method
        period = self.splitPeriod(input)
        question = self.splitQuestionMark(period)
        exclamation = self.splitExclamationMark(question)
        return exclamation

    def exposed_splitStringToList(self, input, separator = ' '):
        return input.split(separator)

    # Helper Methods

    def splitPeriod(self, input):
        return input.replace('. ', '.<br>')

    def splitQuestionMark(self, input):
        return input.replace('? ', '?<br>')

    def splitExclamationMark(self, input):
        return input.replace('! ', '!<br>')


if __name__ == "__main__":
    print("\nServer Live. Listening for requests. Press Ctrl + C to cancel.\n")
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(StringSplitter, port=PORT)
    t.start()
