import os

from dotenv import load_dotenv
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import DirectoryLoader

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

loader = DirectoryLoader("./data", glob="*.txt")
index = VectorstoreIndexCreator().from_loaders([loader])


def query_question(question):
    result = index.query(question)
    return result
