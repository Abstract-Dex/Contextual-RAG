class VectorEmbedder:
    def __init__(self, embedding_model, collection):
        self.embedding_model = embedding_model
        self.collection = collection

    def generate_embeddings(self, chunks):
        for i, chunk in enumerate(chunks):
            # Check if this chunk is already in the collection
            existing_data = self.collection.get(ids=[str(i)])

            # if there are no existing ids, proceed to add
            if not existing_data['ids']:
                embedding = self.embedding_model.embed(chunk)
                self.collection.add(embeddings=[embedding], documents=[
                                    chunk], ids=[str(i)])
            else:
                # Optionally print/log a message or skip
                pass  # Replace with logging or nothing if you want to suppress
