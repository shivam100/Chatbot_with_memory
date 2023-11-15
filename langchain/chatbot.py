from getpass import getpass
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationEntityMemory
from langchain.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from pydantic import BaseModel
from typing import List, Dict, Any

print("Please Enter your OpenAI API KEY" + "\n")
OPENAI_API_KEY = getpass()

llm = OpenAI(model_name='text-davinci-003', 
             temperature=0, 
             openai_api_key= OPENAI_API_KEY,
             max_tokens = 256)


conversation = ConversationChain(
    llm=llm, 
    verbose=False,
    prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
    memory=ConversationEntityMemory(llm=llm)
)

print( "Welcome to the SmartBot !!. You can type \"exit\" to exit from the Chatbot. \n")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye! Will See you soon!")
        break
    bot_response = conversation.predict(input = user_input)
    print("Chatbot:", bot_response)
