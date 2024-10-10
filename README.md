# Contextual-RAG

This is an implementation of a RAG system that uses Contextual Retrieval to improve the performance of the system. The system is based on the traditional RAG system, but it uses a Contextual Embedding model to retrieve the relevant documents for the answer generation. See more [here](https://www.anthropic.com/news/contextual-retrieval)

The system accepts any kind of document, but is optimized for pdf files.

## Files

- `rag-app.py`: The main file of the system. It contains the code to run the web server and the system.
- The `utils` folder contains the code to process the documents and the queries.

## Usage

To use the system, you need to install the dependencies run the script:

```bash
pip install -r requirements.txt
```

Then you can run the system using the following command:

```bash
python rag-app.py
```

The system will start a web server that you can access using your browser.
