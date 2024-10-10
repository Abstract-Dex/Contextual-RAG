from langchain_community.document_loaders import PyPDFLoader


def fetch_info(path: str):
    loader = PyPDFLoader(
        path,
    )

    text = loader.load()
    return text
