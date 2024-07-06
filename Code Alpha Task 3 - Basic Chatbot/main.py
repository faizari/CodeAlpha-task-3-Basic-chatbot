"""
This script implements a simple chatbot using the NLTK library. The chatbot responds to user inputs based on predefined patterns and responses.
It supports basic conversational elements such as greetings, asking for the chatbot's name, and simple questions about the chatbot's creator
and location. The chatbot uses the 'Chat' class from 'nltk.chat.util' and predefined response patterns to simulate conversation.
Type 'quit' to exit the chat.

To run this script, make sure to install the NLTK library using:
pip install nltk
"""

import nltk
from nltk.chat.util import Chat, reflections

# Sample responses and patterns
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!", "Hi!"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot. You can call me Chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you! How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem.", "Don't worry about it."]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Nice to hear that!", "Alright, great!"]
    ],
    [
        r"(.*) (age|old are you?)",
        ["I'm a computer program, so I don't have an age.",]
    ],
    [
        r"what (.*) want?",
        ["I want to help you have a good day!",]
    ],
    [
        r"(.*) created you?",
        ["I was created by a team of developers.",]
    ],
    [
        r"(.*) (location|city)?",
        ["I'm inside a computer, so I don't have a specific location."]
    ],
    [
        r"how (.) weather in (.)?",
        ["I am a computer program and don't have access to weather information."]
    ],
    [
        r"(.*) (sports|game|sport)?",
        ["I'm a big fan of all kinds of sports. What about you?"]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!", "See you later!"]
    ],
    [
        r"(.*)",
        ["I didn't quite understand that. Could you rephrase?",]
    ],
]

def chatbot():
    print("Hi, I'm a chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
