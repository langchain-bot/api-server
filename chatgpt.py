import os

import constants
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import DirectoryLoader

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = constants.APIKEY

loader = DirectoryLoader("./data", glob="*.txt")
index = VectorstoreIndexCreator().from_loaders([loader])


def query_question(question):
    result = index.query(question)
    return result
