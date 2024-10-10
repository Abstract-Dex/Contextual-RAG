from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
import re
import os
import dotenv

dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DOCUMENT_CONTEXT_PROMPT = """
        <document>
        {doc_content}
        </document>
        """

CHUNK_CONTEXT_PROMPT = """
        Here is the chunk we want to situate within the whole document
        <chunk>
        {chunk_content}
        </chunk>

        Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk.
        Answer only with the succinct context and nothing else.
        """


def chunk_document(all_info):
    splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)

    chunks = []
    for text in all_info:
        chunks.extend(splitter.split_text(text))

    text_pattern = re.compile(r'[a-zA-Z0-9@.,:;!?$€£¥+\*/=#&%(){}\[\]<>\'"]+')

    filtered_chunks = []
    for chunk in chunks:
        extracted_text = ' '.join(text_pattern.findall(chunk))
        if extracted_text:
            filtered_chunks.append(extracted_text)

    return filtered_chunks


def generate_chunk_context(doc: str, chunk: str, llm):
    messages = [
        {
            "role": "user",
            "content": DOCUMENT_CONTEXT_PROMPT.format(doc_content=doc) + CHUNK_CONTEXT_PROMPT.format(chunk_content=chunk),
            "cache_control": {"type": "ephemeral"}  # Prompt caching
        },
    ]
    response = llm.invoke(messages)
    return response.content
