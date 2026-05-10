import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
import shutil

load_dotenv()

# model = init_chat_model('gemini-2.5-flash', model_provider='google_genai')
# response = model.invoke('who is modi')
# print(response.content)

def addFile(filename: str) -> str:
    """Create a file in current Directory"""
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            pass
        print(f"File '{filename}' created.")
    elif os.path.isdir(filename):
        print(f"File '{filename}' already exists but its a directory")
    else:
        print(f"File '{filename}' already exists.")

def removeFile(filename: str) -> str:
    """Remove a file in current Directory"""
    if os.path.exists(filename):
        if os.path.isfile(filename):
            os.remove(filename)
            print(f"File '{filename}' removed.")
        else:
            print(f"Cannot remove '{filename}' because it is not a file.")
    else:
        print(f"File '{filename}' already removed.")

def addFolder(filename: str) -> str:
    """Create a directory in current Directory"""
    if not os.path.exists(filename):
        os.mkdir(filename)
        print(f"File '{filename}' created.")
    elif os.path.isdir(filename):
        print(f"File '{filename}' exists.")
    else:
        print(f"File '{filename}' exists but it is not a directory so we creted.")

def removeFolder(filename: str) -> str:
    """Remove a directory in current Directory"""
    if os.path.exists(filename):
        if os.path.isdir(filename):
            shutil.rmtree(filename)
            print(f"Directory '{filename}' removed.")
        else:
            print(f"Cannot remove '{filename}' because it is not a directory.")
    else:
        print(f"Directory '{filename}' doesnot exists.")
    


# agents = create_agent(
#     model='google_genai:gemini-2.5-flash',
#     tools=[addFile, addFolder, removeFile, removeFolder]
# )

agents = create_agent(
    model="openai:gpt-5.4-mini",
    tools=[addFile, addFolder, removeFile, removeFolder]
)

responses = agents.invoke(
    {
        "messages":[
            {
                "role":"user",
                "content":"delete the file name manaru"
            }
        ]
    }
)

print(responses['messages'][-1].content)