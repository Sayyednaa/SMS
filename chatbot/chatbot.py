# in chatbot/chatbot.py

def get_bot_response(user_input):
    response = generate_response(user_input)
    return response
# in chatbot/chatgpt.py

import openai
import os

openai.api_key = "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"
def generate_response(user_input):
    prompt = f"{user_input}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        # stop=["\n", "User:"]

    )
    # print(response).choices[0].text.strip()
    return response["choices"][0]["text"]

# print(generate_response("Hello"))
