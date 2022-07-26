# CS361-Microservices-Implementation
Milestone #2 - Communication contract for String Parsing Microservice

---
## Background
This microservice leverages the remote procedure call Python library `RPyC` to
receive a string input and parse it based on the client's specification.

### RPyC - Python Remote Procedure Call Library
- [Documentation](https://rpyc.readthedocs.io/en/latest/docs.html)
- [RPyC Services Tutorial](https://rpyc.readthedocs.io/en/latest/tutorial/tut3.html)

---
## Getting Started with Development
These instructions will help you get a copy of the microservice installed on your local machine.

### System Requirements
- [Python 3+](https://www.python.org/downloads/)
- [pip3](https://pypi.org/project/pip/)

### Microservice Installation

From the command line, navigate to the directory where you want the microservice
files to live and copy the source code from the repository:

```
https://github.com/markyjordan/CS361-Microservices-Implementation.git
```

Next, navigate to the newly cloned repository and install the `RPyC` python module.

> **NOTE:** You can execute the below instructions with `pip` if `pip3` has been aliased to `pip` in your system.

#### Regular Installation of RPyC Into Project Packages:
```
pip3 install rpyc
```
#### Virtual Environment `virtualenv` Installation:

First, change your directory to the microservice directory.
```
cd microservice-folder-name
```
Next, install the `virtualenv` Python module if your system doesn't already
have it installed.
```
pip3 install virtualenv
```
Initialize a new virtual env.
```
virtual venv
```
Activate the virtual environment.
```
source venv/bin/activate
```

---
## Running the Microservice and Usage Examples

### Running the Microservice Server

In the directory containing the microservice server file, open a command line
window and run the following:
```
python3 server.py
```
> **NOTE:** By default, the microservice is configured to run on PORT 18861. If
> you need to configure the microservice to run on a different PORT, you can
> modify the global `PORT` variable defined in both the `client.py` and
> `server.py` files.

At this point, the microservice server should be active and ready to receive
requests from a client.

To terminate the microservice server, enter `Ctrl + C` in the command line window.

### Sending Requests to the Microservice Server

Inorder to send a request to the microservice, your client file will need to
import the `rpyc` Python module and configure the global PORT variable with a
port number that matches the server port number defined in the `server.py` file.
Then, you will need to establish a connection to the microservice server by
calling `rpyc.connect("localhost", PORT)`.

#### Example `client.py` file:
```
import rpyc

# Configure the port number to match the server's port number.
PORT = 18861

# Establish a connection to the server
connection = rpyc.connect("localhost", PORT)
```

### How to Call the Server's Exposed Methods and Receive the Data
Using the variable in the `client.py` file that was used to establish the
connection to the microservice server (i.e. `connection` in the `client.py`
example above), the client can access two of the microservice server's exposed
string parsing methods as outlined below:

#### Exposed Method #1: splitStringWithHTML(input: str)
This method takes a multiline `string` as input and returns to the client a new
`string` with an HTML `<br>` tag inserted after each punctuation mark.

```
sample_string = "Hello. This is a multiline string. With periods. Split me with HTML. And here is an exclamation point! And then a question mark? And what about multiple?? No problem!! It just works."

splitWithHTML = connection.root.splitStringWithHTML(sample_string)
```
The variable `splitWithHTML` shown above will contain the `string` returned by
the microservice server.

#### Exposed Method #2: splitStringToList(input: str)
This method takes a string as input and returns to the client a `list` of
strings where each element is a word in the input string. If the word is the
last word in a sentence, the punctuation mark is included as part of the word in
the list element.

```
sample_string = "Hello. This is a multiline string. With periods. Split me with HTML. And here is an exclamation point! And then a question mark? And what about multiple?? No problem!! It just works."

stringToList = connection.root.splitStringToList(sample_string)
```
The variable `stringToList` shown above will contain the `list` of strings
returned by the microservice server.

> **NOTE:** The `server.py` file exposes its methods to a client by prefixing
> them with `'exposed_'` (i.e. `exposed_splitStringWithHTML(self, input)`). 
> 
> When calling an exposed method on the client side, the `exposed_` prefix is
> not included (i.e. `connection.root.splitStringWithHTML(input)`).

### UML Sequence Diagram
![UML Sequence Diagram](UML-Sequence-Diagram.png)

---
## About this Software

### Author
Mark Jordan

<br>

[Return to the Top](#CS361-Microservices-Implementation)