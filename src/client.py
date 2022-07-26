# Author:       Mark Jordan
# Course:       CS361 - Software Engineering I - Summer 2022
# Instructors:  L. Letaw, S. Hedaoo
# Project:      7 - Milestone #2 - Microservices Implementation
# Description:  This file contains the sample client code for the RPyC
# microservice.
# Reference:    https://rpyc.readthedocs.io/en/latest/tutorial/tut3.html

import rpyc

def sendReqToMicroservicesServer():
    PORT = 18861    # configure the port here; must match the server port

    connection = rpyc.connect("localhost", PORT)
    print("\nSending a request to the microservice server...\n")

    sample_string = "Hello. This is a multiline string. With periods. Split me with HTML. And here is an exclamation point! And then a question mark? And what about multiple?? No problem!! It just works."
    print("Request body: ", sample_string, "\n")

    # Request Methods

    splitWithHTML = connection.root.splitStringWithHTML(sample_string)
    print("Response body: ", splitWithHTML, "\n") 

    stringToList = connection.root.splitStringToList(sample_string)
    print("Response body: ", stringToList, "\n")


if __name__ == "__main__":
    sendReqToMicroservicesServer()
    exit(0)
