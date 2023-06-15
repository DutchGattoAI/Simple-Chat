import openai

# Set API key
openai.api_key = 'YOUR-API-KEY'

# Initialize the list of messages with the system message
messages = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    # Get user input
    user_input = input("User: ")
    
    # Add user input to messages
    messages.append({"role": "user", "content": user_input})
    
    # Generate model response
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo-0613",  # update this line
      messages=messages
    )
    
    # Extract the model's message from the response
    model_message = response['choices'][0]['message']['content']
    
    # Print the model's message
    print("AI: ", model_message)
    
    # Add the model's message to the messages list
    messages.append({"role": "assistant", "content": model_message})
