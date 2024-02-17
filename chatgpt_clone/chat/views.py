from django.shortcuts import render
from django.http import JsonResponse
import json
from openai import OpenAI
import openai

import os
from dotenv import load_dotenv
import time

def home(request):
    return render(request, 'chat/home.html')

def get_response(request):
    if not request.session.get('chat_history'):
        request.session['chat_history'] = []
    
    data = json.loads(request.body)

    model_name = data['modelName']
    user_input = data['userInput']
    assistant_name = data['assistantName']
    assistant_instructions = data['assistantInstructions']

    print("[~] user_input: " + user_input + str(type(user_input)))
    chat_history = request.session['chat_history']

    # Concatenate user input to chat history for context
    prompt = " ".join(chat_history + [user_input])

    ###
    print("[*] STARTING APP")

    # Load the .env file
    load_dotenv()

    # Access the secret
    secret_key = os.getenv('SECRET_KEY')

    # Use the secret (for demonstration, we'll just print it)
    print("[+] The secret key is:", secret_key)

    # Set your API key
    client = OpenAI(
        # This is the default and can be omitted
        api_key=secret_key,
    )

    assistant = client.beta.assistants.create(
        name=assistant_name,
        instructions=assistant_instructions,
        tools=[],
        model=model_name
    )

    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )

    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        print(run)
        print("[~] Waiting for response... Sleeping for 5 seconds...")
        time.sleep(5)
    

    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )

    print(messages)
    print(str(type(messages)))
    print(str(messages))

    print("---")

    # Step 1: Access the content text
    content_text = messages.data[0].content[0].text.value
    print(content_text)
    print(str(type(content_text)))

    # Update session chat history
    if len(chat_history) > 5:  # Keep last 5 exchanges
        chat_history.pop(0)
    chat_history.append(user_input)
    chat_history.append(content_text)
    request.session['chat_history'] = chat_history

    return JsonResponse({'response': content_text})
