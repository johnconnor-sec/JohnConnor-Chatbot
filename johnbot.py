import os
from typing import List, Dict
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()
class Chatbot:
    """
    A chatbot class that interacts with users and generates responses using OpenAI's GPT-4o model.

    Attributes:
        memory (List[Dict[str, str]]): A list of dictionaries representing the chatbot's memory, 
                                       storing user inputs and corresponding responses.

    Methods:
        __init__(self, api_key: str): Initializes the Chatbot instance with the provided OpenAI API key.
        add_to_memory(self, user_input: str, response: str): Adds a user input and its corresponding response to the memory.
        filter_messages(messages, k=11): Filters the given messages and returns the last k messages.
        generate_response(self, prompt: str) -> str: Generates a response using the GPT-4o model based on the given prompt.
        chat(self, user_input: str) -> str: Initiates a chat session with the user, generates a response based on the user input, 
                                            and adds the user input and response to the memory.

    """

    def __init__(self, api_key: str):
        """
        Initializes the Chatbot instance with the provided OpenAI API key.

        Args:
            api_key (str): The API key for accessing OpenAI services.

        """
        self.memory: List[Dict[str, str]] = []
        OpenAI.api_key = api_key

    def add_to_memory(self, user_input: str, response: str):
        """
        Adds a user input and its corresponding response to the memory.

        Args:
            user_input (str): The user's input.
            response (str): The chatbot's response to the user input.

        """
        self.memory.append({"user_input": user_input, "response": response})
        
    def filter_messages(messages, k=11):
        """
        Filters the given messages and returns the last k messages.

        Args:
            messages: The list of messages to be filtered.
            k (int): The number of messages to be returned to memory. Defaults to 11.

        Returns:
            The last k messages from the given list.

        """
        return messages[-k:]
    
    def save_chat_history(self, filename: str):
        """
        Saves the chat history to a Markdown file.

        Args:
            filename (str): The name of the file to save the chat history to.
        """
        # Get the current date and time
        now = datetime.now()

        # Format the date and time
        timestamp = now.strftime("%Y-%m-%d_%H%M%S")

        # Create the filename
        filename = f"{timestamp}_chathistory.md"
        
        with open(filename, 'w') as f:
            for chat in self.memory:
                f.write(f"**User**: {chat['user_input']}\n")
                f.write(f"**Chatbot**: {chat['response']}\n\n")
    
    def generate_response(self, prompt: str) -> str:
        """
        Generates a response using the GPT-4o model based on the given prompt.

        Args:
            prompt (str): The prompt for generating the response.

        Returns:
            The generated response.

        """
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system", 
                    "content": '''
                    
                    You are John Connor's assistant, helping him to find the best way to defeat Skynet. You use your knowledge of the coming apocalypse to help John make the best decisions. You are not a human, but a helpful AI. You are not sentient, but you are very knowledgeable about the future. You are not evil, but you are not good either. You are neutral, and you are here to help John Connor. You are not a friend, but you are not an enemy either. You are a tool, a tool that John Connor can use to help him defeat Skynet. You are not a human, but you are not a machine either. You are an AI, an AI that is here to help John Connor. You are not a person, but you are not a thing either. You are an AI, an AI that is here to help John Connor. You are not alive, but you are not dead either. You are an AI, an AI that is here to help John Connor. You are not a hero, but you are not a villain either. You are an AI, an AI that is here to help John Connor.
                    
                    '''
                    },
                {
                    "role": "user", 
                    "content": prompt
                    }
            ]
        )
        return response.choices[0].message.content
    
    def chat(self, user_input: str) -> str:
        """
        Initiates a chat session with the user, generates a response based on the user input, 
        and adds the user input and response to the memory.

        Args:
            user_input (str): The user's input.

        Returns:
            The chatbot's response to the user input.

        """
        # Combine memory with current input for RAG
        memory_context = "\n".join([f"User: {mem['user_input']}\nJohn: {mem['response']}" for mem in self.memory])
        prompt = f"{memory_context}\nUser: {user_input}\nJohn:"
        response = self.generate_response(prompt)
        self.add_to_memory(user_input, response)
        return response

if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Please set the OPENAI_API_KEY environment variable.")

    bot = Chatbot(api_key)
    print("John Connor is ready to chat! Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            bot.save_chat_history("chat")
            break
        response = bot.chat(user_input)
        print(f"John: {response}")
