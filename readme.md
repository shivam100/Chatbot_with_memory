# Chatbot with OpenAI and LangChain

This repository contains a simple chatbot that uses the OpenAI API and the LangChain Framework. The chatbot engages in conversations with users and utilizes OpenAI's text-davinci-003 model for natural language processing, uses Entity memory to remember the given facts about specific entities in a conversation. It extracts information on entities (using an LLM) and builds up its knowledge about that entity over time (also using an LLM).

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/shivam100/Chatbot_with_memory.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Chatbot_with_memory
    ```

3. Install the required dependencies. It's recommended to set up a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

4. Obtain an OpenAI API Key:
   - Visit [OpenAI](https://beta.openai.com/signup/) to sign up for an account.
   - Generate an API key from the OpenAI dashboard.


## Usage

Run the chatbot script using the following command:

```bash
python chatbot.py

-- Enter OpenAI API Key 
-- Interact with the chatbot
-- Enter "Exit" to close the Chatbot.


