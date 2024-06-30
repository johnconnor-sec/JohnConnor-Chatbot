from openai import OpenAI
from IPython.display import Image, display, Audio, Markdown
import base64
import os

client = OpenAI()

# When running this, make sure to have an "images" folder where your images are stored.
IMAGE_PATH = "images/2024-06-27_23-01.png"

# Preview image for context
display(Image(IMAGE_PATH)) # I don't think I'll need to do this for my use case.

def encode_image(image_path):
    """Encodes an image file to base64"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    
base64_image = encode_image(IMAGE_PATH)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are an expert computer scientist and coder here to help with coding tasks"},
        {"role": "user", "content": [
            {"type": "text", "text": "What is the coding language being used?"},
            {"type": "image_url", "image_url": {
                "url": f"data:image/png;base64,{base64_image}"}
            }
        ]}
    ],
    stream=True,
    temperature=0.1,
)

print(response.choices[0].message.content)