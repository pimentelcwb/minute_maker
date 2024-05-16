# Project Title
This project is a Python application that interacts with the user, processes text from a .txt file, and uses the OpenAI API to generate a summary of the text. The user can ask questions about the summary, and the conversation can be exported to a .txt file.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
You need Python 3.x and an OpenAI API key to run this script. You can get an API key by signing up on the OpenAI website.

### Installing
1. Clone the repository to your local machine.
2. Install the required Python packages using pip:
```bash
pip install openai
```

### Usage
1. Replace 'C:/file.txt' in the caminho_arquivo variable with the path to your .txt file.
2. Replace 'XXXXXXXXXXXXXXXXXX' in the client = OpenAI(api_key="XXXXXXXXXXXXXXXXXX") line with your OpenAI API key.
3. Run the script in a Python environment. The script will read the .txt file, divide the text into parts, and generate a summary.
4. You can ask questions about the summary. Type ‘exportar’ to save the summary to a .txt file, or type ‘fim’ to end the conversation.

### Built With
Python - The programming language used
OpenAI - Used to generate the summary

### Authors
Pedro Pimentel - pimentelcwb
