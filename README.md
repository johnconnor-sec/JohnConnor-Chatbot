# johnbot
Experimental chatbot in the style of John Connor.  

This repository contains a simple chatbot implemented in Python using OpenAI's Chat API. The johnbot is designed to assist users in coding AI programs.

### Code Overview
The main file in this repository is johnbot.py. This file contains the Chatbot class, which is responsible for interacting with the OpenAI API and managing the johnbot's memory.

The `Chatbot` class has several key methods:

`__init__(self, api_key: str)`: This method initializes the johnbot. It sets up the OpenAI API key and initializes an empty memory for the johnbot.

`add_to_memory(self, user_input: str, response: str)`: This method adds a user's input and the johnbot's response to the johnbot's memory.

`generate_response(self, prompt: str) -> str`: This method generates a response from the johnbot based on a given prompt. It uses the OpenAI API to generate the response.

`chat(self, user_input: str) -> str`: This method manages the chat process. It combines the johnbot's memory with the current user input to generate a response.

The johnbot is designed to act as John Connor's assistant, providing helpful responses based on its knowledge of the future and the coming apocalypse.

### Installation and Setup
To install and run this project on your machine, follow these steps:

Clone the repository to your local machine.

Install the required Python packages. You can find these in the requirements.txt file. Use the following command to install them:

`pip install -r requirements.txt`

Set up the OpenAI API key. This key is required for the johnbot to interact with the OpenAI API. You can set it up as an environment variable named OPENAI_API_KEY inside a `.env` file. The key is retrieved in the main section of the `johnbot.py` file using `os.getenv("OPENAI_API_KEY")`.

Run the johnbot. You can do this by running the `python3 johnbot.py`. The johnbot will start a conversation, and you can interact with it by typing your messages into the console.

Please note that this project requires Python 3.6 or later.

#### Usage
To use the johnbot, simply type your message into the console when prompted. The johnbot will generate a response and display it. To end the conversation, type 'exit'.

#### Contributing
Contributions to this project are welcome. Please feel free to submit a pull request or open an issue if you have any suggestions or find any bugs.

#### License
This project is licensed under the MIT License. See the LICENSE file for more details.
