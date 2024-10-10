import re
from rank_bm25 import BM25Okapi


def create_bm25_index(final_contextualized_chunks):
    tokenized_chunks = [re.findall(r'\w+', chunk.lower())
                        for chunk in final_contextualized_chunks]
    bm25 = BM25Okapi(tokenized_chunks)
    return bm25
